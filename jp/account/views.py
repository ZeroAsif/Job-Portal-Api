from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from account.serializers import UserRegistrationSerializer,UserLoginSerialzer,UserProfileSerializer,UserProfile,UserEducationSerializer,UserExperienceSerializer,UserAdditionalInfoSerializer,UserSkillsSerializer,UserEduUpdateSerializer,UserExUpdateSerializer,UserSkillUpdateSerializer,UserAddInfoUpdateSerializer,UserEduDeleteSerializer

from account.models import UserAdditionalInfo,UserExperience,Eductaion,UserProfile,UserSkills
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request, fromat=None):
        serialzer = UserRegistrationSerializer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            user = serialzer.save()
            return Response({'msg':'registration succesful'}, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, fromat=None):
        serialzer = UserLoginSerialzer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            email = serialzer.data.get('email')
            password = serialzer.data.get('password')
            user = authenticate (email=email, password=password )
            if user is not None:
                return Response({'msg':'login succesful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_error':['email or password is not valid']}}, status=status.HTTP_200_OK)


class UserEducation(APIView):
    def post(self,request):
        serializer = UserEducationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({'msg':'education details save succesful'}, status=status.HTTP_201_CREATED)

class UserExperienceView(APIView):
    def post(self,request):
        serializer = UserExperienceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({'msg':'Experience details save succesful'}, status=status.HTTP_201_CREATED)

class UserAdditionalInfos(APIView):
    def post(self,request):
        serializer = UserAdditionalInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({'msg':'Additional Information save succesful'}, status=status.HTTP_201_CREATED)
        

class UserSkill(APIView):
    def post(self,request):
        serializer = UserSkillsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({'msg':'Additional Information save succesful'}, status=status.HTTP_201_CREATED)


class UserProfileView(APIView):
    Permission_classes = [IsAuthenticated]
    def get(self,request, id):
        user=request.user.id
    
        data=UserProfile.objects.filter(user_id=id)
        serializer=UserProfileSerializer(data,many=True)

        Pi=UserAdditionalInfo.objects.filter(user_id=id)
        serializer1=UserAdditionalInfoSerializer(Pi,many=True)

        Sk = UserSkills.objects.filter(user_id=id)
        serializer2 = UserSkillsSerializer(Sk,many=True)

        Ex = UserExperience.objects.filter(user  =id)
        serializer3 = UserExperienceSerializer(Ex, many = True)

        Ed = Eductaion.objects.filter(user=id)
        serializer4 = UserEducationSerializer(Ed, many=True)

        return Response({'Profile':serializer.data,'AdditionalInformation':serializer1.data,'Experience':serializer3.data,'Education':serializer4.data,"Skill":serializer2.data})



class UserEduUpdate(APIView):
    def put(self,request):
        serializer = UserEduUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({'msg':'Education Update succesful'}, status=status.HTTP_201_CREATED)


class UserExUpdate(APIView):
    def put(self,request):
        serializer = UserExUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({'msg':'Experience Update succesful'}, status=status.HTTP_201_CREATED)


class UserSkillUpdate(APIView):
    def put(self,request):
        serializer = UserSkillUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({'msg':'skills Update succesful'}, status=status.HTTP_201_CREATED)



class AddInfoUpdate(APIView):
    def put(self,request):
        serializer = UserAddInfoUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({'msg':'Additional Info Update succesful'}, status=status.HTTP_201_CREATED)


class UserEduDelete(APIView):
    def put(self,request):
        serializer = UserEduDeleteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        return Response({'msg':'Education Delete  succesful'}, status=status.HTTP_201_CREATED)