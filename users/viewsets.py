from django.contrib.auth.models import User
from rest_framework import viewsets,mixins
from .serializers import UserSerializer , ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly
from .models import Profile

class UserViewsets(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProfileViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                     #mixins.ListModelMixin,mixins.CreateModelMixin,
                    # mixins.DestroyModelMixin
                     ):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
