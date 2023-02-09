from django.urls import path
from applications.post.views import *


urlpatterns = [
    # path('', PostListAPIView.as_view()),
    # path('create/', PostCreateAPIview.as_view()),
    # path('update/<int:pk>/', PostUpdateAPIview.as_view()),
    # path('delete/<int:pk>/', PostDeleteAPIview.as_view()),
    # path('detail/<int:id>/', PostDetailAPIview.as_view()),

    path('', PostListCreateAPIView.as_view()),
    path('<int:pk>/', PostDetailDeleteUpdateAPIView.as_view())
]