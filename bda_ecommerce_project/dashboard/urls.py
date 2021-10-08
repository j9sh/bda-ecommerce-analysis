#  here we’ll store URL routes for our application
from django.urls import path
from . import views

# path(url, view_name)
urlpatterns = [
    path('', views.homepage, name='home'),
    path('report/retail', views.ecommerce_report_page, name='retail_report'),
    path('report/marketing', views.marketing_report_page, name='marketing_report'),
]
