from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class BooksAPIModel(BaseModel):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    isbc = models.IntegerField(null=True,blank=True)
    publisher = models.CharField(max_length=255,blank=False)


