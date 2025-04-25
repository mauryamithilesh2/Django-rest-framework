from rest_framework import routers
from .viewset import TasklistViewset,TaskViewSet,AttachmentViewSet

app_name = 'task'

router=routers.DefaultRouter()
router.register('tasklists',TasklistViewset , basename = 'tasklist')

router.register('tasks',TaskViewSet)
router.register('attachments',AttachmentViewSet,basename='attachment')