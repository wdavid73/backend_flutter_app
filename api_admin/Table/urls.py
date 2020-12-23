from django.urls import path
from .View.TableGetAndPost import GetAndPost
from .View.list_tables_by_restaurant import list_tables_by_restaurant

urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post"),
    path("tables_by_restaurant/", list_tables_by_restaurant,
         name="tables_by_restaurant")

]
