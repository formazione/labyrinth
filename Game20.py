'''
Function:
    走迷宫小游戏
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import cfg
import sys
import pygame
from modules import *


'''主函数'''
def main(cfg):
    # 初始化
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.mixer.music.load(cfg.BGMPATH)
    pygame.mixer.music.play(-1, 0.0)
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('Maze —— Charles的皮卡丘')
    font = pygame.font.SysFont('Consolas', 15)
    # 开始界面
    print("Debug:\nNow we are into modules/misc.py Interface class")
    print("the modules in modules are called with from modules import *")
    print("The buttons are made with class Button, always in misc.py")
    print("""If you press start, there's this code

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_1.collidepoint(pygame.mouse.get_pos()):
                        return True
        
        That will return True
        """)
    Interface(screen, cfg, 'game_start') # it's in modules/misc.py
    print("======================")
    print("Here is the maze, after return from the mode='game start' if statememt in Interface")
    print("Now the mode is set to 'game_switch'")
    # 记录关卡数
    num_levels = 0
    # 记录最少用了多少步通关
    best_scores = 'None'
    # 关卡循环切换
    while True:
        num_levels += 1
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(cfg.SCREENSIZE)
        # --随机生成关卡地图
        maze_now = RandomMaze(cfg.MAZESIZE, cfg.BLOCKSIZE, cfg.BORDERSIZE)
        # --生成hero
        hero_now = Hero(cfg.HEROPICPATH, [0, 0], cfg.BLOCKSIZE, cfg.BORDERSIZE)
        # --统计步数
        num_steps = 0
        # --关卡内主循环
        while True:
            dt = clock.tick(cfg.FPS)
            screen.fill((255, 255, 255))
            is_move = False
            # ----↑↓←→控制hero
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(-1)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        is_move = hero_now.move('up', maze_now)
                    elif event.key == pygame.K_DOWN:
                        is_move = hero_now.move('down', maze_now)
                    elif event.key == pygame.K_LEFT:
                        is_move = hero_now.move('left', maze_now)
                    elif event.key == pygame.K_RIGHT:
                        is_move = hero_now.move('right', maze_now)
            num_steps += int(is_move)
            hero_now.draw(screen)
            maze_now.draw(screen)
            # ----显示一些信息
            showText(screen, font, 'LEVELDONE: %d' % num_levels, (255, 0, 0), (10, 10))
            showText(screen, font, 'BESTSCORE: %s' % best_scores, (255, 0, 0), (210, 10))
            showText(screen, font, 'USEDSTEPS: %s' % num_steps, (255, 0, 0), (410, 10))
            showText(screen, font, 'S: your starting point    D: your destination', (255, 0, 0), (10, 600))
            # ----判断游戏是否胜利
            if (hero_now.coordinate[0] == cfg.MAZESIZE[1] - 1) and (hero_now.coordinate[1] == cfg.MAZESIZE[0] - 1):
                print("you won")
                break # This will break the while loop and make you go in game switch mode
            pygame.display.update()
        # --更新最优成绩
        if best_scores == 'None':
            best_scores = num_steps
        else:
            if best_scores > num_steps:
                best_scores = num_steps
        # --关卡切换
        # when you win you go here
        print("you won, so you go in game_switch")
        Interface(screen, cfg, mode='game_switch')


'''run'''
if __name__ == '__main__':
    main(cfg)