from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ProductModel(BaseModel):
    product_name = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.product_name) 

class ProductSubCategory(BaseModel):
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    product_price = models.DecimalField(decimal_places=2,max_digits=10)
    product_image = models.ImageField(upload_to='product_images/')
    product_model = models.CharField(max_length=255)
    product_ram = models.CharField(max_length=50)

    def __str__(self):
        return str(self.product_model) 