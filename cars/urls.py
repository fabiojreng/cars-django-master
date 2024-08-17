from django.urls import path
from cars.views import (
    CarDeleteView,
    CarDetailView,
    CarUpdateView,
    CarsListView,
    NewCarView,
)


urlpatterns = [
    path("cars_list/", CarsListView.as_view(), name="cars_list"),
    path("new_car/", NewCarView.as_view(), name="new_car"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car_update"),
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car_delete"),
]
