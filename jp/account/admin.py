from django.contrib import admin
from account.models import User,UserProfile,Eductaion,UserExperience,UserAdditionalInfo,UserSkills
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('email','id', 'name', 'tc','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','tc')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name','tc', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()
# UserProfileAdmin
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('id','user')

class UserEductaionAdmin(admin.ModelAdmin):
    list_display = ('institute','course','start_date', 'end_date', 'percetage')


class UserExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name','location','year_of_experience', 'current_ctc')


class UserAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('name','age','gender', 'DOB', 'current_location','langauges')



class UserSkillsAdmin(admin.ModelAdmin):
    list_display = ('skills')



# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Eductaion, )
admin.site.register(UserExperience, )
admin.site.register(UserAdditionalInfo, UserAdditionalInfoAdmin)
admin.site.register(UserSkills, )

