from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response

# Create your views here.
from .models import CarModel
from .serializer import CarSerializer


class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        qs = self.queryset.all()
        auto_park_id = self.request.query_params.get('auto_park_id')
        if auto_park_id:
            qs.filter(auto_parks_id=auto_park_id)
        return super().get_queryset()

class GetAll(APIView):

    def get(self, *args,**kwargs):
        car = CarModel.objects.all()
        serializer = CarSerializer(car,many=True)
        return Response()

class CarUpdateReadDeleteByIdView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    #
    # def get(self, *args, **kwargs):
    #     return super().get(self.request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

