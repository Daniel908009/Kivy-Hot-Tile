from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random

class Tile(Button):
    def __init__(self, caller, idd):
        super(Tile, self).__init__()
        self.caller = caller
        self.id = idd
    def click(self):
        #print(int(self.id))
        # getting the distance between the hot tile and the clicked tile
        position_of_clicked_tile = [0,0]
        for i in range(self.caller.gridSize):
            for j in range(self.caller.gridSize):
                if self.caller.gameGrid[i][j].id == self.id:
                    position_of_clicked_tile = [i,j]
                    break
        distance = abs(self.caller.hotTile[0] - position_of_clicked_tile[0]) + abs(self.caller.hotTile[1] - position_of_clicked_tile[1])
        print(distance)

class MainGrid(BoxLayout):
    def create_game(self):
        self.gameGrid = []
        self.ids.game_grid.clear_widgets()
        self.hotTile = [random.randint(0, self.gridSize-1), random.randint(0, self.gridSize-1)]
        num = 0
        for i in range(self.gridSize):
            self.gameGrid.append([])
            for j in range(self.gridSize):
                tile = Tile(self, num)
                num += 1
                self.gameGrid[i].append(tile)
                self.ids.game_grid.add_widget(tile)
        self.ids.game_grid.cols = self.gridSize

class hot_tileApp(App):
    def build(self):
        return MainGrid()


if __name__ == '__main__':
    hot_tileApp().run()