from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response

# Create your views here.
from .models import CarModel
from .serializer import CarSerializer


class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    # def get_queryset(self):
    #     pk = self.request.query_params.get('pk')
    #     print(pk)
    #     if id:
    #         return self.queryset.filter(pk=pk)
    #     return super().get_queryset()
    #
    # def get(self, *args, **kwargs):
    #     # car = self.get_object()
    #     # serializer = self.serializer_class(car, many=True)
    #     return super().list(self.request, *args, **kwargs)
    #
    # def post(self, *args, **kwargs):
    #     return super().create(self.request, *args, **kwargs)


class CarUpdateReadDeleteByIdView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    #
    # def get(self, *args, **kwargs):
    #     return super().get(self.request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

