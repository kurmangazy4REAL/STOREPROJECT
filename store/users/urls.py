from django.urls import path

from users import views as user_views

app_name = 'users'

urlpatterns = [
    path('login/', user_views.login_view, name='login'),
    path('register/', user_views.register_view, name='register'),
    path('profile/', user_views.profile_view, name='profile'),
    path('logout/', user_views.logout_view, name='logout'),
]