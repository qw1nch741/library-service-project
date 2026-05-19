from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import CreateUserView, ManageUserView

app_name = "users"


urlpatterns = [
    path("", CreateUserView.as_view(), name="create"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # 3. Token renewal endpoint (To keep the user logged in safely)
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # 4. Profile "Me" endpoint
    path("me/", ManageUserView.as_view(), name="manage"),2
]
