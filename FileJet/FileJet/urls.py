"""FileFet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

from EnterApp.views import *
from FileApp.views import *
from DocumentationApp.views import *
from SearchApp.views import *
from ProfileApp.views import *
from MainApp.views import *
from AboutUsApp.views import *


documentation_patterns = [
    path('accounts',  show_documentation_accounts, name='documentation_account'),
    path('confident', show_documentation_confident, name='documentation_confident'),
    path('files', show_documentation_files, name='documentation_files'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', show_about_us, name='about_us'),
    path('', show_main, name='main'),
    path('search/', show_search, name='search'),
    path('profile/', show_profile, name='profile'),
    path('file/', show_file, name='file'),
    path('upload_file/', show_upload_file, name='upload_file'),
    path('enter/', show_enter, name='enter'),
    path('documentation/', show_documentation, name='documentation'),
    path('documentation/accounts', show_documentation_accounts, name='documentation_accounts'),
    path('documentation/confident', show_documentation_confident, name='documentation_confident'),
    path('documentation/files', show_documentation_files, name='documentation_files'),

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)