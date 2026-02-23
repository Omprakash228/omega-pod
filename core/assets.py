import pygame
from .constants import FONT_MEDIUM, FONT_LARGE

def load():
    global FONT_R_M, FONT_S_L
    FONT_R_M = pygame.font.Font("assets/IS-Reg.ttf", FONT_MEDIUM)
    FONT_S_L = pygame.font.Font("assets/IS-Semi.ttf", FONT_LARGE)