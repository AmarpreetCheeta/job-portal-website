from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserBaseManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have there email.')
        if not username:
            raise ValueError('User must have there username.')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


STATE_TYPES = (
    ('Maharashtra','Maharashtra'),('Delhi','Delhi'),('Kerla','Kerla'),('Chennai','Chennai'),
    ('Karnataka','Karnataka'),('Tamil Nadu','Tamil Nadu'),('Hydrabad','Hydrabad'),
    ('Madhya Pradesh','Madhya Pradesh'),('Uttar Pradesh','Uttar Pradesh'),('Himachal','Himachal'),
    ('Punjab','Punjab'),('Hariyana','Hariyana'),('Rajesthan','Rajesthan'),('Gujrat','Gujrat'),
    ('Sikkim','Sikkim'),('Oddisha','Oddisha'),('Telangana','Telangana'),('Uttrakhand','Uttrakhand'),
)

GENDER_TYPE = (
    ('Male','Male'),('Female','Female'),('Others','Others'),
)

class UserAccount(AbstractBaseUser):
    image = models.ImageField(verbose_name='Image',upload_to='profile_image/%y')
    first_name = models.CharField(verbose_name='Full Name',max_length=2000)
    username = models.CharField(verbose_name='Username',unique=True,max_length=2000)
    email = models.EmailField(verbose_name='Email',unique=True)
    phone = models.CharField(verbose_name='Phone Number',unique=True,max_length=13)
    state = models.CharField(verbose_name='State',max_length=20,choices=STATE_TYPES)
    gender = models.CharField(verbose_name='Gender',max_length=20,choices=GENDER_TYPE)
    date_joined = models.DateTimeField(verbose_name='Date Joined',auto_now=True)
    last_login = models.DateTimeField(verbose_name='Last Login',auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserBaseManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perms):
        return self.is_admin
    
    def has_module_perms(self, label_app):
        return True
    
    

CITY_TYPES = (
    ('Mumbai','Mumbai'),('Navi Mumbai','Navi Mumbai'),('Pune','Pune'),('Nashik','Nashik'),('Thane','Thane'),
    ('Ratnagiri','Ratnagiri'),('Aurangabad','Aurangabad'),('Gurgaon','Gurgaon'),('Agra','Agra'),
    ('Faridabad','Faridabad'),
)

COUNTRIES = (
    ('American','American'),('Indian','Indian'),('Pakistani','Pakistani'),('Iranian','Iranian'),('Russian','Russian'),
    ('Australian','Australian'),('African','African'),('British','British'),('Mexican','Mexican')
)

    
class ResumeSubmitModel(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    full_name = models.CharField(verbose_name='Full Name',max_length=2000)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone Number',max_length=13)
    location = models.CharField(verbose_name='Location',max_length=2000)
    linked_in = models.URLField(verbose_name='Linked In', max_length=5000)
    education = models.TextField(verbose_name='Education')
    higher_education = models.TextField(verbose_name='Higher Education')
    skills = models.TextField(verbose_name='Skills')
    project = models.TextField(verbose_name='Projects')
    birth_date = models.DateField(verbose_name='Birth Date')
    nationality = models.CharField(verbose_name='Nationality',choices=COUNTRIES, max_length=100)
    hobbies = models.TextField(verbose_name='Hobbies')
    address = models.TextField(verbose_name='Address')
    objectives = models.TextField(verbose_name='Objectives')
    declaration = models.TextField(verbose_name='Declaration')
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.full_name)
    
    
class CompanyModel(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    company_name = models.CharField(verbose_name='Company Name',max_length=2000)
    industry_type = models.CharField(verbose_name='Industry Type',max_length=2000)
    headquarter = models.TextField(verbose_name='Headquarter')
    city = models.CharField(verbose_name='City',max_length=40, choices=CITY_TYPES)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone',max_length=15)
    start_date = models.DateField(verbose_name='Start Date')
    logo = models.ImageField(verbose_name='Company Logo',upload_to='company_logo/%y')
    discription = models.TextField(verbose_name='Discription')
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.company_name)
    
    

JOB_TYPES = (
    ('Internship','Internship'),('Full Time','Full Time'),('Part Time','Part Time'),
    ('Temporary','Temporary'),
)

class SubmitJobsModel(models.Model):    
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    job_title = models.CharField(verbose_name='Job Title',max_length=2000)
    location = models.CharField(verbose_name='Location',max_length=2000)
    email = models.EmailField(verbose_name='Email')
    company_name = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='company')
    salary = models.IntegerField(verbose_name='Salary')
    job_type = models.CharField(verbose_name='Job Type',max_length=15, choices=JOB_TYPES)
    skills = models.TextField(verbose_name='Skills')
    discription = models.TextField(verbose_name='Discription')
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.job_title)
    
    

class ContactModel(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Enter your full name',max_length=2000)
    email = models.EmailField(verbose_name='Enter your email')
    message = models.TextField(verbose_name='Message')
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name) + " " + str(self.email)
    
    

class ApplyModel(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='Users')
    apply = models.ForeignKey(SubmitJobsModel, on_delete=models.CASCADE)
    applyers = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='Applyers')
    
    def __str__(self):
        return str(self.user)
    
    
class FollowCompanyModel(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    following = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)
    
    

class JobsSavedModel(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='user_name')
    jobs = models.ForeignKey(SubmitJobsModel, on_delete=models.CASCADE, related_name='jobs_name')
    
    def __str__(self):
        return str(self.user)