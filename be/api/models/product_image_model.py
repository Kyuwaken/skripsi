from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel
from django.db.models import Max
import os
def file_path(instance, filename):
    # prodImg =ProductImage.objects.all()
    # nextId = prodImg.aggregate(Max('id'))['id__max'] + 1 if prodImg else 1
    name = instance.product.seller.username + '/' + str(instance.product.id) + '/' + str(instance.product.id) + '_' + filename
    return os.path.join('products/',name)

class ProductImage(TimestampModel, UserTrackModel):
    product = auto_prefetch.ForeignKey(
        'Product', on_delete=models.CASCADE, null=True, db_constraint=False, related_name='product_image')
    image = models.ImageField(upload_to=file_path, null=True)
    