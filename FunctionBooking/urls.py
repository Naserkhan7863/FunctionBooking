"""FunctionBooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mainapp import views as mainviews
from userapp import views as userviews
from adminapp import views as adminviews
from banquetapp import views as banquetviews
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainviews.index,name='index'),
    path('about',mainviews.about,name='about'),
    path('contact',mainviews.contact,name='contact'),
    path('function-halls',mainviews.function_halls,name='function_halls'),
    path('services',mainviews.services,name='services'),


      # Views For Userapp which is defined as userviews


    path('user-login',userviews.user_login,name='user_login'),
    path('user-register',userviews.user_register,name='user_register'),
    path('user-dashboard',userviews.user_dashboard,name='user_dashboard'),
    path('user-functionhall',userviews.user_functionhall,name='user_functionhall'),
    path('user-functionhall-details/<int:id>/',userviews.user_functionhall_details,name='user_functionhall_details'),
    # path('exclude-user-functionhall-details/<int:id>/', userviews.user_order_view, name='exclude_user_functionhall_details'),

    path('user-services',userviews.user_services,name='user_services'),
    path('user-feedback',userviews.user_feedback,name='user_feedback'),

      # Views For adminapp which is defined as adminviews

    path('admin-login',adminviews.admin_login,name='admin_login'),
    path('admin-dashboard',adminviews.admin_dashboard,name='admin_dashboard'),
    path('admin-function-halls',adminviews.admin_function_halls,name='admin_function_halls'),
    path('admin-view-services',adminviews.admin_view_services,name='admin_view_services'),
    path('admin-view-users',adminviews.admin_view_users,name='admin_view_users'),
    path('admin-view-feedbacks',adminviews.admin_view_feedbacks,name='admin_view_feedbacks'),
    path('function-halls-accept/<int:id>/',adminviews.function_halls_accept,name='function_halls_accept'),
    path('function-halls-reject/<int:id>/',adminviews.function_halls_reject,name='function_halls_reject'),
    path('service-partners-accept/<int:id>/',adminviews.service_partners_accept,name='service_partners_accept'),
    path('service-partners-reject/<int:id>/',adminviews.service_partners_reject,name='service_partners_reject'),



      # Views For adminapp which is defined as adminviews
    path('banquet-register',banquetviews.banquet_register,name='banquet_register'),
    path('banquet-login',banquetviews.banquet_login,name='banquet_login'),
    path('banquet-dashboard',banquetviews.banquet_dashboard,name='banquet_dashboard'),
    path('banquet-add-profile',banquetviews.banquet_add_profile,name='banquet_add_profile'),
    path('banquet-add-booking',banquetviews.banquet_add_booking,name='banquet_add_booking'),
    path('banquet-my-booking',banquetviews.banquet_my_bookings,name='banquet_my_bookings'),
    path('banquet-feedbacks',banquetviews.banquet_feedbacks,name='banquet_feedbacks'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)