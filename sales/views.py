from django.shortcuts import render,redirect
from django.views import View 
from django.views.generic import TemplateView,FormView,CreateView
from account.models import Products,Cart,Orders
from django.views.generic import ListView,TemplateView,FormView,DetailView
from django.contrib import messages
# Create your views here.


class CustomerHomeView(TemplateView):
    template_name="home.html"
    


class ProductListView(ListView):
    template_name='productlist.html'
    queryset=Products.objects.all()
    context_object_name="products"
    def get_queryset(self):
        cat=self.kwargs.get('cat')
        return self.queryset.filter(category=cat)
    
    
class ProductDetailView(DetailView):
    template_name="productdetails.html"
    queryset=Products.objects.all()
    context_object_name="product"
    pk_url_kwarg="pid"
    
    
    
def addtocart(request,*args,**kwargs):
    try:
        pid=kwargs.get('id')
        product=Products.objects.get(id=pid)
        user=request.user
        cartcheck=Cart.objects.filter(product=product,user=user).exists()
        if cartcheck:
            cartitem=Cart.objects.create(product=product,user=user)
            cartitem.quantity+=1
            cartitem.save()
            messages.success(request,"cart-item quantity increased")
            return redirect('home')
        else:
            Cart.objects.create(product=product,user=user)
            messages.success(request,f"{product.ProductName}Added to cart")
            return redirect ('home')
    except Exception as e:
        print(e)
        messages.warning(request,"something went wrong")
        return redirect('home')  
    
class CartListview(ListView):
        template_name="cart.html"
        queryset=Cart.objects.all()
        context_object_name="carts"
        
        def get_queryset(self):
            qs=self.queryset.filter(user=self.request.user)
            return qs
        
        
class OrderListView(ListView):
    template_name='orders.html'
    queryset=Orders.objects.all()
    context_object_name='orders'
    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user)
    
    

    
def deletecartitem(request,*args,**kwargs):
    try:
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        cart.delete()
        messages.success(request,"item removed from cart")
        return redirect('cartlist')
    except:
        messages.warning(request,"spomething went wrong!!")
        return redirect('cartlist')
    
    
    

def placeorder(request,**kwargs):
    try:
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        Orders.objects.create(product=cart.product,user=request.user,quantity=cart.quantity)
        cart.delete()
        messages.success(request,f'{cart.product.title}\' s order placed')
        return redirect('cartlist')
    
    except:
        messages.warning(request,"spomething went wrong!!")
        return redirect('cartlist')