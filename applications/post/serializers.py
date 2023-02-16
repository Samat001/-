from rest_framework import serializers
from applications.post.models import *
from applications.feedback.serializers import *
from django.db.models import Avg


class PostImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostImage 
        fields = '__all__'
        # fields = ('id',)
        # exclude = ('post',)





class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.EmailField(required=False)
    likes = LikeSerializer(many=True, read_only=True)
    images = PostImageSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')
    
    # likes_count = serializers.SerializerMethodField()
    # def get_likes_count(self, post):
    #     return Like.objects.filter(post_id=post).count()

    class Meta:
        model = Post 
        fields = '__all__' # ('title',)
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['like_count'] = instance.likes.filter(is_like=True).count()
        # rating_result = 0
        # for rating in instance.ratings.all():
        #     rating_result += rating.rating
        # if rating_result:
        #     representation['rating'] = rating_result / instance.ratings.all().count()
        # else:
        #     representation['rating'] = rating_result    
        representation['rating']= instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return representation





    # def to_representation(self, instance):
    #     # print(instance)
    #     representation = super().to_representation(instance)
    #     # print(representation)
    #     # representation['name'] = 'John'
    #     representation['name'] = instance.owner.email
    #     return representation

    # def create(self, validated_data):
    #     validated_data['owner'] = self.context['request'].user #request.user
    #     print(validated_data)
    #     return super().create(validated_data)


    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        request = self.context.get('request')
        data = request.FILES
        # for i in data.getlist('images'):
        #     PostImage.objects.create(post=post,image=i)
        image_objects = []
        for i in data.getlist('images'):
            image_objects.append(PostImage(post=post,image=i))
        PostImage.objects.bulk_create(image_objects)
        return post

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Comment
        fields = '__all__'



