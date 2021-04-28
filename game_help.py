import json

from helper import Helper

class GameHelp:

  helpfiles = None

  def __init__(self):
    self.load_help()

  def __del__(self):
    self.save_help()

  def load_help(self):
    if (Helper.file_exists('./help/helpfiles.json')):
      with open('./help/helpfiles.json', 'r') as helpfiles:
        self.helpfiles = json.load(helpfiles, strict = False)

  def reload_help(self):
    self.helpfiles = None
    self.load_help()

  def save_help(self):
    with open('./help/helpfiles.json', 'r') as helpfiles:
      json.dump(self.helpfiles, helpfiles)

  def lookup(self, keyword):
    if (keyword in self.helpfiles.keys()):
      return self.helpfiles[keyword]
    else:
      return 'Helpfile not found.'
