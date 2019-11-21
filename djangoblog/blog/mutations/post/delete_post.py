import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from ...models import Post

class DeletePostMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        post = Post.objects.get(pk=kwargs['id'])
        post.delete()
        return DeletePostMutation(message="Deleted.")