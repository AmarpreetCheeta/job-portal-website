from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/',views.SignUp,name='signup'),
    path('login/',views.LogIn,name='login'),
    
    path('',views.Index,name='index'),
    
    path('company/',views.Company,name='company'),
    path('company_data/<int:pk>/',views.CompanyData,name='company_data'),
    path('company_data_edit/<int:pk>/',views.CompanyDataEdit,name='company_data_edit'),
    path('company_data_delete/<int:pk>/',views.CompanyDataDelete,name='company_data_delete'),
    
    path('follow_company/<int:pk>/',views.FollowCompany,name='follow_company'),
    
    path('contact/',views.Contact,name='contact'),
    
    path('jobs/',views.Jobs,name='jobs'),
    path('jobs_update/<int:pk>/',views.JobsEdit,name='jobs_update'),
    path('jobs_remove/<int:pk>/',views.RemoveJobs,name='jobs_remove'),
    
    path('resume/',views.Resume,name='resume'),
    path('resume_data/<int:pk>/',views.ResumeData,name='resume_data'),
    path('resume_data_edit/<int:pk>/',views.ResumeDataEdit,name='resume_data_edit'),
    path('delet_resume/<int:pk>/',views.DeleteResume,name='delet_resume'),
    
    path('searchjobs/',views.SearchJobs,name='searchjobs'),
    
    path('jobs_details/<int:pk>/',views.JobsDetails,name='jobs_details'),
    
    path('accounts/',views.Accounts,name='accounts'),
    path('accountsedits/<int:pk>/',views.AccountsEdits,name='accountsedits'),
    
    path('users_account/<int:pk>/',views.UsersAccounts,name='users_account'),
    path('usersapply_del/<int:pk>/',views.DeleteUsersApply,name='usersapply_del'),
    
    path('change_password/',views.Settings,name='settings'),
    
    path('DeleteAccount/<int:pk>/',views.DeleteAccount,name='DeleteAccount'),
    
    path('apply/<int:pk>/',views.ApplyFunc,name='apply'),
    
    path('saved/<int:pk>/',views.JobSavedFunc,name='saved'),
    path('saved_delete/<int:pk>/',views.SavedJobsDelete,name='saved_delete'),
    
    path('jobs_and_company_data/',views.JobsAndCompanyFunc,name='jobs_and_company_data'),
    
    path('logout/',views.LogOut,name='logout'),
    path('forgetpassword/',views.forgetPassword, name="forgetpassword"),
    path('updatepassword/',views.updatePassword, name="updatePassword")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)