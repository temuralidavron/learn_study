from django.urls import path

from accounts.views import user

urlpatterns = [
    path('register/', user.create_user,name="register"),
    path('login/', user.login_view,name="login"),
    path('logout/', user.logout_view,name="logout"),
]
