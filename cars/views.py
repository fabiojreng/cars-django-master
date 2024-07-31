from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all()
    req = request.GET.get("search")

    if req:
        cars = cars.filter(model__icontains=req)

    return render(request, "cars.html", {"cars": cars})
