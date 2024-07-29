#!/bin/bash
class Playlist: 
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def __setitem__(self, index, cancion):
        
        if index == len(self.canciones):
            self.canciones.append(cancion)
        elif 0 <= index < len(self.songs):
            self.canciones[index] = cancion
        else:
            raise IndexError("Índice fuera de rango")

    def __getitem__(self, index):
        return self.canciones[index]
    
    def __len__(self):
      return len(self.canciones) 
    
playlist1 = Playlist("Playlist1")
#
print(len(playlist1))

playlist1[0] = "Cancion 1"
playlist1[1] = "Cancion 2"
playlist1[2] = "Cancion 3"
# 

print(playlist1[0])
print(playlist1[2])
print(playlist1[1])
print(len(playlist1))