from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # The first three views are now set to use generic views
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/r/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # These views are not set to use generic views
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/category/2/
    path('category/<int:category_id>/', views.cat, name='category'),
    # ex: /polls/categories/
    path('categories/', views.cats, name='categories')
]
