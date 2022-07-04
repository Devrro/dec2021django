from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import CarModel
from .serializer import CarSerializer

# Create your views here.


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user.id)
        qs = self.queryset.all()
        auto_park_id = self.request.query_params.get('autoParkId')
        if auto_park_id:
            qs = qs.filter(auto_parks_id=auto_park_id)
            print(qs.query)
        return qs


# class GetAll(APIView):
#
#     def get(self, *args,**kwargs):
#         car = CarModel.objects.all()
#         serializer = CarSerializer(car,many=True)
#         return Response(serializer.data)


class CarUpdateReadDeleteByIdView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        qs = self.queryset.all()
        auto_park_id = self.request.query_params.get('auto_park_id')
        if auto_park_id:
            qs.filter(auto_parks_id=auto_park_id)
        return qs
