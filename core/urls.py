
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
] + debug_toolbar_urls()