import os
import json
from django.shortcuts import render

from .models import User

# Create your views here.

names = ['Max', 'Olya', 'Igor']
db_path = os.path.join('users', 'db.json')


def home(request):
    print(db_path)
    return render(request, 'users/home.html', {'names': names})


def users(request):
    file = open(db_path, 'r')
    data = json.load(file)
    file.close()
    print(data)
    return render(request, 'users/users.html')

    # второй способ:
    # with open(db_path, 'r') as file:
    #     users_list = [User(**item) for item in json.load(file)]
    # return render(request, 'users/users.html', {'users': users_list})


# один из способов получения информации с урлы
# def create_user(request, id, name, age):
#     print(id)
#     print(name)
#     print(age)
#
#     return render(request, 'users/users.html')

# второй способ получения информации с урлы
# def create_user(request, **kwargs):
#     with open(db_path, 'w') as file:
#         json.dump(kwargs, file)
#     with open(db_path, 'r') as file:
#         user = User(**json.load(file))
#     return render(request, 'users/users.html', {'user': user})

# если вдруг нету файла с юзерами чтобы отловить ошибку:
def users(request):
    users_list = []
    try:
        with open(db_path, 'r') as file:
            users_list = [User(**item ) for item in json.load(file)]
    except FileNotFoundError as err:
        print(err)
    finally:
        print('Finisch')
    return render(request, 'users/users.html', {'user': users_list})

