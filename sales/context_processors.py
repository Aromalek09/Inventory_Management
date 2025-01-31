from account.models import Cart

def item_count(request):
    if request.user.is_authenticated:
        cart_count=Cart.objects.filter(user=request.user).count()
        
        return {'cart':cart_count}
    else:
        return {"cart":0}