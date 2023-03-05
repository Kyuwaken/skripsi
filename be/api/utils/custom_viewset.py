import pprint
from django.http import Http404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from api.utils.serialize import Serializer
from api.utils.generate import generate, generate_structure
from api.models import AuditLog
# from api.utils.query import query_debugger


class CustomGetGlobalRawObject:
    def get_raw_global_object(self, pk):
        model = self.get_queryset().model
        try:
            return model.global_objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404


class CustomGetDeletedRawObject:
    def get_raw_deleted_object(self, pk):
        model = self.get_queryset().model
        try:
            return model.deleted_objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404


class CustomGetRawObject:
    def get_raw_object(self, pk):
        model = self.get_queryset().model
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404


class CustomListModelMixin:
    # @query_debugger
    def list(self, request, *args, **kwargs):
        queryset, structure = generate(request.GET, self.get_queryset())
        serializer = Serializer(queryset, self.serializer_class.Meta.model.__name__, many=True,
                                structure=structure)
        return Response(serializer.data)


class CustomRetrieveModelMixin:

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_raw_object(kwargs['pk'])
        queryset, structure = generate(request.GET, instance)
        serializer = Serializer(instance, self.serializer_class.Meta.model.__name__, many=False,
                                structure=structure)
        return Response(serializer.data)


class CustomListHistoriesModelMixin:

    @action(detail=True)
    def histories(self, request, *args, **kwargs):
        instance = self.get_raw_global_object(kwargs['pk'])
        logs = AuditLog.objects.filter(
            entity_id=instance.id,
            content_type=AuditLog().get_content_type(instance)
        )
        structure = dict(generate_structure(AuditLog))
        serializer = Serializer(logs, AuditLog.__name__, many=True, structure=structure)
        return Response(serializer.data)


class CustomModelViewSet(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         CustomGetRawObject,
                         CustomGetGlobalRawObject,
                         CustomRetrieveModelMixin,
                         CustomListModelMixin,
                         viewsets.GenericViewSet):
    pass


class CustomModelWithHistoryViewSet(mixins.CreateModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    CustomGetRawObject,
                                    CustomGetGlobalRawObject,
                                    CustomGetDeletedRawObject,
                                    CustomRetrieveModelMixin,
                                    CustomListModelMixin,
                                    CustomListHistoriesModelMixin,
                                    viewsets.GenericViewSet):
    pass


class CustomReadOnlyModelViewSet(viewsets.GenericViewSet,
                                 CustomGetRawObject,
                                 CustomGetGlobalRawObject,
                                 CustomGetDeletedRawObject,
                                 CustomRetrieveModelMixin,
                                 CustomListModelMixin):
    pass


class CustomHistoryModelViewSet(CustomGetGlobalRawObject,
                                CustomGetDeletedRawObject,
                                CustomGetRawObject,
                                CustomListHistoriesModelMixin,
                                viewsets.GenericViewSet):
    pass
