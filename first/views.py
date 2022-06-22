import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class FirstOne(APIView):
    def get(self, *args, **kwargs):
        return Response('Method GET')

    def post(self, *args, **kwargs):
        return Response('Method POST')

    def put(self, *args, **kwargs):
        return Response('Method PUT')

    def delete(self, *args, **kwargs):
        return Response('Method DELETE')

    def patch(self, *args, **kwargs):
        return Response('Method PATCH')


class SecondOne(APIView):
    def get(self, *args, **kwargs):
        data = self.request.data
        res = self.request.query_params.dict()
        print(data)
        return Response(res)

    def post(self, *args, **kwargs):
        return Response('Method POST')

    def put(self, *args, **kwargs):
        return Response('Method PUT')

    def delete(self, *args, **kwargs):
        return Response('Method DELETE')

    def patch(self, *args, **kwargs):
        return Response('Method PATCH')


class UsersListCreateView(APIView):
    def get(self, *args, **kwargs):
        user_storage: list[{}, ...] = []
        with open('././src/storage.json', 'r+') as userStorage:
            user_storage = json.load(userStorage)
            userStorage.close()
        user_id = 0
        if 'user_id' in kwargs.keys():
            user_id = kwargs['user_id']
            return Response(filter(lambda x: x['user_id'] == user_id, user_storage))

        return Response(user_storage)

    def post(self, *args, **kwargs):
        data = self.request.data
        user_storage: list[{}, ...] = []
        with open('././src/storage.json', 'r') as userStorage:
            user_storage = json.load(userStorage)
        with open('././src/storage.json', 'w') as userStorage:
            user_storage.append(data)
            print(user_storage)
            userStorage.write(json.dumps(user_storage))
        return Response('Created')

    def patch(self, *args, **kwargs):

        saved_user = self.request.data
        user_storage: list[{}, ...] = []
        with open('././src/storage.json', 'r') as userStorage:
            user_storage = json.load(userStorage)
        if kwargs:
            for i in user_storage:
                if int(i['user_id']) == int(kwargs['user_id']):
                    try:
                        i['name'] = (saved_user['name'])
                    except Exception as err:
                        return Response(err)
        with open('././src/storage.json', 'w') as userStorage:
            userStorage.write(json.dumps(user_storage))
        return Response('Patched')

    def delete(self, *args, **kwargs):
        if 'user_id' in kwargs.keys():
            user_storage: list[{}, ...] = []
            with open('././src/storage.json', 'r') as userStorage:
                user_storage = json.load(userStorage)
                userStorage.close()
            user_storage = list(filter(lambda x: x['user_id'] != kwargs['user_id'], user_storage))
            with open('././src/storage.json', 'w') as userStorage:
                userStorage.write(json.dumps(user_storage))
            return Response('Successful deleted')
        else:
            return Response('Cant delete user')
