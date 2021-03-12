from django.urls import path
from . import views
urlpatterns=[
    path('',views.StudentViewList.as_view(),name='home'),
    path('create/',views.StudentViewCreate.as_view()),
    path('delete/<int:pk>/',views.StudentViewDelete.as_view(),name='delete'),
    path('update/<int:pk>/',views.StudentViewUpdate.as_view(),name='update'),
    path('<int:pk>/',views.StudentViewDetail.as_view(),name='detail'),
]