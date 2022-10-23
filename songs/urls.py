from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.songs_list),

]


# path('',views.products_list),
# path('<int:pk>/', views.product_detail),
# my API to serve content on the following URLs paths:   Paths must match these exactly!   ‘api/music/'   ‘api/music/<int:pk>/’