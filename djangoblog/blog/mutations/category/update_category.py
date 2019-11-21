import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from ...models import Category
from ...types import CategoryType

class UpdateCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        slug = graphene.String()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        category = Category.objects.get(pk=kwargs['id'])
        category.name = kwargs['name']
        category.slug = kwargs['slug']
        category.save()
        return UpdateCategoryMutation(category=category)