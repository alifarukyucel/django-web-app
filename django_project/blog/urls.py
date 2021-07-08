from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

# Looking for a template with the naming convention:
# <app>/<model>_<viewtype>.html
# So in our case, it was looking for blog/post_list.html
