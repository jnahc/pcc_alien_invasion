import pygame
from pygame.sprite import sprite

class Bullet(Sprite):
  """a class to manage bullets fired from the ship"""

  def __init__(self, ai_game):
    """create a bullet object at the ship's current position."""
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.color = self.settings.bullet_color

    #create a bullet rect at (0, 0) and then set the correct positon
    self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
      self.settings.bullet_height)
    self.rect.midtop = ai_game.ship.rect.midtop

    #store the bullet's position as a decimal value;
    self.y = float(self.rect.y)