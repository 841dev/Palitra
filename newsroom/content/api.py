from ninja import NinjaAPI
from ninja.pagination import paginate, PageNumberPagination
from ninja.responses import Response
from typing import List, Optional
from .models import Article, Category, Tags
from .schemas import (ArticleSchema,
                      CategorySchema,
                      TagsSchema,
                      ArticleNotFoundSchema,
                      CategoryNotFoundSchema,
                      TagNotFoundSchema)


api = NinjaAPI()

@api.get("/articles/", response=List[ArticleSchema])
@paginate(PageNumberPagination)
def articles(request):
    return Article.objects.all()


@api.get("/articles/id/{article_id}", response={200 : ArticleSchema, 404 : ArticleNotFoundSchema})
def article(request, article_id: int):
    try:
        article = Article.objects.get(pk=article_id)
        return 200, article
    except Article.DoesNotExist:
        return 404, {'message' : 'Article not found'}

@api.get("/articles/category/{category}", response={200 : ArticleSchema, 404 : ArticleNotFoundSchema})
def article(request, category: str):
    try:
        article = Article.objects.get(category=category)
        return 200, article
    except Article.DoesNotExist:
        return 404, {'message' : 'Article not found'}




@api.get("/articles/tags/{tags}", response={200 : ArticleSchema, 404 : ArticleNotFoundSchema})
def article(request, tags: int):
    try:
        article = Article.objects.get(tags=tags)
        return 200, article
    except Article.DoesNotExist:
        return 404, {'message' : 'Article not found'}


@api.get("/category/", response=List[CategorySchema])
@paginate(PageNumberPagination)
def category(request):
    return Category.objects.all()

@api.get("/category/{category_id}", response={200 : CategorySchema, 404 : CategoryNotFoundSchema})
def category(request, category_id: int):
    try:
        category = Category.objects.get(pk=category_id)
        return 200, category
    except Category.DoesNotExist:
        return 404, {'message' : 'Category not found'}

@api.get("/tags/", response=List[TagsSchema])
@paginate(PageNumberPagination)
def tags(request):
    return Tags.objects.all()

@api.get("/tags/{tag_id}", response={200 : TagsSchema, 404 : TagNotFoundSchema})
def tag(request, tag_id: int):
    try:
        tag = Tags.objects.get(pk=tag_id)
        return 200, tag
    except Tags.DoesNotExist:
        return 404, {'message' : 'Tag not found'}