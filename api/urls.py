from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Book Store API",
      default_version='v1',
      description="Book and Author Create",
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('welcome', views.welcome),

    path('getbooks', views.get_books),
    path('addbook', views.add_book),
    path('updatebook/<int:book_id>', views.update_book),
    path('deletebook/<int:book_id>', views.delete_book),

    path('getauthors', views.get_authors),
    path('addauthor', views.add_author),

    path('docs/', schema_view.with_ui('swagger', 
        cache_timeout=0), name='schema-swagger-ui'),
]

