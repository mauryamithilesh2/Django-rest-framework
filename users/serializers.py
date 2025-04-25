from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='user-detail')
    class Meta:
        model=Profile
        fields = ['url','id','user','image']





#how to create a viewset
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True,required=False)
    old_password = serializers.CharField(write_only=True,required=False)
    # for automatically generate username using firstname and lastname
    username=serializers.CharField(read_only=True)
    profile = ProfileSerializer(read_only=True)



    # user serialize custom validation
    def validate(self,data):
        request_method = self.context['request'].method
        password = data.get('password',None)
        if request_method=='POST':
            if password==None:
                raise serializers.ValidationError({"please provide apassword"})
        elif request_method=='PUT' or request_method=='PATCH':
            old_password= data.get('old_password',None)
            if password!=None and old_password==None:
                raise serializers.ValidationError({"info":"please provide the old password."})
        return data

    def create(self,validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
    
    def update(self,instance,validated_data):
        try:
            user = instance
            if 'password' in validated_data:
                password = validated_data.pop('password')
                old_password = validated_data.pop('old_password')
                if user.check_password(old_password):
                    user.set_password(password)
                else:
                    raise Exception("Old password is incorrect.") 
                user.save()
            
        except Exception as err:
            raise serializers.ValidationError(err)

        return super(UserSerializer,self.update(instance,validated_data))   

    class Meta:    # basic things of serializers
        model = User
        fields = ['url','id','username','email','first_name','last_name','email','password','old_password','profile']