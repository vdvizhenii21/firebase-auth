from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['bio','dob']


class UserSerializer(serializers.ModelSerializer):    
    userprofile = UserProfileSerializer()
    def update(self, instance,validated_data):
        if(not instance.username == 
                        self.context['request'].user.username):
            raise exceptions.PermissionDenied('You do not have permission to update')
        profile_data = validated_data.pop('userprofile')
        if(not hasattr(instance,'userprofile')):
            instance.userprofile = UserProfile.objects.create(user=instance,**profile_data)
        else:
            instance.userprofile.dob = profile_data["dob"]
            instance.userprofile.bio = profile_data["bio"]
            instance.userprofile.save()
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance
        
    class Meta:
        model = User
        fields = ['last_name','first_name','userprofile']