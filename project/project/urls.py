"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg',views.registration),
    path('log',views.Login),
    path('home',views.studenthome),
    path('edit/<int:id>',views.edit,name='edit'),
    path('register',views.register2),
    path('complaints',views.complaints),
    path('view',views.viewcomplaints),
    path('log2',views.teacherlogin),
    path('home2',views.teacherhome),
    path('teacherview',views.teacherview),
    path('reply',views.reply),
    path('viewreply',views.viewreply),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)