import threading
import g

from game      import Game
from sockserv  import ThreadedSockServer
from sockserv  import SockServHandler
from commands  import Commands
from player    import Player
from world     import World
from game_help import GameHelp
from helper    import Helper

if (__name__ == '__main__'):
  print("Loading game...")
  game = Game()
  g.game = game
  game.name = "New Game"
  print("Game loaded, loading help...")
  game.help = GameHelp()
  print("Help loaded, loading world...")
  game.world = World()
  print("World loaded, loading zones...")
  game.world.load_zones()
  print("Zones loaded, setting up socket server...")
  game.address = ('localhost', 9000)
  game.server = ThreadedSockServer(game.address, SockServHandler)
  (game.ip, game.port) = game.server.server_address
  game.thread = threading.Thread(target=game.server.serve_forever)
  game.thread.setDaemon(True)
  game.thread.start()
  print('Socket Server setup, running in thread ' + game.thread.getName())
  print('Game is ready to rock on ' + game.ip + ':' + str(game.port))
  game.loop()
