import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from ...forms import PostForm
from ...types import PostType

class CreatePostMutation(DjangoModelFormMutation):
    post = graphene.Field(PostType)
    class Meta:
        form_class = PostForm