   
from abc import abstractmethod
from board import Board_Class
import random


class Player:
    def __init__(self,value:str,board:Board_Class):
        self.value=value
        self.board=board
    @abstractmethod
    def move(self):
        pass




