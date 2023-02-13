from django.urls import path , include
from applications.post.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router. register('comments', CommentViewSet, basename='comment')
router.register('comment', CommentModelViewset)

urlpatterns = [
    # path('', PostListAPIView.as_view()),
    # path('create/', PostCreateAPIview.as_view()),
    # path('update/<int:pk>/', PostUpdateAPIview.as_view()),
    # path('delete/<int:pk>/', PostDeleteAPIview.as_view()),
    # path('detail/<int:id>/', PostDetailAPIview.as_view()),

    path('', PostListCreateAPIView.as_view()),
    path('<int:pk>/', PostDetailDeleteUpdateAPIView.as_view()),
    path('add/image/', CreateImageAPIView.as_view()),
    # path('comments/', CommentViewSet.as_view({'get':'list'})),
    path('', include(router.urls)),
    
]