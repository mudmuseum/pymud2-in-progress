import threading
import socketserver
import g
from helper import Helper
from player import Player

class SockServHandler(socketserver.BaseRequestHandler,):

  def handle(self):
    player = None
    while(not player):
      player = Helper.login(self)
    player['conn'] = self
    g.game.plist.append(player)
    self.request.send(Player.get_prompt(player).encode())

    while(True):
      command = self.request.recv(1024).decode('utf-8')[0:-2]
      if (command in Commands.command_list):
        (player, response, success) = getattr(Commands, command)(player)
      # response = g.game.name + ' | You typed: "' + data + '"'
      # self.request.send(response.encode() + b'\n\r')
      # self.request.send(Player.get_prompt(player).encode())

class ThreadedSockServer(socketserver.ThreadingMixIn, socketserver.TCPServer,):
  pass

