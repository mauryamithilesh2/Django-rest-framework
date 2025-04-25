from rest_framework import viewsets,mixins,response,status,filters
from .serializers import TasklistSerializers,TaskSerializer,AttachmentSerializer
from .models import Task,Tasklist,Attachment,COMPLETE,NOT_COMPLETE
from .permissions import IsAllowToEditTasklistElseNone, IsAllowToEditTaskElseNone,IsAllowEditAttachmentElseNone
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework import status as s

from django_filters.rest_framework import DjangoFilterBackend

class TasklistViewset(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      #  mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    
    permission_classes=[IsAllowToEditTasklistElseNone,]
    queryset = Tasklist.objects.all()
    serializer_class=TasklistSerializers




class TaskViewSet(viewsets.ModelViewSet):

    permission_classes=[IsAllowToEditTaskElseNone,]    # the content or list writen in it  is imported from permission file
    queryset=Task.objects.all()
    serializer_class= TaskSerializer

    # defination for djnago filteraion  and search
    filter_backends=[filters.SearchFilter , DjangoFilterBackend]
    search_fields = ['name','description',]
    filterset_fields = ['status',]

    def get_queryset(self):
       
        queryset = super(TaskViewSet, self).get_queryset()
        user_profile = self.request.user.profile
        update_queryset = queryset.filter(created_by=user_profile)
        return update_queryset


    @action(detail=True,methods=['patch'])
    def update_task_status(self,request,pk=None):
        try:
            task= self.get_object()
            profile = request.user.profile
            status = request.data['status']
            if (status == NOT_COMPLETE):
                if(task.status == COMPLETE):
                    task.status = NOT_COMPLETE
                    task.completed_on = None
                    task.completed_by = None
                else:
                    raise Exception("Task is already marked as not completed. ")    
            elif(status==COMPLETE):
                if(task.status == NOT_COMPLETE):
                    task.status = COMPLETE
                    task.completed_on = timezone.now()
                    task.completed_by= profile
                else:
                    raise Exception("Task is already marked completed. ") 
            else:
                raise Exception("incorrect ststus provided.")
            task.save()
            serializer = TaskSerializer(instance=task,context = {'request':request})   
            return response.Response(serializer.data,status=s.HTTP_200_OK)

        except Exception as e:
            return response.Response({'detail':str(e)}, status=s.HTTP_400_BAD_REQUEST)

class AttachmentViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
     permission_classes=[IsAllowEditAttachmentElseNone]                  # the content or list writen in it  is imported from permission file
     queryset= Attachment.objects.all()
     serializer_class=AttachmentSerializer