from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CarModel
from .serializer import CarSerializer

# Create your views here.
from permissions.user_permissions import IsSuperUser

class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.car_car_by_price_filter(0)
    # permission_classes = (IsSuperUser,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user.id
        qs = self.queryset.all()
        auto_park_id = self.request.query_params.get('autoParkId')
        if auto_park_id:
            qs = qs.filter(auto_parks_id=auto_park_id)
        qs = qs.filter(user=user)
        print(qs.query)
        return qs

    def post(self, request, *args, **kwargs):
        user = self.request.user
        data = self.request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data)


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
