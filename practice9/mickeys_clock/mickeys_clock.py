import pygame
import datetime
l_hand=pygame.image.load("images/c:\Users\Bagdaulet\Pictures\Screenshots\left_hand.png")
r_hand=pygame.image.load("images/c:\Users\Bagdaulet\Pictures\Screenshots\right_hand.png")
mickey=pygame.image.load("images/c:\Users\Bagdaulet\Pictures\Screenshots\mickey.png.png")
center=(300, 300)
def update_angles():
    now=datetime.datetime.now()
    sec=now.second * 6
    minute=now.minute * 6
    return sec, minute
def draw_clock(screen, sec, minute):
    screen.blit(mickey, mickey.get_rect(center=center))
    sec_hand=pygame.transform.rotate(l_hand, -sec)
    screen.blit(sec_hand, sec_hand.get_rect(center=center))
    min_hand=pygame.transform.rotate(r_hand, -minute)
    screen.blit(min_hand, min_hand.get_rect(center=center))