from django.urls import path
from .views import top_customers

urlpatterns = [
    path('', top_customers, name='top_customers'),
    path('top-customers/', top_customers, name='top_customers')
]