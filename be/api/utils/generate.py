from django.db.models import ForeignKey
from django.db import models
import auto_prefetch
from skripsi.settings import ENV_VARIABLE
from django.db.models.query import QuerySet
import pprint
from django.db.models import Prefetch


# DetailTransaksi.objects.all().filter("transaksi__tanggal_transaksi__month=")


def generate_structure(model):
    for field in vars(model._meta)['fields']:
        yield field.name, {
            'type': 1 if isinstance(field, ForeignKey) else 0,
            'attname': field.attname,
            'name': field.name,
            'is_parse_json': getattr(field, 'parse_json', False) if isinstance(field, models.TextField) else False,
            'related_model_name': field.related_model.__name__ if isinstance(field,
                                                                             auto_prefetch.ForeignKey) or isinstance(
                field, models.ForeignKey) else None,
            'related_model': field.related_model,
            'fields': {},
            'limit': None,
            'offset': None,
            'many': False
        }


def generate_foreign(model):
    return {x.name: x.related_model for x in vars(model._meta)['fields'] if x.related_model}


def generate_include(structure):
    pass


def generate_fields(structure, fields, level, is_exclude):
    only = [] if level == 0 else {}
    temp_fields = []
    for field in fields:
        result = field.split(".")
        n = len(result)
        if n > level + 1:
            temp_fields.append(field)
        if is_exclude:
            if n == level + 1:
                field = result[level]
        else:
            field = result[level]
        if level > 0:
            if result[level - 1] in structure.keys():
                if result[level - 1] in only:
                    only[result[level - 1]].append(field)
                else:
                    only[result[level - 1]] = [field]
        else:
            if field in structure.keys():
                only.append(field)
    if level > 0:
        for key in only.keys():
            set_data = structure[key]['fields'].keys() & set(only[key]) \
                if is_exclude else structure[key]['fields'].keys() - set(only[key])
            for x in set_data:
                del structure[key]['fields'][x]
    else:
        set_data = structure.keys() & set(only) if is_exclude else structure.keys() - set(only)
        for x in set_data:
            del structure[x]

    return structure, only, temp_fields


def generate_list_offset_limit(word, data):
    list_result = {}
    for key, value in data:
        try:
            number = int(value[len(value) - 1])
            if number >= 0:
                key = key[len(word) + 1:-1]
                list_result[key] = value
        except ValueError:
            pass
    return list_result


def generate_nested_offset(structure, relations, level):
    print("masuk")
    only = [] if level == 0 else {}
    temp_fields = []
    for relation in relations:
        result = relation.split(".")
        n = len(result)
        print(result)
    pass


def generate_queryset_from_dict(stucture):
    pass


def generate(query, queryset):
    if isinstance(queryset, QuerySet):
        model = queryset.model
    else:
        model = queryset

    query = dict(query)
    limit = None
    offset = None
    only = []
    defer = []
    order_by = []
    structure = dict(generate_structure(model))

    # Construct Field Query Params
    if 'fields' in query:
        structure, only, query['fields'] = \
            generate_fields(structure, query['fields'][len(query['fields']) - 1].split(','), 0, False)

    # Construct Exclude Query Params
    if 'exclude' in query:
        structure, defer, query['exclude'] = \
            generate_fields(structure, query['exclude'][len(query['exclude']) - 1].split(','), 0, True)
        # del query['exclude']

    # Construct Offset Query Params
    if 'offset' in query:
        try:
            offset = int(query['offset'][len(query['offset']) - 1])
        except ValueError:
            pass
        del query['offset']

    # Construct Nested Offset Query Params
    list_offset = [(key, value) for key, value in query.items() if key.startswith("offset[") and key.endswith("]")]
    for key, value in list(query.items()):
        if key.startswith("offset[") and key.endswith("]"):
            del query[key]
    list_offset = generate_list_offset_limit('offset', list_offset)
    print(list_offset)

    # Construct Limit Query Params
    if 'limit' in query:
        try:
            if offset:
                limit = int(query['limit'][len(query['limit']) - 1]) + offset
            else:
                limit = int(query['limit'][len(query['limit']) - 1])
        except ValueError:
            pass
        del query['limit']

    # Construct Nested Limit Query Params
    list_limit = [(key, value) for key, value in query.items() if key.startswith("limit[") and key.endswith("]")]
    for key, value in list(query.items()):
        if key.startswith("limit[") and key.endswith("]"):
            del query[key]
    list_limit = generate_list_offset_limit('limit', list_limit)
    print(list_limit)

    if 'include' in query:
        foreign = generate_foreign(model)
        includes = [x.strip() for x in query['include'][len(query['include']) - 1].split(',')]
        check = {}
        new_check = {}
        for i in range(ENV_VARIABLE.get('MAX_LEVEL_INCLUDE', 1)):
            relations = list(includes)
            count_deleted = 0
            for index in range(len(relations)):
                result = relations[index].split(".")
                n = len(result)
                if n - 1 == i:
                    if i == 0:
                        if relations[index] in foreign.keys() and relations[index] in structure:
                            structure[relations[index]]['fields'] = dict(
                                generate_structure(structure[relations[index]]['related_model']))
                            new_check[result[i]] = structure[relations[index]]
                    elif check:
                        parent_field = check.get(result[i - 1], False)
                        if parent_field:
                            field = parent_field['fields'].get(result[i], False)
                            if field and field['related_model']:
                                field['fields'] = dict(generate_structure(field['related_model']))
                                new_check[result[i]] = field

                    del includes[index - count_deleted]
                    count_deleted += 1

            if 'fields' in query:
                if query['fields']:
                    new_check, tas, query['fields'] = \
                        generate_fields(new_check, query['fields'], i + 1, False)
            if 'exclude' in query:
                if query['exclude']:
                    new_check, tas, query['exclude'] = \
                        generate_fields(new_check, query['exclude'], i + 1, True)
            #
            if list_offset:
                generate_nested_offset(new_check, list_offset, i + 1)
            # pprint.pprint(new_check)
            # print()
            check = new_check
            new_check = {}

            if not check:
                break

            if len(includes) == 0:
                break

        del query['include']

    # Construct Order By Query Params
    if 'order_by' in query:
        order_by = query['order_by'][len(query['order_by']) - 1].split(',')
        del query['order_by']

    # Construct Fields In Query Params
    if 'fields' in query:
        del query['fields']

    # Construct Exclude In Query Params
    if 'exclude' in query:
        del query['exclude']

    # List filter
    list_filter = ['__exact', '__iexact', '__contains', '__icontains', '__in', '__gt', '__gte', '__lt',
                   '__lte', '__startswith', '__istartswith', '__endswith', '__iendswith', '__range',
                   '__month', '__day', '__iso_year']

    # Construct Filter In Query Params
    for x in query.copy():
        if any(([y in x for y in list_filter])):
            if "__in" not in x:
                query[x] = query[x][len(query[x]) - 1]
            else:
                query[x] = query[x][len(query[x]) - 1].split(',')
        else:
            del query[x]

    if isinstance(queryset, QuerySet):
        if order_by:
            if only:
                queryset = queryset.filter(**query).only(*only).defer(*defer).order_by(*order_by)[offset:limit]
            else:
                queryset = queryset.filter(**query).defer(*defer).order_by(*order_by)[offset:limit]
        else:
            if only:
                queryset = queryset.filter(**query).only(*only).defer(*defer)[offset:limit]
            else:
                queryset = queryset.filter(**query).defer(*defer)[offset:limit]

        return queryset, structure
    else:
        return model, structure
