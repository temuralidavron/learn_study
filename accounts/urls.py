from django.urls import path

from accounts.views import user

urlpatterns = [
    path('dashboard/', user.dashboard,name="dashboard"),
    path('', user.create_user,name="register"),
    path('login/', user.login_view,name="login"),
    path('logout/', user.logout_view,name="logout"),
]
