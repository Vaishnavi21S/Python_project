

# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),                      # /recipes/
    path('list/', views.recipe_list, name='recipe_list'),        # /recipes/list/
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'), # /recipes/1/
]
