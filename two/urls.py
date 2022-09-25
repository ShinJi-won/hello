from django.urls import path
from . import views

urlpatterns=[
    path('list/',views.list, name='list'),
    path('make/',views.make, name='food-make'),
    path('update/',views.update,name='food-update'),
    path('food/<int:id>/',views.detail,name='food-detail'),
    path('food/<int:id>/delete/',views.delete,name='food-delete'),
    path('food/<int:food_id>/review/make',views.review_make,
         name='review-make'),
    path('food/<int:food_id>/review/delete/<int:review_id>',
         views.review_delete, name='review-delete'),
    path('review/list/',views.review_list, name='review-list'),
]
