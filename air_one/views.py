from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers, models, utils


class CityListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.CitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.City.objects.all()


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CitySerializer
    queryset = models.City.objects.all()


class PlaneListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.PlaneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.Plane.objects.all()


class PlaneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PlaneSerializer
    queryset = models.Plane.objects.all()


class RouteListView(generics.ListAPIView):
    serializer_class = serializers.RouteSerializer
    queryset = models.Route.objects.all()


class RouteDetailDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.RouteSerializer
    queryset = models.Route.objects.all()


@api_view(["POST"])
def find_routes(request):

    print(request.data)

    routeTest = {
        "name": "new Route",
        "travel_times": 180,
        "from_city": 1,
        "to_city": 4,
        "planes": [],
        "id": 22,
    }

    # serializer = serializers.RouteSerializer(routeTest)
    # return Response(serializer.data)
    return Response(routeTest)
    #     form = RouteForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             context = get_routes(request, form)
    #         except ValueError as e:
    #             messages.error(request, e)
    #             return render(request, 'routes/home.html', {'form': form})
    #         return render(request, 'routes/home.html', context)
    #     return render(request, 'routes/home.html', {'form': form})
    # else:
    #     form = RouteForm()
    #     messages.error(request, "No data for search")
    #     return render(request, 'routes/home.html', {'form': form})
