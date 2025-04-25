from rest_framework import routers

from .viewset import HouseViewset

app_name ="house"
router = routers.DefaultRouter()
router.register('houses', HouseViewset)
