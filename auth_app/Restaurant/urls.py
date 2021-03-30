from django.urls import path
from .views.get_and_post import GetAndPost, GetCodeByUserId

urlpatterns = [
    path('', GetAndPost.as_view(), name="get_and_post"),
    path('code/<int:id>/', GetCodeByUserId.as_view(), name="get_code_by_user_id"),
]
