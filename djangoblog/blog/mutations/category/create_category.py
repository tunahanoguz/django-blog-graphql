import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from ...forms import CategoryForm
from ...types import CategoryType

class CreateCategoryMutation(DjangoModelFormMutation):
    category = graphene.Field(CategoryType)
    class Meta:
        form_class = CategoryForm