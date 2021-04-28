class Player:

  @staticmethod
  def get_name(player):
    return player['info']['short_name']

  @staticmethod
  def get_prompt(player):
    return player['info']['prompt']
