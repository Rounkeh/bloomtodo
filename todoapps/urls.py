from django.urls import path
from . import views
urlpatterns = [
    
    path('create-todo/',views.createRetrieveView.as_view()),
    path('get-all-todo/',views.createRetrieveView.as_view()),
    # path('get-single-todo/<str:id>/',views.getUpdateDeleteview.as_view()),
    # path('update-todo/<str:id>/',views.getUpdateDeleteview.as_view()),
    # path('delete-todo/<str:id>/',views.getUpdateDeleteview.as_view())
]

