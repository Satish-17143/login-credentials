from django.urls import path
from app1 import views
urlpatterns = [
    path("add/", views.details, name="add_patient"),
    path("patient/<str:Name>/", views.display, name="view_patient"),
    path('all/', views.view_all_patients, name='view_all_patients'),
    path('filter/', views.filter_patients, name='filter_patients'),
    path('patient/update/<int:id>/', views.update_patient, name='update_patient'),
    path('patient/delete/<int:id>/', views.delete_patient, name='delete_patient'),
     path("dis/",views.demo,name="demo"),
    path("log/",views.login,name="login"),
    path("sinup/",views.sinup,name="sinup"),
]