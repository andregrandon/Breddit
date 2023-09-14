from django.urls import include, path
from django.contrib import admin
from breddit_django import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('posts/', include('bit_posts.urls')),
    path('admin/', admin.site.urls), 
    path('', include('bit_users.urls')),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('privacy/', views.PrivacyPage.as_view(), name='privacy'),

]

urlpatterns += staticfiles_urlpatterns()
