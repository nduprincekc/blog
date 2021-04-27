from django.urls import path
from .views import indexView,PostDetailView,CreatePostView,PostEditView,PostDeleteView

urlpatterns = [
	path('',indexView.as_view(),name='home'),
	path('article/<int:pk>/',PostDetailView.as_view(),name = 'post_detail'),
	path('article/new/',CreatePostView.as_view(),name = 'post-new'),
	path('article/edit/<int:pk>/',PostEditView.as_view(),name = 'post_edit'),
	path('article/<int:pk>/remove',PostDeleteView.as_view(),name = 'post_delete'),
	



]