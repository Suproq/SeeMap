import pygame
import requests
import sys
import os
import datetime
from mapapi import show_map

def get_address_coords(address):
    geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode="+address+"&format=json"
    response = requests.get(geocoder_request)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    return toponym_coodrinates

def main():
    time = datetime.datetime.now()
    print("Здравствуйте! Как к вам обращаться?")
    name = input()
    if time.hour < 4:
        hi = "Доброй ночи,"
    elif time.hour < 10:
        hi = "С добрый утром,"
    elif time.hour < 17:
        hi = "Доброго дня,"
    elif time.hour < 23:
        hi = "Добрый вечер,"
    else:
        hi = "Доброй ночи,"
    print(hi, name)
    print("Это консольное приложение, способное отобразить часть карты мира. Вы можете посмотреть абсолютно любое "
          "место мира, введя лишь несколько команд.")
    while(1):
        print("Пожалуйста, введите адресс:")
        address = input()
        print("Теперь введите размер карты в километрах(Например, диаметр МКАДа равен 35 км, чтобы увидеть всю Москву, "
              "нужно ввести 35")
        r = int(input())
        print("Вы хотели бы увидеть фото со спутника(1), или карту(2)?")
        type = input()
        print("Подождите, карта подготавливается...")
        coords = get_address_coords(address)
        for i in range(len(coords)):
            if coords[i] == " ":
                coords2 = coords[:i] + "," + coords[i + 1:]
        r2 = r*0.005714285
        per = "ll=" + coords2 + "&spn=" + str(r2) + "," + str(r2)
        print("Готово! Теперь вы можете рассмотреть карту, чтобы продолжить просто закройте данное окно")
        if(type == "спутник" or type == "1"):
            type = "sat"
        else:
            type = "map"
        show_map(per, type)

if __name__ == "__main__":
    main()