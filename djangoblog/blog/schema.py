import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphql_jwt.decorators import login_required
from .models import Post, Category
from .mutations import CreatePostMutation, UpdatePostMutation, DeletePostMutation, CreateCategoryMutation, UpdateCategoryMutation, DeleteCategoryMutation
from .types import PostType, CategoryType

class Query(object):
    all_posts = graphene.List(PostType)
    all_categories = graphene.List(CategoryType)
    post = graphene.Field(PostType, id=graphene.Int())
    category = graphene.Field(CategoryType, id=graphene.Int())

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')
        return Post.objects.get(pk = id)

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        return Category.objects.get(pk = id)

class Mutation(object):
    create_post = CreatePostMutation.Field()
    update_post = UpdatePostMutation.Field()
    delete_post = DeletePostMutation.Field()

    create_category = CreateCategoryMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()