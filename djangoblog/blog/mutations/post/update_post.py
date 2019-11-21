import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from ...models import Post
from ...types import PostType

class UpdatePostMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        slug = graphene.String()
        body = graphene.String()

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        post = Post.objects.get(pk=kwargs['id'])
        post.title = kwargs['title']
        post.slug = kwargs['slug']
        post.body = kwargs['body']
        post.save()
        return UpdatePostMutation(post=post)