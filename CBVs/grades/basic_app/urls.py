from django.urls import path
from basic_app import views

app_name="app"

urlpatterns = [
        path("create/",views.UserFormView.as_view(),name='create'),
        path("login/",views.user_login,name='login'),
        path("logout/",views.user_logout,name='logout'),
        path("list/",views.StudentsListView.as_view(),name='list'),
        path('summary/<int:pk>/',views.StudentsSummaryView.as_view(),name='details'),
        path('update/<int:pk>/',views.UpdateStudentSummary.as_view(),name='update_summary'),
]
