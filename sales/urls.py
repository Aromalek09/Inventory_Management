from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('home',CustomerHomeView.as_view(),name='home'),
    path('plist/<str:cat>',ProductListView.as_view(),name='plist'),
    path('pdetail/<int:pid>',ProductDetailView.as_view(),name='pdetail'),
    path('carts',CartListview.as_view(),name='cartlist'),
    path("cart/<int:id>",addtocart,name='acart'),
    path('orderlist',OrderListView.as_view(),name='orders'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)