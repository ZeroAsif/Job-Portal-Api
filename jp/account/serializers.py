from rest_framework import serializers
from account.models import User,UserProfile,Eductaion,UserExperience,UserAdditionalInfo,UserSkills

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model= User
        fields = ['email', 'name','gender','password','password2','tc']
        extra_kwargs ={
            'password':{'write_only':True}
        }
# password vailidation
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password dons't match")
        return super().validate(attrs)

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerialzer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']


# UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields=['user','image']

# education
class UserEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eductaion
        fields = '__all__'

class UserExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExperience
        fields = '__all__'


class UserAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdditionalInfo
        fields = '__all__'

class UserSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkills
        fields = '__all__'

# Update
class UserEduUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Eductaion
        fields = '__all__'

class UserExUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserExperience
        fields = '__all__'

class UserSkillUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserSkills
        fields = '__all__'


class UserAddInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserAdditionalInfo
        fields = '__all__'


class UserEduDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Eductaion
        fields = '__all__'