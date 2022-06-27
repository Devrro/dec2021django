from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.pc_shop.models import PcModel

# Create your views here.

from .serializers import PcSerializer


class PcModelView(APIView):
    def get(self, *args, **kwargs):
        pc_set = PcModel.objects.all()
        serializer = PcSerializer(pc_set, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        # instance = PcModel.objects.create(**data)
        serializer = PcSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class PcReadUpdateDestroy(APIView):
    def get(self, *args, **kwargs):
        pc_id = kwargs.get('pk')
        if not PcModel.objects.filter(pk=pc_id).exists():
            return Response('Pc does not exist', status=status.HTTP_204_NO_CONTENT)
        pc_model = PcModel.objects.get(pk=pc_id)
        serializer = PcSerializer(pc_model)
        return Response(serializer.data)

    def put(self, *args, **kwargs):
        data = self.request.data
        pc_id = kwargs.get('pk')
        if not PcModel.objects.filter(pk=pc_id).exists():
            return Response('Pc does not exist')

        pc_model = PcModel.objects.get(pk=pc_id)
        serializer = PcSerializer(pc_model, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, *args, **kwargs):
        data = self.request.data
        pc_id = kwargs.get('pk')
        if not PcModel.objects.filter(pk=pc_id).exists():
            return Response('Pc does not exist')

        pc_model = PcModel.objects.get(pk=pc_id)
        serializer = PcSerializer(pc_model, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pc_id = kwargs.get('pk')
        if not PcModel.objects.filter(pk=pc_id).exists():
            return Response('Pc does not exist')
        pc_model = PcModel.objects.get(pk=pc_id)
        pc_model.delete()
        return Response("SUCC")