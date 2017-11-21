from pony.orm import *
from Model import MusiclyDB


class Person(MusicDB):
    name = Required(str)
    age = Required(int)
