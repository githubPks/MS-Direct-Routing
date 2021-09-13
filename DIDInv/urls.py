from django.urls import path
from DIDInv import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.register,name='register'),
    path('welcome/',views.welcome,name='welcome'),
    path('regrequest/',views.UserRequestRegistration,name='registration-request'),
    path('did_numbers/',views.did_numbers,name='did-numbers'),
    path('did-prov/',views.didProvison,name='did-prov'),
    path('final/',views.finalview,name='final-view'),
    path('did_allocation/',views.did_allocationview,name='did-allocation')

]