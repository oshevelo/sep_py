from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('question_l/', views.Question_List.as_view(), name='Question_List'),
    path('question_l_c/', views.Question_List_Create.as_view(), name='Question_List_Create'),
    path('question_c/', views.Question_Create.as_view(), name='Question_Create'),
    path('question_r/<int:pk>/', views.Question_Retrieve.as_view(), name='Question_Retrieve'),
    path('question_rud/<int:question_id>/', views.Question_Detail.as_view(), name='Question_Detail'),

    path('choice_l_c/', views.Choice_List_Create.as_view(), name='Choice_List_Create'),
    path('choice_rud/<int:choice_id>/', views.Choice_Detail.as_view(), name='Choice_Detail'),




]