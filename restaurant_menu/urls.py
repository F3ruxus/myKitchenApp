from django.urls import path
from . import views 

# This means that when the viewer visits the root or the homepage, the default page will be the index.html file as indicated by the MenuList. 
# views means the file where MenuList is coming from.
# For JHCP hackers, the job application form uses function based views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    # The as_view is required for class based views, but you don't need it for function based views!
    path('item/', views.MenuItemDetail.as_view(), name="menu_item")
]