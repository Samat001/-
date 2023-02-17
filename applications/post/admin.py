from django.contrib import admin
from applications.post.models import Post,PostImage , Comment

class ImageAdmin(admin.TabularInline):
    model = PostImage
    fields = ('image',)
    max_num = 4

class PostAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin,)
    
    list_display = ('title', 'owner', 'post_count','post_rating', 'created_at', 'john',)
    list_filter = ('owner','id',)
    search_fields = ('title',)
    # exclude = ('title',)

    def post_count(self,obj):
        return obj.likes.filter(is_like=True).count()


    def post_rating(self,obj):
        return obj.ratings.count()

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
admin.site.register(Comment)