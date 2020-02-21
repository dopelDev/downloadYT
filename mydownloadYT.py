#!/usr/bin/env python3
"""
script YTdownload
"""
import os
import pickle
from pytube import YouTube
from methods import *


# Aqui comienza
print("inicio correctamente")
objTube = genYtobj()

if objTube is False:
    print("No es un objeto")
else:
    itagSelector(objTube)

# Aqui termina
print("\n\n------------------\n\n")
print("Termino ...")
