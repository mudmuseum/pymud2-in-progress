class Commands:

  command_list = ["quit", "exit", "save", "version", "login", "commands"]

  def __init__(self):
    pass

  @staticmethod
  def exit(game, player):
    # TODO
    print("Closing server.")
    sys.exit(0)

  @staticmethod
  def quit(main, player):
    # TODO
    print("Closing server.")
    sys.exit(0)

  @staticmethod
  def save(main, player):
    # TODO
    print("TODO")

  @staticmethod
  def version(main, player):
    print("This is version 0.1.0")
    return True

  @staticmethod
  def login(main, player):
    # TODO
    print("TODO.")

  @staticmethod
  def commands(main, player):
    print('Commands list: ') 
    for i in Command.command_list:
      print('\t' + i)
    return True
