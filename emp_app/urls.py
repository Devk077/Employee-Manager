from django.urls import path
from . import views

app_name = 'emp_app'

urlpatterns = [
    path('', views.index, name='index'),
    path("about/",views.about , name="about"),
    path("contact/",views.contact , name="contact"),
    path("list/", views.EmployeeListView.as_view(), name="list"),
    path("create/", views.EmployeeCreateView.as_view(), name="create"),
    path('list/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_details'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete'),

    # path('profile/',views.profile , name="profile"),

]
