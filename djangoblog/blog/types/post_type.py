from graphene_django.types import DjangoObjectType
from ..models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post