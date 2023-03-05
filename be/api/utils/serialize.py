import six
import api.models as models_api
import auto_prefetch
from django.db import models
from django.apps import AppConfig
import json


class SerializerMeta(type):
    mapping_model_field = {}

    def __new__(mcs, name, bases, attrs):
        selected_models = [models_api]
        for selected_model in selected_models:
            for model_name in selected_model.app:
                model = getattr(selected_model, model_name)

                mcs.mapping_model_field[model_name] = {field.name: construct_field(field) for field in
                                                       model._meta.fields}

        real_cls = super(SerializerMeta, mcs).__new__(mcs, name, bases, attrs)
        real_cls.mapping_model_field = mcs.mapping_model_field

        return real_cls


def construct_field(field):
    return {
        'type': 1 if isinstance(field, auto_prefetch.ForeignKey) or isinstance(field, models.ForeignKey) else 0,
        'attname': field.attname,
        'name': field.name,
        'is_parse_json': getattr(field, 'parse_json', False) if isinstance(field, models.TextField) else False,
        'related_model': field.related_model.__name__ if isinstance(field, auto_prefetch.ForeignKey) or isinstance(
            field, models.ForeignKey) else None
    }


class Serializer(six.with_metaclass(SerializerMeta)):
    def __init__(self, instance=None, model_name=None, many=None, structure=None, limit=2, **kwargs):
        self.instance = instance
        self.model_name = model_name
        self.many = many
        self._data = None
        self.limit = limit
        self.structure = structure
        # print(json.dumps(self.structure, indent=4))

    @property
    def data(self):
        if self._data is None:
            self._data = self.to_value(self.instance, 0, "", self.many)
        return self._data

    def to_value(self, instance, level, field, many):
        if field:
            fields = field
        else:
            fields = self.structure
        if many:
            serialize = self._serialize
            return (dict(serialize(o, fields, level)) for o in instance)
        return dict(self._serialize(instance, fields, level))

    def _serialize(self, o, fields, level):
        for field_key, fields_data in fields.items():
            if fields_data['type'] == 0:
                if fields_data['is_parse_json']:
                    yield field_key, json.loads(getattr(o, fields_data['name']))
                else:
                    yield field_key, getattr(o, fields_data['name'])
            else:
                if fields_data['fields']:
                    if getattr(o, fields_data['name']):
                        yield field_key, self.to_value(getattr(o, fields_data['name']),
                                                       level + 1, fields_data['fields'], False)
                    else:
                        yield field_key, getattr(o, fields_data['attname'], None)
                else:
                    yield field_key, getattr(o, fields_data['attname'], None)
