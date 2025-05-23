from rest_framework import serializers
# from task.models import
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    members_count = serializers.IntegerField(read_only = True)
    members = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='profile-detail')
    manager = serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')
    lists = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='tasklist-detail')
    
    class Meta:
        model = House
        fields = ['url','id','image','name','created_on',
                  'manager','description','members_count','members','points',
                  'completed_tasks_count','notcompleted_tasks_count','lists']
        read_only_fields = ['points','completed_tasks_count','notcompleted_tasks_count']
