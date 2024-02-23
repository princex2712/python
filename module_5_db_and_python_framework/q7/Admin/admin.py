from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import ProductModel,ProductSubCategory

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(ProductModel)
admin.site.register(ProductSubCategory)