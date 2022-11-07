import os, pathlib
from assets.util.logging import *

class LevelReader():
  def __init__(self, path):
    self.path = path
    self.data = {}
    self.load()
  
  def load(self):
    # Find all the folders in the levels directory
    for i in os.listdir(self.path):
      if pathlib.Path(os.path.join(self.path, i)).is_dir():
        # If it's a directory, load the data.json file and the collision.png and display.png files
        data_file = str(pathlib.Path(self.path, i, "data.json"))
        collision_file = str(pathlib.Path(self.path, i, "collision.png"))
        display_file = str(pathlib.Path(self.path, i, "display.png"))

        self.data[i] = {
          "data": data_file,
          "collision": collision_file,
          "display": display_file
        }
  
  def list_lvls(self):
    return list(self.data.keys())
  
  def get_lvl(self, lvl):
    if lvl in self.data:
      return self.data[lvl]
    else:
      raise FileNotFoundError("The level "+lvl+" does not exist")
  

if __name__ == "__main__":
  level_reader = LevelReader("assets/levels")
  info(str(level_reader.list_lvls()))
  info(str(level_reader.get_lvl("test")))
