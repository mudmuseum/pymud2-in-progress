import time

class Game:

  world = None
  socketserver = None
  running = False
  name = ""

  def __init__(self):
    self.running = True

  def __del__(self):
    pass

  def loop(self):
    while(self.running):
      time.sleep(5)
      print('5 seconds have elapsed...')
