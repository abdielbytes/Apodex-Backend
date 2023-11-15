from django.urls import path
from user_app.views import RegisterView,UserLoginView,UpdateProfileView,UserLogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),
]