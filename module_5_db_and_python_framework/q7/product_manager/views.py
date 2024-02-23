from django.shortcuts import render,redirect
from Admin.models import ProductModel,ProductSubCategory
from django.db.models import Q

# Create your views here.
def dashboard_view(request):
    products = ProductSubCategory.objects.all()
    context = {
        'products':products
    }
    return render(request,'product_manager/dashboard.html',context)

def search_view(request):
    if request.method=="POST":
        query = request.POST['search_query']
        try:
            product = ProductSubCategory.objects.filter(Q(product_model__icontains=query))
            more_product = ProductSubCategory.objects.filter(Q(product__product_name__icontains=query))
            products = list(product)+list(more_product)

        except ProductSubCategory.DoesNotExist:
            return redirect('dashboard_view')
        else:
            context =  {
                'products':products 
            }
            return render(request,'product_manager/search_res.html',context)
    return render(request,'product_manager/search_res.html')
