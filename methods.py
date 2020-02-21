#!/usr/bin/env python3
"""
script Methods
"""
import os
import pickle
from pytube import YouTube

# funcion de creacion de objTube


def genYtobj():
    url = input("ingresar url\n")
    try:
        objTube = YouTube(url)
        print("Titulo del video\n" + str(type(objTube)))
        print(objTube.title)
    except BaseException as e:
        print(e)
        objTube = False
    return objTube

# method creato a menu


def menu(objTube):

    print("\n1 para video y sonido\n2 para solo video\n3 para solo audios")
    print("\n4 para todos")
    print("\n\n----")
    op = input()
    print("\n\n------------------\n\n")

    if(int(op) == 1):
        print("entro a # video y audio")
        listStream = objTube.streams.filter(progressive=True).all()
        return listStream
    elif(int(op) == 2):
        print("entro a # solo video")
        listStream = objTube.streams.filter(only_video=True).all()
        return listStream
    elif(int(op) == 3):
        print("entro a # solo audio")
        listStream = objTube.streams.filter(only_audio=True).all()
        return listStream
    elif(int(op) == 4):
        print("entro a # TODO: ")
        listStream = objTube.streams.all()
        return listStream
    else:
        return "FUCK YOU"


def itagSelector(objTube):

    while (True):
        listStream = menu(objTube)
        showList(listStream)
        print("\n\nPara agrear itag 1\nPara regresar a menu ingrese 2")
        print("\nPara salir 3")
        op = int(input("\n : "))

        if(op == 1):
            print("ingresar el numero de itag\n\n-----------------\n")
            itag = input()
            fileTO = objTube.streams.get_by_itag(itag)
            print("\n\nEl itag ingresado es "+itag)
            print("\n\npara confirmar 1\nPara regresar a menu 2")
            print("\nPara salir y cerrar 3")

            subOp = int(input())
            if(subOp == 1):
                raiz = os.getcwd()
                print(raiz)
                print("descargar seleccionado\n" + raiz)
                if not os.path.exists(raiz + '/youDescarga'):
                    os.mkdir(raiz + '/youDescarga')
                print("Descargando ...\n")
                fileTO.download(raiz + '/youDescarga')
                print("\n\nEl titulo del archivo es :  "+objTube.title)
                op = 3
                break

            elif(subOp == 2):
                continue
            elif(subOp == 3):
                op = 3
                break

        elif(op == 2):
            continue
        elif(op == 3):
            break


def showList(listStream):
    print("\n\n------------------\n\n")
    for inter in listStream:
        print(inter)
