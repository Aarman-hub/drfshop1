from django.urls import path
from .views import CategoryView, ProductView


urlpatterns = [ 
    path('categories/', CategoryView.as_view(), name="categories"),
    path('products/', ProductView.as_view(), name="products"),
]