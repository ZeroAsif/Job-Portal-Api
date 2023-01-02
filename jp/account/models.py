from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# manager base user.
class UserManager(BaseUserManager):
    def create_user(self, email, name, gender, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
           name=name,
           gender=gender,
           tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, gender,tc, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            gender=gender,
            tc=tc
        
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



# abstract base user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='static/',default='static/user.png')
    back_image=models.ImageField(upload_to='static/',default='static/user.png')
    
    def __str__(self):
        return f'{self.id} {self.user} Profile'


class Eductaion(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    percentage = models.IntegerField()

    def __str__(self):
        return f'{self.user}'

class UserExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    year_of_experience = models.IntegerField()
    current_ctc = models.IntegerField()

    def __str__(self):
        return f'{self.user}'


class UserAdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CHOICES = (
        ("M" , "Male"),
        ("F" , "Female"),
        ("O" , "Others"),
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=200, choices=CHOICES)
    DOB = models.DateField()
    current_location = models.CharField(max_length=200)
    langauges = models.CharField(max_length=255)


class UserSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.TextField(max_length=300)












# signal for profile update
@receiver(post_save, sender=User)
def created_profile(sender,instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(created_profile, sender=User)