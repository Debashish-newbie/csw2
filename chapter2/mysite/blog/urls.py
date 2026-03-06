from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    # slug converter name must match view parameter 'slug'
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_slug_date_detail, name='post_slug_date_detail'),
    
]