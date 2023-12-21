import uuid
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse, FileResponse
from models.structure import User, Main_User, New_Respons
import hashlib
from typing import Union, Annotated

users_router = APIRouter()

#функция создания пороля

def coder_passwd(cod: str):
    result = cod*2


# Примитивная база данных
user_list = [Main_User(name='Makarov', id=15, age=22, password='*********'), Main_User(name="Vasiliev", id=126, age=43, password='*********')]


#для поиска пользователя в списке (по id возвращает человека из баз данных)

def find_user(id: int) -> Union[Main_User, None]:
    for user in user_list:
        if user.id == id:
            return user
    return None

# чтение пользователей
@users_router.get("/api/users", response_model=Union[list[User], None])
def get_users():
    return user_list

# чтение пользователя
@users_router.get("/api/users/{id}", response_model=Union[User, New_Respons])
def get_user(id: int):
    # получаем пользовател по id
    user = find_user(id)
    print(user)
    # если не найден, отправляем сообщение об ошибке
    if user == None:
        return New_Respons(massage="Пользователь не найден")
    # если пользователь найден
    return user

@users_router.post("/api/users", response_model=Union[User, New_Respons])
def create_user(item: Annotated[User, Body(embed=True, decription="Новый пользователь")]):
    user = Main_User(name=item.name, id=item.id, age=item.age, password=coder_passwd(item.name))
    #добавляем объект в список
    user_list.append(user)
    return user

@users_router.put("/api/users", response_model=Union[User, New_Respons])
def edit_person(item: Annotated[User, Body(embed=True, description="Изменяем данные для пользователя по id")]):
    # получаем пользователя по id
    user = find_user(item.id)
    #если не найден
    if user == None:
        return New_Respons(message= "Пользователь не найден")
    # если пользователь найден,изменяем его данные и отправляем обратно клиенту
    user.name = item.name
    user.age = item.age
    return user


@users_router.delete("/api/users/{id}", response_model=Union[list[User], None])
def delete_person(id: int):
    #получаем пользователя по id
    user = find_user(id)

    #если не найден
    if user == None:
        return New_Respons(message= "Пользователь не найден")
    # удаляем пользователя
    user_list.remove(user)
    return user_list