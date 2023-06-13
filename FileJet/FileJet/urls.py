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
from SubscriptionApp.views import *


documentation_patterns = [
    path(r'', show_documentation, name='documentation'),
    path(r'accounts',  show_documentation_accounts, name='documentation_account'),
    path(r'confident', show_documentation_confident, name='documentation_confident'),
    path(r'files', show_documentation_files, name='documentation_files'),
]


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'about_us/', show_about_us, name='about_us'),
    path(r'', show_main, name='main'),
    path(r'search/', show_search, name='search'),
    path(r'profile/', show_profile, name='profile'),
    path(r'file/<int:file_pk>', show_file, name='file'),
    path(r'upload_file/', show_upload_file, name='upload_file'),
    path(r'registration/', show_registration, name='registration'),
    path(r'login/', show_login, name='login'),
    path(r'logout/', log_out, name='logout'),
    path(r'documentation/', include(documentation_patterns), name='documentation'),
    path(r'subscription/', show_subscription, name='subscription'),
    path(r'authenticate/', authenticate, name='authenticate'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)