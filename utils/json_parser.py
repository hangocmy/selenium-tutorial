import json
import os

class JsonParser:
  def __init__(self, json_path):
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    DATA_FILES_PATH = os.path.join(ROOT_DIR, "data")
    self.json_path = os.path.join(DATA_FILES_PATH, json_path)
  
  def read_from_json(self): 
    # read from file
    with open(self.json_path, 'r') as json_file:
      json_reader = json.load(json_file)
    return json_reader
