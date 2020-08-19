"""
使用pygame制作个大球吃小球的游戏
"""
import pygame
from PIL import Image

def main():
    #初始化导入pygame模块
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')

    #写一个循环，让界面持续响应
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()