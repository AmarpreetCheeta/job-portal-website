from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import *


class UserAccountAdmin(UserAdmin):
    list_display = ['id','image','first_name','username','email','phone','state','gender','date_joined',
                    'last_login','is_active','is_admin','is_superuser','is_staff']
    search_fields = ['id','first_name','username']
    readonly_fields = ['date_joined','last_login','is_active','is_admin','is_superuser','is_staff']
    
    filter_horizontal = []
    list_filter = []
    fieldsets = []
admin.site.register(UserAccount, UserAccountAdmin)


class Resume_Submit_Admin(admin.ModelAdmin):
    list_display = ['id','user','full_name','email','phone','location','linked_in','education','higher_education',
    'skills','project','birth_date','nationality','hobbies','address','objectives','declaration','date']
admin.site.register(ResumeSubmitModel, Resume_Submit_Admin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','user','company_name','industry_type','headquarter','city','email','phone','start_date',
    'logo','discription','date']
admin.site.register(CompanyModel, CompanyAdmin)


class SubmitJobsAdmin(admin.ModelAdmin):
    list_display = ['id','user','job_title','location','email','company_name','salary','job_type','skills','discription','date']
admin.site.register(SubmitJobsModel, SubmitJobsAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','email','message','date']
admin.site.register(ContactModel, ContactAdmin)



class ApplyAdmin(admin.ModelAdmin):
    list_display = ['id','user','apply','applyers']
admin.site.register(ApplyModel, ApplyAdmin)


class FollowCompanyAdmin(admin.ModelAdmin):
    list_display = ['id','user','following']
admin.site.register(FollowCompanyModel, FollowCompanyAdmin)


class SavedJobsAdmin(admin.ModelAdmin):
    list_display = ['id','user','jobs']
admin.site.register(JobsSavedModel, SavedJobsAdmin)