from rest_framework import serializers 
from blog.models import Blog, Author, Comments


class AuthorSerializer(serializers.Serializer):    
    class Meta:
        model = Author

class BlogSerializer(serializers.Serializer):
    class Meta:
        model = Blog
        
class CommentsSerializer(serializers.Serializer):
    class Meta:
        model = Comments