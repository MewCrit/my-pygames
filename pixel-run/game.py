import pygame

from sys import exit
from random import randint, choice

from player import Player
from enemies import Enemies


def display_score(): 
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'{current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    return current_time
    

# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5
             
#             if obstacle_rect.bottom == 300: 
#                 screen.blit(snail_surface, obstacle_rect)
#             else:
#                 screen.blit(fly_surface, obstacle_rect)

#         # Delete rectangle objects if it is lower than 100
#         obstacle_list = [obs for obs in obstacle_list if obs.x > -100 ]

#         return obstacle_list
#     else:
#         return [] 


def collisions(player, obstacles):
    if obstacles:
        for rect in obstacles:
            if player.colliderect(rect):
                return False
    return True

def collide():
    if pygame.sprite.spritecollide(player.sprite, enemy, False):
        enemy.empty()
        return False
    else:
        return True


# def player_animation():
#     global player_surface, player_index

#     if player_rect.bottom < 300:
#         player_surface = player_jump
#     else:
#         player_index += 0.1
#         if player_index >= len(player_walk):
#             player_index = 0
#         player_surface = player_walk[int(player_index)]



pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 40)
game_active = False
start_time = 0
score = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

enemy = pygame.sprite.Group()



image_load = pygame.image

sky_surface = image_load.load('graphics/Sky.png').convert()
ground_surface = image_load.load('graphics/ground.png').convert()
text_surface = test_font.render('Pixel Run', False, 'Black')

pygame.mixer.Sound('audio/music.wav').play(loops= -1)
# Obstacles

obstacle_list =[]

# snail_frame_1 = image_load.load('graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = image_load.load('graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_frame_index = 0
# snail_surface = snail_frames[snail_frame_index]


# fly_frame_1 = image_load.load('graphics/Fly/Fly1.png').convert_alpha()
# fly_frame_2 = image_load.load('graphics/Fly/Fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_frame_index = 0
# fly_surface = fly_frames[fly_frame_index]


obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

# Player image

# walk
# player_surface_walk_1 = image_load.load('graphics/player/player_walk_1.png').convert_alpha()
# player_surface_walk_2 = image_load.load('graphics/player/player_walk_2.png').convert_alpha()
# player_walk = [player_surface_walk_1, player_surface_walk_2]

player_index = 0

# jump
player_jump = image_load.load('graphics/player/jump.png').convert_alpha()


# Place a rectangle arround the image
# player_surface = player_walk[player_index]
# player_rect = player_surface.get_rect(midbottom = (80, 300))
# player_gravity = 0


score_surface = test_font.render('0', False, 'Black')
score_rect = score_surface.get_rect(center = (370, 30))

guide_surface = test_font.render('Press Space button to play', False, 'Black')
guide_rect = guide_surface.get_rect(center = (390, 300))

title_surface = test_font.render('PIXEL RUNER', False, 'Black')
title_rect = title_surface.get_rect(center = (390, 260))


snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
 

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


while True:
    # get all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            pass
            # if event.type == pygame.MOUSEMOTION:
            #     mouse_position = pygame.mouse.get_pos()
            #     if player_rect.collidepoint(mouse_position):
            #         print('12122')  
        
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE and player_rect.bottom == 300:
            #         player_gravity = -20 
        else :
             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    # reset score
                    start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
           

            if event.type == obstacle_timer:
                enemy.add(Enemies(choice(['fly', 'snail'])))   

            
            # if event.type == snail_animation_timer:
            #     if snail_frame_index == 0: 
            #         snail_frame_index = 1
            #     else:
            #         snail_frame_index = 0
                
            #     snail_surface = snail_frames[snail_frame_index]

            # if event.type == fly_animation_timer:
            #     if fly_frame_index == 0: 
            #         fly_frame_index = 1
            #     else:
            #         fly_frame_index = 0
                
            #     fly_surface = fly_frames[fly_frame_index]
     
    if game_active:
        
        # blit: block limit image transfer ( blit(test_surface, (x,y))   )
        # order here matters
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        # screen.blit(text_surface, (350, 50))

        score = display_score()
        
        # snail_rect.x -= 4

        # if snail_rect.x == -100 : 
        #     snail_rect.x=800

        # screen.blit(snail_surface, snail_rect)
        
        # apply gravity to player
        # player_gravity +=0.9
        # player_rect.y += player_gravity

        # # apply ground to player
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300

        # player_animation()
        # screen.blit(player_surface, player_rect)


        player.draw(screen)
        player.update()

        enemy.draw(screen)
        enemy.update()



        # Obstacle movement
        # obstacle_list = obstacle_movement(obstacle_list)


        # apply collision between player and enemy
        game_active =  collide()

    else:
        screen.fill('Yellow')
        final_score_surface = test_font.render(f'Your score is: {score}', False, 'Black')
        final_score_rect = final_score_surface.get_rect(center = (390, 100))
       
        if score > 0:
           screen.blit(final_score_surface, final_score_rect)
          
        screen.blit(guide_surface, guide_rect)
        screen.blit(title_surface, title_rect)
        obstacle_list.clear()


    pygame.display.update()
    clock.tick(60)