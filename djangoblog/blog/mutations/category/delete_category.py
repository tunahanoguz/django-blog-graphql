import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from ...models import Category

class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        category = Category.objects.get(pk=kwargs['id'])
        category.delete()
        return DeleteCategoryMutation(message="Deleted.")