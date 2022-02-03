from django.urls import path
from .views import StatusDetailDeleteUpdateApi, StatusListCreateView
app_name = 'App_Crud'

# status/ --> list, create --> Get,Post
# status/<id>/ --> Details, Update, Delete -> Get, Delete, put/patch


urlpatterns = [
    path('status/', StatusListCreateView.as_view()),
    path('status/<id>/', StatusDetailDeleteUpdateApi.as_view()),

]



