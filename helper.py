import json

from pathlib import Path

import g

class Helper:

  @staticmethod
  def file_exists(filename):
    ftest = Path(filename)
    if (ftest.is_file()):
      return True
    return False

  @staticmethod
  def login(conn):
    conn.request.send(g.game.help.lookup('greeting').encode())
    player_name = conn.request.recv(1024).decode('utf-8')[0:-2]
    if (len(player_name) >= 3):
      if (Helper.file_exists('players/' + player_name + '.json')):
        conn.request.send(g.game.help.lookup('motd').encode())
        return Helper.load_player(player_name)
      else:
        return None

  @staticmethod
  def load_player(player_name):
    with open('players/' + player_name + '.json') as player_file:
      return json.load(player_file)
    return None

  @staticmethod
  def save_player(player):
    pass
