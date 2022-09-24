from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout', logout_user, name='logout'),
    # path('index/<pk:id>', File_download.as_view(), name='file'),
    path('detail_view/<slug:pk>', Profile.as_view(), name='detail'),
    # path('index/', File_download.as_view())
    path('index/', upload_file)

]