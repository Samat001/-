from rest_framework import generics
from applications.post.models import *
from applications.post.serializers import *
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from applications.post.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response



# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostCreateAPIview(generics.CreateAPIView):
#     serializer_class = PostSerializer

# class PostUpdateAPIview(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDeleteAPIview(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailAPIview(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'id'

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['owner', 'title']
    search_fields = ['title']
    ordering_feilds = ['id']
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     filter_owner = self.request.query_params.get('owner')
    #     if filter_owner:
    #         queryset = queryset.filter(owner=filter_owner)
    #     # queryset = queryset.filter(owner=5)
    #     return queryset

class PostDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreateImageAPIView(generics.CreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [IsAuthenticated]

    # stackowerflow

class CommentViewSet(ViewSet):
    def list(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentModelViewset(ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer