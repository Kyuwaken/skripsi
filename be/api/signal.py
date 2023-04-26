from django.contrib.auth.models import AnonymousUser
from django.db.models import signals
from api.models import *
from api.middleware.custom_get_current_middleware import get_current_user
from api.utils.serialize import Serializer
from django.core.serializers.json import DjangoJSONEncoder
import json
from api.utils.generate import generate_structure
from django.dispatch import receiver
from datetime import datetime, date

def is_date_type(instance, x):
    return type(getattr(instance, x)) == date or type(getattr(instance, x)) == datetime

def audit_trail_created_updated(sender, instance, created,update_fields, **kwargs):
    structure = dict(generate_structure(instance._meta.model))
    serializer = Serializer(instance,
                            sender.__name__,
                            many=False,
                            structure=structure)
    action = Log.CREATED
    if not created:
        log = Log.objects.filter(
            object_id=instance.id,
            content_type=Log().get_content_type(instance),
        ).order_by('action_time').first()  #this is not used
        # serialize_data = json.loads(log.serialized_data)

        # if serialize_data.get('is_deleted'):
        #     print("blank")
        # else:
        if instance.is_deleted is True:
            action = Log.DELETED
        else:
            action = Log.UPDATED
    full = []
    if not created and instance.is_deleted is False:
        serializer_prev = Serializer(instance.prev,
                        sender.__name__,
                        many=False,
                        structure=structure)
        changes = {}
        changes_after = {}
        # print([a for a in dir(instance.prev) if not a.startswith('__')])
        for x in serializer.data:
            # if getattr(instance,x).__str__() != getattr(instance.prev,x).__str__() and x != 'updated_at': ## also can 
            if serializer.data[x] != serializer_prev.data[x] and x != 'updated_at':
                temps ={}
                try:                  
                    temps["field"]= x
                    temps["before"] = getattr(instance.prev, x).strftime(
                        "%d %B %Y") if is_date_type(instance.prev,x) else getattr(instance.prev, x).__str__()
                    temps["after"] = getattr(instance, x).strftime(
                        "%d %B %Y") if is_date_type(instance,x) else getattr(instance, x).__str__()
                    # changes[x] = getattr(instance,x).__str__() ## if item is foreign key
                    # changes_after[x] = getattr(instance,x).__str__() ## if item is foreign key
                    full.append(temps)
                except AttributeError:
                    # changes[x] = getattr(instance.prev,x)
                    # changes_after[x] = getattr(instance,x) 
                    temps["field"]= x
                    temps["before"] = getattr(instance.prev, x).strftime(
                        "%d %B %Y") if is_date_type(instance.prev,x) else getattr(instance.prev, x)
                    temps["after"] = getattr(instance, x).strftime(
                        "%d %B %Y") if is_date_type(instance,x) else getattr(instance, x)
                    full.append(temps)
    else:
        temps ={}
        for x in serializer.data:
            if type(getattr(instance, x)) == date or type(getattr(instance, x)) == datetime:
                temps[x]= getattr(instance, x).strftime("%d %B %Y")
                continue
            try :
                temps[x] = getattr(instance,x).__str__()
            except:
                temps[x] = getattr(instance,x)
        full.append(temps)

    #print(get_current_user())
    # userDetail = get_current_user()
    # if get_current_user()!='AnonymousUser':
    #     try:
    #         userDetail = CustomUser.objects.get(username=get_current_user()).display_name
    #         #print(userDetail , "Signal")
    #     except:
    #         userDetail= get_current_user()

    user = get_current_user()
    try:
        user = User.objects.get(pk=user['id'])
    except:
        user = None
    
    log = Log(
        user=user.__str__() if user else None,
        object_id=instance.id,
        serialized_data=json.dumps(full, cls=DjangoJSONEncoder),
        object_repr=instance.__class__.__name__,
        content_type=Log().get_content_type(instance),
        action=action
    )
    
    log.save() if len(full) > 0 else None

def set_state_before_save(sender, instance, **kwargs):
    try:
        instance.prev = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass # Object is new, so field hasn't technically changed


def audit_trail_deleted(sender, instance, **kwargs):
    structure = dict(generate_structure(instance._meta.model))
    serializer = Serializer(instance,
                            sender.__name__,
                            many=False,
                            structure=structure)
    user = get_current_user()
    
    log = Log(
        user=user.__str__() if user else None,
        object_id=instance.id,
        serialized_data=json.dumps(serializer.data, cls=DjangoJSONEncoder),
        object_repr=instance.__class__.__name__,
        content_type=Log().get_content_type(instance),
        action=Log.DELETED
    )
    log.save()

# @receiver(signals.post_save, sender=SubGroup) this is for trying reciever
# def helloworld(sender,update_fields,*args,**kwargs):
#     print("helloworlds" ,update_fields)

model_classes = [Category, Country, Courier, MasterStatus, PaymentMethod, Payment, PaymentType, Product, ProductReview, Role, TransactionDetail, Transaction, TransactionStatus, User]

for model_class in model_classes:
    signals.post_save.connect(audit_trail_created_updated, sender=model_class)

for model_class in model_classes:
    signals.post_delete.connect(audit_trail_deleted, sender=model_class)

for model_class in model_classes:
    signals.pre_save.connect(set_state_before_save, sender=model_class)