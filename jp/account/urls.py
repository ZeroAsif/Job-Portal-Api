from django.urls import path,include
from account.views import UserRegistrationView,UserLoginView,UserProfileView,UserEducation,UserExperienceView,UserAdditionalInfos,UserSkill,UserEduUpdate,UserExUpdate,UserSkillUpdate,AddInfoUpdate,UserEduDelete

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profil/', UserProfileView.as_view(), name='profil'),
    path('education/', UserEducation.as_view(), name='education'),
    path('experience/', UserExperienceView.as_view(), name='experience'),
    path('info/', UserAdditionalInfos.as_view(), name='info'),
    path('skill/', UserSkill.as_view(), name='skill'),
    path('viewprofile/<int:id>', UserProfileView.as_view(), name='viewprofile'),
    path('eduupdate/', UserEduUpdate.as_view(), name='eduupdate'),
    path('exupdate/', UserExUpdate.as_view(), name='exupdate'),
    path('skillupdate/', UserSkillUpdate.as_view(), name='skillupdate'),
    path('addupdate/', AddInfoUpdate.as_view(), name='addupdate'),
    path('edudelete/', UserEduDelete.as_view(), name='edudelete'),


]
