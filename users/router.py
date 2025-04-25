from rest_framework import routers

from .viewsets import UserViewsets,ProfileViewSet
app_name = "users"

router = routers.DefaultRouter()
router.register('users',UserViewsets) 
router.register('profiles',ProfileViewSet)