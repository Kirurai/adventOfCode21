import os.path
from pathlib import Path

class Reader:
    def __init__(self, nombre, path = os.path.dirname(__file__), mode = 'r'):
        self.nombre = os.path.join(path, nombre)
        self.mode = mode

    def __enter__(self):
        self.nombre = open(self.nombre, self.mode, encoding='utf8')
        return  self.nombre

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.nombre:
            self.nombre.close()