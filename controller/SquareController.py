from typing import Union
from model.Square import Square
from view.SquareView import SquareView
from model.PropertySquare import PropertySquare

class SquareController:
    def __init__(self, view: SquareView = None, target_square: Union[Square, PropertySquare] = None):
        self.view = view
        self.target_square = target_square

    def set_target_square(self, target_square):
        self.target_square = target_square

    def set_view(self,view):
        self.view = view

    def set_owner(self, player):
        if(self.target_square == None):
            raise RuntimeError('please call set_target_square() first')

        self.target_square.set_owner(player)

    def remove_owner(self):
        if(self.target_square == None):
            raise RuntimeError('please call set_target_square() first')

        self.target_square.remove_owner()

    def render_view(self):
        if(self.target_square == None):
            raise RuntimeError('please call set_target_square() first')
        elif(self.view == None):
            raise RuntimeError('please call set_target_square() first')
            
        self.view.render(self.target_square)

    def render_view_you_are_here(self):
        if(self.target_square == None):
            raise RuntimeError('please call set_target_square() first')
        elif(self.view == None):
            raise RuntimeError('please call set_target_view() first')

        self.view.render_you_are_here(self.target_square)