from django.urls import path
from .views import *
from sales.views import *
urlpatterns=[
    path('log',LoginView.as_view(),name='log'),
    path('reg',RegView.as_view(),name='reg'),
    path('lgout',logoutview.as_view(),name="logout"),
    path('removeitem<int:id>',deletecartitem,name='delcart'),
]