from django.db import router
from django.urls import path,include
from hello1.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('crud',views.UserViewSet,basename='user')
router.register('crud1',views.ProductViewSet,basename='product')


# This api url 
urlpatterns=[
    path('',include(router.urls))
]