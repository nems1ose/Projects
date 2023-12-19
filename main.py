import pygame
import math

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Semen's Games")
icon = pygame.image.load('images/6834201_ghost_halloween_horror_scary_skeleton_icon.png').convert_alpha()
pygame.display.set_icon(icon)

def game(level, index_sky1_square, index_sky2_square, exit_x, exit_y,
         index_ghost, index_axes_x, index_axes_y, money_x, money_y,
         ghost_sky_x, cobweb_x, cobweb_y, broom_x, broom_y, coffin_x, coffin_y,
         ghost_jump_x, helmet_x, helmet_y, ghost_jump_spavn_x):

    gameplay = True

    label = pygame.font.Font('fonts/DoorsDefinitiveRegularr.ttf', 40)
    information = pygame.font.Font('fonts/DoorsDefinitiveRegularr.ttf', 60)
    lose_label = label.render('YOU LOSE', False, (193, 196, 199))
    restart_label = label.render('RESTART', False, (115, 132, 148))
    restart_label_rect = restart_label.get_rect(topleft=(550, 330))
    pause_label = label.render('PAUSE', False, (193, 196, 199))
    pause_label_rect = pause_label.get_rect(topleft=(1100, 30))
    resume_label = label.render('RESUME', False, (115, 132, 148))
    resume_label_rect = resume_label.get_rect(topleft=(550, 370))
    menu_in_pause_label = label.render('MENU', False, (193, 196, 199))
    menu_in_pause_label_rect = menu_in_pause_label.get_rect(topleft=(30, 30))

    bg = pygame.image.load('images/946f035d76a03dc11a7d5566e86311ce.jpg').convert_alpha()
    square = pygame.image.load('images/85347_square_icon (1).png').convert_alpha()
    ghost = pygame.image.load('images/6834201_ghost_halloween_horror_scary_skeleton_icon.png').convert_alpha()
    axe = pygame.image.load('images/6834214_axe_ghost_halloween_horror_scary_icon.png').convert_alpha()
    exit = pygame.image.load('images/1531901_spooky_halloween_ghost_castle_icon (1).png').convert_alpha()
    money = pygame.image.load('images/6834227_ghost_halloween_horror_monster_scary_icon.png').convert_alpha()
    ghost_sky = pygame.image.load('images/6834232_creepy_ghost_halloween_horror_monster_icon.png').convert_alpha()
    cobweb = pygame.image.load('images/6834206_ghost_halloween_horror_scary_spider web_icon.png').convert_alpha()
    broom = pygame.image.load('images/6834247_ghost_halloween_horror_monster_scary_icon.png').convert_alpha()
    coffin = pygame.image.load('images/6834210_coffin_ghost_halloween_horror_scary_icon.png').convert_alpha()
    ghost_jump = pygame.image.load('images/6834236_ghost_halloween_horror_pumpkin_scary_icon.png').convert_alpha()
    helmet = pygame.image.load('images/6834203_ghost_halloween_horror_monster_scary_icon.png').convert_alpha()
    ghost_jump_spavn = pygame.image.load('images/6834212_ghost_halloween_horror_magic pot_scary_icon.png').convert_alpha()
    right1 = pygame.image.load('images/right 1.png').convert_alpha()
    right2 = pygame.image.load('images/right 2.png').convert_alpha()
    right3 = pygame.image.load('images/right 3.png').convert_alpha()
    right4 = pygame.image.load('images/right 4.png').convert_alpha()
    left1 = pygame.image.load('images/left 1.png').convert_alpha()
    left2 = pygame.image.load('images/left 2.png').convert_alpha()
    left3 = pygame.image.load('images/left 3.png').convert_alpha()
    left4 = pygame.image.load('images/left 4.png').convert_alpha()

    square_list_in_game = []
    square_tach = []
    for bgi in range(exit_x + 20):
        square_list_in_game.append(square.get_rect(topleft=(bgi * 64, 680)))
        square_tach.append(False)
    sky1_square = []
    sky1_square_tach = []
    sky2_square = []
    sky2_square_tach = []
    exit_x_64 = exit_x * 64

    player_x = 100
    player_y = 616
    is_jump = False
    is_down = False
    jump_num = 0
    down_num = 0
    jump_prog = [128, 64, 32, 16, 8, 4, 2, 2, 4, 8, 10, 20, 40, 80, 66, 24, 103, 103, 24, 100, 130] #382
    down_prog = [2, 4, 8, 10, 20, 40, 80, 66, 24, 103, 103, 24, 100, 130] #24 230 254 460 484 714
    right_go = [right1, right2, right3, right4]
    right_index = 0
    left_go = [left1, left2, left3, left4]
    left_index = 0
    player_go_right = False
    player_go_left = False

    ghost_y = 630
    #ghost_timer = pygame.USEREVENT + 1
    #pygame.time.set_timer(ghost_timer, 10000)
    ghost_list_in_game = []

    ghost_sky_list_in_game_x = []
    ghost_sky_list_in_game_y = []

    ghost_jump_num_list = []
    ghost_down_num_list = []
    ghost_jump_prog = [72, 32, 16, 8, 4, 2, 1] #135
    ghost_down_prog = [1, 2, 4, 8, 16, 32, 72] #135
    ghost_jump_list_x = []
    ghost_jump_list_y = []
    time_jump_list = []
    time_down_list = []
    time_stop_list = []

    ghost_jump_spavn_list = []
    ghost_jump_spavn_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_jump_spavn_timer, 10000)

    cobweb_list = []
    cobweb_list_tach = []
    cobweb_tach = False
    broom_col = 0
    broon_list = []

    coffin_list = []

    right_shoot = True
    axes = []
    axes_col = 0
    axes_shoot = [] #сторона в которую стреляем
    #axes_timer = pygame.USEREVENT + 1
    #pygame.time.set_timer(axes_timer, 2000)
    lose_axes = [] #лежащие топоры

    lose_money = []
    money_col = 0

    helmet_col = 0
    lose_helmet = []

    menu_lose = False
    resume_t = False

    index_game = 0

    #PLATFORM
    for index_sky1 in index_sky1_square:
        sky1_square.append(square.get_rect(topleft=(index_sky1 * 64 + 1408, 450)))
        sky1_square_tach.append(False)

    for index_sky2 in index_sky2_square:
        sky2_square.append(square.get_rect(topleft=(index_sky2 * 64 + 1408, 220)))
        sky2_square_tach.append(False)

    #GHOST
    for i in index_ghost:
        ghost_list_in_game.append(i * 64 + 1408)

    #GHOST SKY
    for (i, el) in enumerate(ghost_sky_x):
        ghost_sky_list_in_game_x.append(ghost_sky_x[i] * 64 + 1408)
        ghost_sky_list_in_game_y.append(0)

    #GHOST JUMP
    for (i, el) in enumerate(ghost_jump_x):
        ghost_jump_list_x.append(ghost_jump_x[i] * 64 + 1408)
        ghost_jump_list_y.append(640)
        ghost_jump_num_list.append(0)
        ghost_down_num_list.append(0)
        time_down_list.append(0)
        time_stop_list.append(0)
        time_jump_list.append(0)

    #LOSE MONEY
    for (i, el) in enumerate(money_x):
        lose_money.append(money.get_rect(topleft=(money_x[i] * 64 + 1408, money_y[i] - 10)))

    #LOSE HELMET
    for (i, el) in enumerate(helmet_x):
        lose_helmet.append(helmet.get_rect(topleft=(helmet_x[i] * 64 + 1408, helmet_y[i] - 10)))

    #LOSE AXES
    for (i, el) in enumerate(index_axes_x):
        lose_axes.append(axe.get_rect(topleft=(index_axes_x[i] * 64 + 1408, index_axes_y[i] - 10)))

    #BROOM
    for (i, el) in enumerate(broom_x):
        broon_list.append(broom.get_rect(topleft=(broom_x[i] * 64 + 1408, broom_y[i] - 10)))

    #COBWEB
    for (i, el) in enumerate(cobweb_x):
        cobweb_list.append(cobweb.get_rect(topleft=(cobweb_x[i] * 64 + 1408, cobweb_y[i] - 10)))
        cobweb_list_tach.append(False)

    #GHOST SPAVN
    for (i, el) in enumerate(ghost_jump_spavn_x):
        ghost_jump_spavn_list.append(ghost_jump_spavn.get_rect(topleft=(ghost_jump_spavn_x[i] * 64 + 1408, 600)))

    #COFFIN
    for (i, el) in enumerate(coffin_x):
        coffin_list.append(coffin.get_rect(topleft=(coffin_x[i] * 64 + 1408, coffin_y[i] - 10)))

    running = True
    while running:
        screen.blit(bg, (0, 0))

        if gameplay:

            keys = pygame.key.get_pressed()

            #MENU
            screen.blit(pause_label, pause_label_rect)

            mouse_1 = pygame.mouse.get_pos()
            if pause_label_rect.collidepoint(mouse_1) and pygame.mouse.get_pressed()[0]:
                gameplay = False

            # PLAYER
            if not player_go_right:
                right_index = 0
            if not player_go_left:
                left_index = 0
            if right_shoot:
                player_rect = right_go[right_index // 4].get_rect(topleft=(player_x - index_game, player_y))
                screen.blit(right_go[right_index // 4], (player_x - index_game, player_y))
                if right_index < 15:
                    right_index += 1
                else:
                    right_index = 0
            else:
                player_rect = left_go[left_index // 4].get_rect(topleft=(player_x - index_game, player_y))
                screen.blit(left_go[left_index // 4], (player_x - index_game, player_y))
                if left_index < 15:
                    left_index += 1
                else:
                    left_index = 0

            # EXIT
            exit_rect = exit.get_rect(topleft=(exit_x_64, exit_y))
            screen.blit(exit, (exit_x_64, exit_y))

            if player_rect.colliderect(exit_rect):
                return(money_col)

            #GAME PLATFORM
            for (i, squareel) in enumerate(square_list_in_game):
                screen.blit(square, squareel)
                if player_rect.colliderect(squareel):
                    square_tach[i] = True
                else:
                    square_tach[i] = False

            for (i, squareel) in enumerate(sky1_square):
                screen.blit(square, squareel)
                if player_rect.colliderect(squareel):
                    sky1_square_tach[i] = True
                else:
                    sky1_square_tach[i] = False

            for (i, squareel) in enumerate(sky2_square):
                screen.blit(square, squareel)
                if player_rect.colliderect(squareel):
                    sky2_square_tach[i] = True
                else:
                    sky2_square_tach[i] = False

            sky1_tach = False
            sky2_tach = False
            sky0_tach = False

            for el in square_tach:
                sky0_tach = sky0_tach or el
            for el in sky1_square_tach:
                sky1_tach = sky1_tach or el
            for el in sky2_square_tach:
                sky2_tach = sky2_tach or el

            #UP CONFIGURATIONS
            screen.blit(axe, (30, 20))
            label_axe_col = label.render(": " + str(axes_col), False, (193, 196, 199))
            screen.blit(label_axe_col, (80, 10))
            screen.blit(broom, (180, 18))
            label_broom_col = label.render(": " + str(broom_col), False, (193, 196, 199))
            screen.blit(label_broom_col, (230, 10))
            screen.blit(helmet, (330, 19))
            label_helmet_col = label.render(": " + str(helmet_col), False, (193, 196, 199))
            screen.blit(label_helmet_col, (380, 10))
            screen.blit(money, (480, 19))
            label_money_col = label.render(str(money_col) + " / 3", False, (193, 196, 199))
            screen.blit(label_money_col, (530, 10))

            #CONFIGURATIONS
            if level == 1:
                if 0 < player_x < 200:
                    label_1 = information.render("TAB lefr/rignt TO WALK", False, (193, 196, 199))
                    screen.blit(label_1, (30, 70))
                if 200 < player_x < 400:
                    label_2 = information.render("TAB up TO JUMP", False, (193, 196, 199))
                    screen.blit(label_2, (30, 70))
                if 400 < player_x < 600:
                    label_3 = information.render("TAB q TO Shoot the axe", False, (193, 196, 199))
                    screen.blit(label_3, (30, 70))
                if 600 < player_x < 800:
                    label_4 = information.render("Use a axe to kill the cteatures", False, (193, 196, 199))
                    screen.blit(label_4, (30, 70))
                if 800 < player_x < 1000:
                    label_5 = information.render("Collect all of the three bags", False, (193, 196, 199))
                    screen.blit(label_5, (30, 70))
            elif level == 10:
                if 0 < player_x < 1000:
                    label_6 = information.render("Use a broom to remove the cobwebs. Tab w", False, (193, 196, 199))
                    screen.blit(label_6, (30, 70))

            #JUMP
            if not is_jump:
                if keys[pygame.K_UP] and not is_down and not cobweb_tach:
                    is_jump = True
            else:
                if jump_num < len(jump_prog):
                    t = 0
                    if jump_num <= 6:
                        player_y -= jump_prog[jump_num]
                    else:
                        if not (sky0_tach or sky2_tach or sky1_tach) or (player_y != 618 and player_y != 388 and player_y != 158):
                                player_y += jump_prog[jump_num]
                                jump_num += 1
                                t = 1
                        else:
                            jump_num = 0
                            is_jump = False
                    if is_jump and t == 0:
                        jump_num += 1
                else:
                    jump_num = 0
                    is_jump = False

            #DOWN
            if not is_jump:
                if not (sky0_tach or sky2_tach or sky1_tach) or (player_y != 618 and player_y != 388 and player_y != 158):
                    is_down = True
                    if down_num < len(down_prog):
                        player_y += down_prog[down_num]
                        down_num += 1
                else:
                    down_num = 0
                    is_down = False

            #CORRECT COORDINATES
            if player_y > 618:
                player_y = 616
                down_num = 0
                jump_num = 0
                is_jump = False
                is_down = False

            #GHOST
            if ghost_list_in_game:
                for (i, el) in enumerate(ghost_list_in_game):
                    ghost_rect = ghost.get_rect(topleft=(el - index_game, ghost_y))
                    screen.blit(ghost, (el - index_game, ghost_y))
                    if -960 < player_x - el < 960:
                        if player_x > el:
                            ghost_list_in_game[i] += 2
                        else:
                            ghost_list_in_game[i] += -2

                    if player_rect.colliderect(ghost_rect):
                        if helmet_col == 0:
                            gameplay = False
                            menu_lose = True
                        else:
                            helmet_col -= 1
                            ghost_list_in_game.pop(i)

            #GHOST SKY
            if ghost_sky_list_in_game_x:
                for (i, el) in enumerate(ghost_sky_list_in_game_x):
                    ghost_sky_rect = ghost_sky.get_rect(topleft=(el - index_game, ghost_sky_list_in_game_y[i]))
                    screen.blit(ghost_sky, (el - index_game, ghost_sky_list_in_game_y[i]))
                    if -960 < player_x - el < 960:
                        x_t = abs(player_x - el)
                        y_t = abs(player_y - ghost_sky_list_in_game_y[i])
                        if player_x > el:
                            ghost_sky_list_in_game_x[i] += 2 * math.ceil(x_t / (x_t + y_t))
                            if y_t < 2:
                                ghost_sky_list_in_game_x[i] += 1
                        else:
                            ghost_sky_list_in_game_x[i] += -2 * math.ceil(x_t / (x_t + y_t))
                            if y_t < 2:
                                ghost_sky_list_in_game_x[i] += -1
                        if player_y > ghost_sky_list_in_game_y[i]:
                            ghost_sky_list_in_game_y[i] += 2 * math.ceil(y_t / (x_t + y_t))
                            if x_t < 2:
                                ghost_sky_list_in_game_y[i] += 1
                        else:
                            ghost_sky_list_in_game_y[i] += -2 * math.ceil(y_t / (x_t + y_t))
                            if x_t < 2:
                                ghost_sky_list_in_game_y[i] += -1

                    if player_rect.colliderect(ghost_sky_rect):
                        if helmet_col == 0:
                            gameplay = False
                            menu_lose = True
                        else:
                            helmet_col -= 1
                            ghost_sky_list_in_game_x.pop(i)
                            ghost_sky_list_in_game_y.pop(i)

            #GHOST JUMP
            if ghost_jump_list_x:
                for (i, el) in enumerate(ghost_jump_list_x):
                    ghost_jump_rect = ghost_jump.get_rect(topleft=(el - index_game, ghost_jump_list_y[i]))
                    screen.blit(ghost_jump, (el - index_game, ghost_jump_list_y[i]))
                    if -960 < player_x - el < 960:
                        if time_stop_list[i] == 20:
                            if player_x > el:
                                if -7 < player_x - el < 7:
                                    ghost_jump_list_x[i] = player_x
                                else:
                                    ghost_jump_list_x[i] += 7
                            elif player_x < el:
                                if -7 < player_x - el < 7:
                                    ghost_jump_list_x[i] = player_x
                                else:
                                    ghost_jump_list_x[i] += -7
                            if ghost_jump_list_y[i] == 640:
                                if time_jump_list[i] == 0:
                                    ghost_jump_list_y[i] -= ghost_jump_prog[ghost_jump_num_list[i]]
                                    ghost_jump_num_list[i] += 1
                                    time_jump_list[i] = 0
                                else:
                                    time_jump_list[i] += 1
                            elif ghost_jump_num_list[i] > 0:
                                if time_jump_list[i] == 0:
                                    ghost_jump_list_y[i] -= ghost_jump_prog[ghost_jump_num_list[i]]
                                    if ghost_jump_list_y[i] == 505:
                                        ghost_jump_num_list[i] = 0
                                    else:
                                        ghost_jump_num_list[i] += 1
                                    time_jump_list[i] = 0
                                else:
                                    time_jump_list[i] += 1
                            elif ghost_jump_list_y[i] == 505:
                                if time_down_list[i] == 0:
                                    ghost_jump_list_y[i] += ghost_down_prog[ghost_down_num_list[i]]
                                    ghost_down_num_list[i] += 1
                                    time_down_list[i] = 0
                                else:
                                    time_down_list[i] += 1
                            else:
                                if time_down_list[i] == 0:
                                    ghost_jump_list_y[i] += ghost_down_prog[ghost_down_num_list[i]]
                                    if ghost_jump_list_y[i] == 640:
                                        ghost_down_num_list[i] = 0
                                        time_stop_list[i] = 0
                                    else:
                                        ghost_down_num_list[i] += 1
                                    time_down_list[i] = 0
                                else:
                                    time_down_list[i] += 1
                        else:
                            time_stop_list[i] += 1

                    if player_rect.colliderect(ghost_jump_rect):
                        if helmet_col == 0:
                            gameplay = False
                            menu_lose = True
                        else:
                            helmet_col -= 1
                            ghost_jump_list_x.pop(i)
                            ghost_jump_list_y.pop(i)
                            time_stop_list.pop(i)
                            time_down_list.pop(i)
                            time_jump_list.pop(i)
                            ghost_jump_num_list.pop(i)
                            ghost_down_num_list.pop(i)

            #COFFIN
            if coffin_list:
                for (i, el) in enumerate(coffin_list):
                    screen.blit(coffin, el)

                    if player_rect.colliderect(el):
                        coffin_list.pop(i)
                        ghost_sky_list_in_game_x.append(player_x )
                        ghost_sky_list_in_game_y.append(0)
                        ghost_sky_list_in_game_x.append(player_x + 320)
                        ghost_sky_list_in_game_y.append(0)
                        ghost_sky_list_in_game_x.append(player_x - 320)
                        ghost_sky_list_in_game_y.append(0)

            #COBWEB
            if cobweb_list:
                for (i, el) in enumerate(cobweb_list):
                    screen.blit(cobweb, el)

                    if player_rect.colliderect(el):
                        cobweb_list_tach[i] = True
                    else:
                        cobweb_list_tach[i] = False

            cobweb_tach = False
            for el in cobweb_list_tach:
                cobweb_tach = cobweb_tach or el

            if cobweb_tach:
                player_spped = 1
            else:
                player_spped = 6

            #GHOST SPAVN
            if ghost_jump_spavn_list:
                for (i, el) in enumerate(ghost_jump_spavn_list):
                    screen.blit(ghost_jump_spavn, el)

            #BROOM
            if broon_list:
                for (i, el) in enumerate(broon_list):
                    screen.blit(broom, el)

                    if player_rect.colliderect(el):
                        broom_col += 1
                        broon_list.pop(i)

            #LOSE MONEY
            if lose_money:
                for (i, el) in enumerate(lose_money):
                    screen.blit(money, el)

                    if player_rect.colliderect(el):
                        money_col += 1
                        lose_money.pop(i)

            #LOSE AXES
            if lose_axes:
                for (i, el) in enumerate(lose_axes):
                    screen.blit(axe, el)

                    if player_rect.colliderect(el):
                        axes_col += 1
                        lose_axes.pop(i)

            #LOSE HELMET
            if lose_helmet:
                for (i, el) in enumerate(lose_helmet):
                    screen.blit(helmet, el)
                    if player_rect.colliderect(el):
                        helmet_col += 1
                        lose_helmet.pop(i)

            #AXES
            if axes:
                for (i, el) in enumerate(axes):
                    screen.blit(axe, (el.x - index_game, el.y))
                    if axes_shoot[i]:
                        el.x += 7
                    else:
                        el.x -= 7

                    axe_life = True

                    if el.x > player_x + 640 or el.x < player_x - 640:
                        axes.pop(i)
                        axes_shoot.pop(i)
                        continue

                    if ghost_list_in_game:
                        for (index, ghostel) in enumerate(ghost_list_in_game):
                            if el.colliderect(ghost.get_rect(topleft=(ghostel, ghost_y))):
                                ghost_list_in_game.pop(index)
                                axes.pop(i)
                                axes_shoot.pop(i)
                                axe_life = False
                                break

                    if not axe_life:
                        continue

                    if ghost_sky_list_in_game_x:
                        for (index, ghostel) in enumerate(ghost_sky_list_in_game_x):
                            if el.colliderect(ghost_sky.get_rect(topleft=(ghostel, ghost_sky_list_in_game_y[index]))):
                                ghost_sky_list_in_game_x.pop(index)
                                ghost_sky_list_in_game_y.pop(index)
                                axes.pop(i)
                                axes_shoot.pop(i)
                                axe_life = False
                                break

                    if not axe_life:
                        continue

                    if ghost_jump_list_x:
                        for (index, ghostel) in enumerate(ghost_jump_list_x):
                            if el.colliderect(ghost_jump.get_rect(topleft=(ghostel, ghost_jump_list_y[index]))):
                                ghost_jump_list_x.pop(index)
                                ghost_jump_list_y.pop(index)
                                time_stop_list.pop(index)
                                time_down_list.pop(index)
                                time_jump_list.pop(index)
                                ghost_jump_num_list.pop(index)
                                ghost_down_num_list.pop(index)
                                axes.pop(i)
                                axes_shoot.pop(i)
                                axe_life = False
                                break

                    if not axe_life:
                        continue

                    if ghost_jump_spavn_list:
                        for (index, ghostel) in enumerate(ghost_jump_spavn_list):
                            ghostel.x += index_game
                            if el.colliderect(ghostel):
                                ghost_jump_spavn_list.pop(index)
                                axes.pop(i)
                                axes_shoot.pop(i)
                                axe_life = False
                                break
                            ghostel.x -= index_game

                    if not axe_life:
                        continue

            #WALK
            player_go_right = False
            player_go_left = False
            if keys[pygame.K_LEFT]:
                right_shoot = False
                player_go_left = True
                if player_x - index_game > 300:
                    player_x -= player_spped
                elif index_game > 300:
                    index_game -= player_spped
                    player_x -= player_spped
                    exit_x_64 += player_spped
                    for (i, squareel) in enumerate(square_list_in_game):
                        squareel.x += player_spped
                    for (i, squareel) in enumerate(sky1_square):
                        squareel.x += player_spped
                    for (i, squareel) in enumerate(sky2_square):
                        squareel.x += player_spped
                    for (i, el) in enumerate(lose_money):
                        el.x += player_spped
                    for (i, el) in enumerate(lose_axes):
                        el.x += player_spped
                    for (i, el) in enumerate(lose_helmet):
                        el.x += player_spped
                    for (i, el) in enumerate(cobweb_list):
                        el.x += player_spped
                    for (i, el) in enumerate(broon_list):
                        el.x += player_spped
                    for (i, el) in enumerate(coffin_list):
                        el.x += player_spped
                    for (i, el) in enumerate(ghost_jump_spavn_list):
                        el.x += player_spped

            elif keys[pygame.K_RIGHT]:
                right_shoot = True
                player_go_right = True
                if player_x - index_game < 980:
                    player_x += player_spped
                else:
                    index_game += player_spped
                    player_x += player_spped
                    exit_x_64 -= player_spped
                    for (i, squareel) in enumerate(square_list_in_game):
                        squareel.x -= player_spped
                    for (i, squareel) in enumerate(sky1_square):
                        squareel.x -= player_spped
                    for (i, squareel) in enumerate(sky2_square):
                        squareel.x -= player_spped
                    for (i, el) in enumerate(lose_money):
                        el.x -= player_spped
                    for (i, el) in enumerate(lose_axes):
                        el.x -= player_spped
                    for (i, el) in enumerate(lose_helmet):
                        el.x -= player_spped
                    for (i, el) in enumerate(cobweb_list):
                        el.x -= player_spped
                    for (i, el) in enumerate(broon_list):
                        el.x -= player_spped
                    for (i, el) in enumerate(coffin_list):
                        el.x -= player_spped
                    for (i, el) in enumerate(ghost_jump_spavn_list):
                        el.x -= player_spped

        #PAUSE
        else:
            screen.fill((87, 88, 89))
            if menu_lose:
                screen.blit(lose_label, (550, 290))
            else:
                screen.blit(resume_label, resume_label_rect)
                resume_t = True
            screen.blit(restart_label, restart_label_rect)
            screen.blit(menu_in_pause_label, menu_in_pause_label_rect)

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                return(-2)
            if resume_t:
                if resume_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    gameplay = True
                    resume_t = False
            if menu_in_pause_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                return(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return (-1)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return(-1)
            if gameplay:
                if event.type == ghost_jump_spavn_timer:
                    for (i, el) in enumerate(ghost_jump_spavn_list):
                        ghost_jump_list_x.append(el.x + index_game + 20)
                        ghost_jump_list_y.append(505)
                        time_stop_list.append(0)
                        time_down_list.append(0)
                        time_jump_list.append(0)
                        ghost_jump_num_list.append(0)
                        ghost_down_num_list.append(0)
                #if index_game is in index_ghost:
                #    ghost_list_in_game.append(ghost.get_rect(topleft=(ghost_x, ghost_y)))
                if event.type == pygame.KEYUP and keys[pygame.K_q] and axes_col > 0:
                    axes.append(axe.get_rect(topleft=(player_x, player_y + 10)))
                    axes_shoot.append(right_shoot)
                    axes_col -= 1
                if event.type == pygame.KEYUP and keys[pygame.K_w] and broom_col > 0:
                    for (i, el) in enumerate(cobweb_list):
                        if player_rect.colliderect(el):
                            cobweb_list.pop(i)
                            cobweb_list_tach.pop(i)
                            broom_col -= 1
                            break
                #if event.type == axes_timer:
                #    lose_axes.append(axe.get_rect(topleft=(1400, 630)))
        clock.tick(40)


level = 0
menu_running = True
play_quit = False
go_game = False
menu_label = pygame.font.Font('fonts/DoorsDefinitiveRegularr.ttf', 40)
choice_label = pygame.font.Font('fonts/DoorsDefinitiveRegularr.ttf', 60)
choice = choice_label.render('choose a level', False, (255, 255, 224))
part1 = menu_label.render('part 1', False, (255, 255, 224))
part2 = menu_label.render('part 2', False, (255, 255, 224))
part3 = menu_label.render('part 3', False, (255, 255, 224))
part4 = menu_label.render('part 4', False, (255, 255, 224))
part5 = menu_label.render('part 5', False, (255, 255, 224))
part0 = menu_label.render(' / 24', False, (255, 255, 224))
level_1_text = menu_label.render('1', False, (255, 255, 224))
level_2_text = menu_label.render('2', False, (255, 255, 224))
level_3_text = menu_label.render('3', False, (255, 255, 224))
level_4_text = menu_label.render('4', False, (255, 255, 224))
level_5_text = menu_label.render('5', False, (255, 255, 224))
level_6_text = menu_label.render('6', False, (255, 255, 224))
level_7_text = menu_label.render('7', False, (255, 255, 224))
level_8_text = menu_label.render('8', False, (255, 255, 224))
level_9_text = menu_label.render('9', False, (255, 255, 224))
level_10_text = menu_label.render('10', False, (255, 255, 224))
level_11_text = menu_label.render('11', False, (255, 255, 224))
level_12_text = menu_label.render('12', False, (255, 255, 224))
level_13_text = menu_label.render('13', False, (255, 255, 224))
level_14_text = menu_label.render('14', False, (255, 255, 224))
level_15_text = menu_label.render('15', False, (255, 255, 224))
level_16_text = menu_label.render('16', False, (255, 255, 224))
level_17_text = menu_label.render('17', False, (255, 255, 224))
level_18_text = menu_label.render('18', False, (255, 255, 224))
level_19_text = menu_label.render('19', False, (255, 255, 224))
level_20_text = menu_label.render('20', False, (255, 255, 224))
level_21_text = menu_label.render('21', False, (255, 255, 224))
level_22_text = menu_label.render('22', False, (255, 255, 224))
level_23_text = menu_label.render('23', False, (255, 255, 224))
level_24_text = menu_label.render('24', False, (255, 255, 224))
level_label = pygame.image.load('images/3305209_environment_fall_forest_nature_rock_icon (1).png').convert_alpha()
points = pygame.image.load('images/299110_check_sign_icon.png').convert_alpha()

point = []
for ind in range(46):
    point.append(0)
level_l_x = []
level_l_y = []
for i in range(225, 525, 100):
    for j in range (250, 1050, 100): #200 1100 100
        level_l_x.append(j)
        level_l_y.append(i)
for i in range(1):
    point.append(0)

while menu_running:
    screen.fill((87, 88, 89))
    screen.blit(choice, (470, 100))

    for (i, el) in enumerate(level_l_x):
        screen.blit(level_label, (el, level_l_y[i]))
    screen.blit(level_1_text, level_1_text.get_rect(topleft=(273, 233)))
    screen.blit(level_2_text, level_2_text.get_rect(topleft=(373, 233)))
    screen.blit(level_3_text, level_3_text.get_rect(topleft=(473, 233)))
    screen.blit(level_4_text, level_4_text.get_rect(topleft=(573, 233)))
    screen.blit(level_5_text, level_5_text.get_rect(topleft=(673, 233)))
    screen.blit(level_6_text, level_6_text.get_rect(topleft=(773, 233)))
    screen.blit(level_7_text, level_7_text.get_rect(topleft=(873, 233)))
    screen.blit(level_8_text, level_8_text.get_rect(topleft=(973, 233)))

    screen.blit(level_9_text, level_9_text.get_rect(topleft=(273, 333)))
    screen.blit(level_10_text, level_10_text.get_rect(topleft=(365, 333)))
    screen.blit(level_11_text, level_11_text.get_rect(topleft=(465, 333)))
    screen.blit(level_12_text, level_12_text.get_rect(topleft=(565, 333)))
    screen.blit(level_13_text, level_13_text.get_rect(topleft=(665, 333)))
    screen.blit(level_14_text, level_14_text.get_rect(topleft=(765, 333)))
    screen.blit(level_15_text, level_15_text.get_rect(topleft=(865, 333)))
    screen.blit(level_16_text, level_16_text.get_rect(topleft=(965, 333)))

    screen.blit(level_17_text, level_17_text.get_rect(topleft=(265, 433)))
    screen.blit(level_18_text, level_18_text.get_rect(topleft=(365, 433)))
    screen.blit(level_19_text, level_19_text.get_rect(topleft=(465, 433)))
    screen.blit(level_20_text, level_20_text.get_rect(topleft=(565, 433)))
    screen.blit(level_21_text, level_21_text.get_rect(topleft=(665, 433)))
    screen.blit(level_22_text, level_22_text.get_rect(topleft=(765, 433)))
    screen.blit(level_23_text, level_23_text.get_rect(topleft=(865, 433)))
    screen.blit(level_24_text, level_24_text.get_rect(topleft=(965, 433)))


    for (i, el) in enumerate(point):
        if el >= 1:
            screen.blit(points, (level_l_x[i] - 5, level_l_y[i] + 47))
        if el >= 2:
            screen.blit(points, (level_l_x[i] + 19, level_l_y[i] + 47))
        if el == 3:
            screen.blit(points, (level_l_x[i] + 43, level_l_y[i] + 47))

    l = 0 #level
    is1s = [] #index sky1
    is2s = [] #index sky2
    ex = 0 #exit x + 22
    ey = 560
    ig = [] #index ghost
    iax = [] #index axe x
    iay = []  # index axe y 630 420 190
    mx = [] #money x
    my = []  # money y 630 400 170
    gsx = [] #ghost sky x
    gsy = [] #ghost sky y
    cx = [] #cobweb_x
    cy = [] #cobweb_y
    bx = [] #broom_x
    by = [] #broom_y
    cfx = [] #coffin x
    cfy = [] #coffin y
    gjx = [] #ghost jump x
    hx = [] #helmet x
    hy = [] #helmrt y
    gjs = [] #ghost jump spavn

    mouse_menu = pygame.mouse.get_pos()
    if level_1_text.get_rect(topleft=(273, 233)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 1
        is1s = [1, 2, 3, 5, 6, 7, 11, 12]
        is2s = [2, 3, 4, 5, 13, 14]
        ex = 45
        ig = [10, 15, 20]
        iax = [1, 5, 6, 13, 16]
        iay = [640, 640, 420, 190, 640] #630 420 190
        mx = [4, 14, 7]
        my = [640, 190, 420] #630 420 190
        go_game = True
    elif level_2_text.get_rect(topleft=(373, 233)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 2
        is1s = [1, 2, 3, 4, 11, 12, 13, 17, 18]
        is2s = [12, 13, 14, 15]
        ex = 45
        ig = [8, 15, 20]
        iax = [1, 5, 13, 13, 16]
        iay = [640, 640, 420, 190, 640] #630 420 190
        mx = [4, 15, 17]
        my = [640, 190, 420] #630 420 190
        go_game = True
    elif level_3_text.get_rect(topleft=(473, 233)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 3
        is1s = [1, 2, 4, 6, 7, 13, 16, 18]
        is2s = [7, 8, 9, 20, 21]
        ex = 45
        ig = [10, 11, 15, 17, 20, 21]
        iax = [1, 2, 6, 9, 13, 16, 18, 21]
        iay = [420, 420, 640, 190, 420, 640, 420, 190] #630 420 190
        mx = [6, 12, 20]
        my = [420, 640, 190] #630 420 190
        go_game = True
    elif level_4_text.get_rect(topleft=(573, 233)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 4
        is1s = [1, 2, 3, 4, 5, 10, 11]
        is2s = [4, 5, 6]
        ex = 40
        iax = [1, 2, 3, 4, 5]
        iay = [640, 420, 420, 190, 640] #630 420 190
        mx = [5, 6, 10]
        my = [420, 190, 420] #630 420 190
        gsx = [10, 11]
        go_game = True
    elif level_5_text.get_rect(topleft=(673, 233)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 5
        is1s = [1, 2, 3, 4, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19]
        is2s = [6, 7, 8, 12, 13, 14, 15, 18]
        ex = 50
        iax = [1, 1, 12, 16, 19, 12, 13, 15]
        iay = [640, 420, 420, 420, 420, 190, 190, 190] #630 420 190
        mx = [6, 14, 18]
        my = [630, 190, 420] #630 420 190
        gsx = [15, 10, 17, 23]
        go_game = True
    elif level_6_text.get_rect(topleft=(773, 233)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 6
        is1s = [1, 2, 3, 4, 5, 8, 9, 12, 14, 15, 16, 21, 24, 25, 32, 35, 36, 37, 42, 44, 46, 47]
        is2s = [5, 6, 7, 8, 9, 16, 17, 24, 31, 39, 48, 50]
        ex = 75
        ig = [10, 14, 19, 25, 27, 40, 46, 50]
        iax = [2, 5, 9, 12, 15, 16, 32, 42, 47, 8, 17, 24, 50, 4, 7, 12, 23, 44, 47]
        iay = [420, 420, 420, 420, 420, 420, 420, 420, 420, 190, 190, 190, 190, 640, 640, 640, 640, 640, 640] #630 420 190
        mx = [48, 14, 34]
        my = [190, 420, 630] #630 420 190
        gsx = [12, 14, 23, 28, 32, 37, 45, 49]
        go_game = True
    elif level_7_text.get_rect(topleft=(873, 233)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 7
        is1s = [1, 3, 5, 7, 9, 11, 12, 13, 18, 19, 28, 29, 32, 45, 46, 47, 50, 51, 54]
        is2s = [13, 14, 15, 16, 20, 21, 27, 34, 37, 38, 39, 42, 43, 44, 52]
        ex = 80
        ig = [10, 14, 15, 22, 28, 34, 35, 38, 42, 44, 49, 55]
        iax = [5, 9, 11, 13, 19, 28, 45, 46, 50, 15, 20, 27, 37, 42, 44, 8, 11, 13, 27, 28, 47, 52]
        iay = [420, 420, 420, 420, 420, 420, 420, 420, 420, 190, 190, 190, 190, 190, 190, 640, 640, 640, 640, 640, 640, 640] #630 420 190
        mx = [34, 47, 9]
        my = [190, 420, 640] #630 420 190
        gsx = [15, 22, 27, 34, 43, 48]
        go_game = True
    elif level_8_text.get_rect(topleft=(973, 233)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 8
        is1s = [3, 8, 13, 16, 22, 35, 44, 45]
        is2s = [1, 4, 5, 14, 15, 24, 26, 27, 28, 47, 48]
        ex = 80
        ig = [13, 18, 33, 43, 51, 52]
        iax = [2, 10, 11, 14, 24, 25, 37, 46, 50, 54, 16, 35, 1, 4, 24, 28]
        iay = [] #630 420 190
        for i in range(10):
            iay.append(640)
        for i in range(2):
            iay.append(420)
        for i in range(4):
            iay.append(190)
        mx = [26, 45, 47]
        my = [190, 420, 190] #630 420 190
        gsx = [10, 11, 20, 29, 37, 50, 51]
        go_game = True
    elif level_9_text.get_rect(topleft=(273, 333)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 9
        is1s = [1, 5, 7, 12, 17, 19, 21, 23, 28, 32, 43, 55, 57, 59, 66, 67, 68, 69, 72, 73, 74]
        is2s = [13, 14, 27, 29, 30, 31, 49, 50, 51, 52, 53, 61, 62, 63, 64, 73, 74]
        ex = 100
        ig = [12, 17, 19, 20, 25, 26, 27, 31, 34, 36, 37, 39, 49, 51, 53, 57, 62, 64, 67, 68, 72, 73, 74]
        iax = [1, 3, 5, 6, 8, 9, 14, 15, 22, 23, 24, 28, 30, 33, 40, 42, 45, 47, 50, 52, 55, 59, 60, 63, 65, 70, 1, 7, 12, 17, 19, 21, 28, 43, 59, 66, 67, 68, 72, 73, 14, 30, 50, 51, 62, 74]
        iay = [] #630 420 190
        for i in range(26):
            iay.append(640)
        for i in range(14):
            iay.append(420)
        for i in range(6):
            iay.append(190)
        mx = [10, 31, 55]
        my = [640, 190, 420] #630 420 190
        gsx = [15, 18, 19, 24, 25, 26, 34, 38, 40, 48, 53, 55, 57, 63, 67, 70, 72, 73, 74]
        go_game = True

    elif level_10_text.get_rect(topleft=(365, 333)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 10
        is1s = [1, 2 ,6, 7, 9, 10, 11, 20, 21, 22, 26, 27, 28, 29]
        is2s = [7, 8, 13, 17, 18, 24, 25]
        ex = 60
        ig = [15, 22, 23, 28, 29]
        iax = [1, 4, 5, 6, 10, 13, 13, 17, 21, 24]
        iay = [420, 640, 640, 420, 420, 640, 190, 640, 420, 190] #640 420 190
        mx = [10, 17, 27]
        my = [640, 190, 420] #640 420 190
        gsx = [20, 24, 28]
        cx = [2, 9, 16, 18, 26, 28]
        cy = [380, 600, 600, 150, 600, 380] #600 380 150
        bx = [1, 8, 19]
        by = [640, 190, 640] #640 420 190
        go_game = True
    elif level_11_text.get_rect(topleft=(465, 333)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 11
        is1s = [1, 3, 8, 9, 10, 11, 13, 18, 19, 22, 28, 29, 30, 33, 34, 38, 39]
        is2s = [5, 6, 17, 62, 26, 27, 31, 37]
        ex = 70
        ig = [11, 15, 17, 19, 20, 25, 27, 31, 34, 36, 39]
        iax = [3, 4, 7, 8, 14, 18, 22, 24, 26, 32, 35, 37, 1, 9, 13, 19, 29, 38, 6, 17, 27]
        iay = [] #640 420 190
        for i in range(12):
            iay.append(640)
        for i in range(6):
            iay.append(420)
        for i in range(3):
            iay.append(190)
        mx = [11, 26, 34]
        my = [420, 190, 420] #640 420 190
        gsx = [15, 19, 20, 28, 29, 33, 37, 38, 39]
        cx = [2, 5, 12, 18, 22, 23, 30, 33]
        cy = [600, 190, 600, 380, 380, 600, 600, 380] #600 380 150
        bx = [3, 10, 21, 30]
        by = [420, 640, 640, 420] #640 420 190
        go_game = True
    elif level_12_text.get_rect(topleft=(565, 333)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 12
        is1s = [2, 3, 12, 13, 19, 20, 21, 27, 35, 36]
        is2s = [1, 5, 22, 23, 29, 30]
        ex = 70
        ig = [10, 23, 34, 41]
        iax = [1, 3, 3, 6, 23, 27, 29, 36, 37]
        iay = [640, 640, 420, 640, 190, 420, 640, 640, 640] #640 420 190
        mx = [16, 29, 36]
        my = [640, 190, 420] #640 420 190
        gsx = [19, 20, 33, 39, 43]
        cx = [9, 15, 20, 35]
        cy = [600, 600, 380, 380] #600 380 150
        bx = [13, 30]
        by = [420, 190] #640 420 190
        go_game = True
    elif level_14_text.get_rect(topleft=(765, 333)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 14
        is1s = [2, 3, 6, 7, 8, 14, 16, 18, 26, 27, 28]
        is2s = [1, 10, 11, 20, 22, 24, 29, 30]
        ex = 60
        ig = [15, 19, 20, 22, 26, 28]
        iax = [1, 4, 5, 10, 12, 14, 21, 23, 27, 30, 3, 14, 18, 20, 24, 29]
        iay = [] #640 420 190
        for i in range(10):
            iay.append(640)
        for i in range(3):
            iay.append(420)
        for i in range(3):
            iay.append(190)
        mx = [7, 11, 26]
        my = [420, 190, 420] #640 420 190
        gsx = [12, 13, 17, 18, 19, 23, 27]
        cx = [6, 10, 17, 22, 24, 28]
        cy = [600, 150, 600, 150, 600, 380] #600 380 150
        bx = [1, 16, 25]
        by = [190, 420, 640] #640 420 190
        cfx = [6, 8, 18]
        cfy = [380, 380, 610]  # 610 380 150
        go_game = True
    elif level_13_text.get_rect(topleft=(665, 333)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 13
        is1s = [1, 7, 8, 16, 17, 25, 30, 31, 32, 39]
        is2s = [10, 19, 26, 27]
        ex = 70
        ig = [10, 11, 34]
        iax = [1, 3, 4, 13, 19, 24, 1, 17, 25, 10, 19, 26]
        iay = [] #640 420 190
        for i in range(6):
            iay.append(640)
        for i in range(3):
            iay.append(420)
        for i in range(3):
            iay.append(190)
        mx = [8, 17, 32]
        my = [420, 640, 420] #640 420 190
        gsx = [14, 22, 35, 38]
        cx = [16, 30]
        cy = [380, 380] #600 380 150
        bx = [14, 29]
        by = [640, 640] #640 420 190
        cfx = [7, 27, 31]
        cfy = [380, 150, 380]  # 610 380 150
        go_game = True
    elif level_15_text.get_rect(topleft=(865, 333)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 15
        is1s = [1, 2, 3, 7, 8, 9, 10, 23, 26, 28, 29, 30, 31, 32, 36, 39, 40, 41, 47, 48, 49, 50]
        is2s = [2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 17, 18, 19, 23, 24, 31, 32, 33, 42, 48, 49]
        ex = 80
        ig = [10, 15, 22, 34, 37, 39, 46]
        iax = [1, 3, 6, 14, 15, 19, 23, 27, 36, 37, 42, 45, 47, 2, 7, 23, 28, 32, 40, 2, 6, 7, 19]
        iay = [640, 640, 640, 640, 640, 640, 640, 640, 640, 640, 640, 640, 640, 420, 420, 420, 420, 420, 420, 190, 190, 190, 190] #640 420 190
        mx = [14, 30, 42]
        my = [190, 630, 190] #640 420 190
        gsx = [13, 29, 43, 47]
        cx = [9, 12, 18, 26, 28, 34, 40, 48]
        cy = [600, 150, 150, 380, 150, 600, 380, 150] #600 380 150
        bx = [1, 8, 10, 36]
        by = [420, 640, 420, 420] #630 420 190
        cfx = [4, 13, 28, 31, 47]
        cfy = [150, 150, 610, 610, 380] #610 380 150
        go_game = True
    elif level_16_text.get_rect(topleft=(965, 333)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 16
        is1s = [4, 5, 13, 27, 30, 31, 38, 49, 50, 51, 52, 53, 54]
        is2s = [7, 8, 9, 14, 16, 18, 29, 37, 47, 52, 53, 55, 56]
        ex = 80
        ig = [19, 23, 26, 31, 32, 42, 46, 51, 54]
        iax = [1, 2, 3, 8, 11, 15, 18, 24, 29, 36, 40, 43, 45, 47, 50, 53, 56, 5, 13, 27, 31, 38, 49, 52, 54, 16, 18, 29, 47, 56]
        iay = [] #640 420 190
        for i in range(17):
            iay.append(640)
        for i in range(8):
            iay.append(420)
        for i in range(5):
            iay.append(190)
        mx = [9, 34, 53]
        my = [190, 640, 190] #640 420 190
        gsx = [14, 18, 23, 24, 31, 35, 42, 46, 51, 54, 55]
        cx = [4, 8, 27, 35, 44, 55]
        cy = [600, 150, 600, 600, 600, 150] #600 380 150
        bx = [14, 37, 49]
        by = [150, 150, 640] #640 420 190
        cfx = [7, 16, 33, 50]
        cfy = [150, 610, 610, 380]  # 610 380 150
        go_game = True
    elif level_17_text.get_rect(topleft=(265, 433)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 17
        is1s = [1, 9, 10, 18, 19, 20, 26, 31, 32, 33, 36, 37, 38, 39, 40, 41, 42, 48, 51, 54, 56, 59, 60, 61, 62, 64]
        is2s = [3, 5, 7, 8, 9, 11, 12, 13, 14, 23, 24, 35, 36, 37, 40, 41, 43, 44, 46, 50, 61, 62, 63]
        ex = 90
        ig = [13, 17, 21, 28, 32, 36, 41, 45, 48, 52, 60, 63]
        iax = [3, 7, 10, 11, 14, 16, 30, 33, 46, 53, 57, 62, 9, 19, 26, 36, 38, 41, 48, 54, 59, 64, 7, 8, 9, 14, 23, 35, 41, 43, 44, 50, 61, 63]
        iay = [] #640 420 190
        for i in range(12):
            iay.append(640)
        for i in range(10):
            iay.append(420)
        for i in range(12):
            iay.append(190)
        mx = [18, 36, 55]
        my = [420, 190, 640] #640 420 190
        gsx = [18, 24, 29, 31, 38, 39, 47, 51, 54, 62, 64]
        cx = [5, 10, 12, 24, 38, 42, 50, 56, 64]
        cy = [600, 380, 150, 600, 600, 380, 600, 380, 600] #600 380 150
        bx = [5, 20, 39, 47]
        by = [190, 640, 640, 640] #640 420 190
        cfx = [15, 20, 33, 37, 51, 58, 61]
        cfy = [610, 380, 380, 150, 380, 610, 380]  # 610 380 150
        go_game = True
    elif level_18_text.get_rect(topleft=(365, 433)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 18
        is1s = [2, 5, 6, 11, 12, 16, 17, 18, 19, 20, 21, 23, 28, 29, 30, 39, 42, 44, 48, 49, 50, 54, 55, 56, 57, 60, 61, 64, 65, 68, 70, 72, 75]
        is2s = [7, 8, 9, 17, 19, 20, 25, 26, 27, 32, 34, 36, 43, 50, 51, 52, 57, 58, 67, 68, 69, 76, 77]
        ex = 100
        ig = [14, 23, 27, 32, 38, 45, 49, 54, 56, 62, 66, 71, 75]
        iax = [3, 11, 15, 22, 26, 35, 36, 40, 47, 63, 64, 70, 74, 2, 6, 11, 12, 17, 21, 28, 29, 30, 39, 44, 50, 55, 57, 61, 68, 70, 75, 7, 9, 17, 20, 27, 32, 34, 52, 68, 69, 76]
        iay = [] #640 420 190
        for i in range(13):
            iay.append(640)
        for i in range(18):
            iay.append(420)
        for i in range(11):
            iay.append(190)
        mx = [26, 43, 65]
        my = [190, 640, 380] #640 420 190
        gsx = [20, 24, 25, 33, 36, 39, 46, 47, 55, 59, 64, 69, 72, 76, 77]
        cx = [5, 12, 16, 25, 25, 37, 52, 64, 72]
        cy = [600, 600, 380, 600, 150, 600, 600, 380, 600] #600 380 150
        bx = [7, 18, 46, 60]
        by = [640, 420, 640, 640] #640 420 190
        cfx = [9, 19, 33, 48, 58, 58, 67, 67, 77]
        cfy = [610, 380, 610, 380, 610, 150, 610, 150, 150]  # 610 380 150
        go_game = True
    elif level_19_text.get_rect(topleft=(465, 433)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 19
        is1s = [2, 3, 4, 6, 7, 8, 11, 12, 13, 16, 18, 20, 24, 25, 27, 29, 30, 31, 36, 38, 39, 40]
        is2s = [4, 5, 6, 9, 15, 23, 28, 29, 35, 38]
        ex = 70
        ig = [10, 15, 31, 38]
        iax = [1, 2, 6, 9, 11, 12, 16, 19, 20, 26, 32, 36, 2, 6, 12, 16, 24, 25, 29, 38, 39, 5, 6, 23, 29, 35]
        iay = [] #640 420 190
        for i in range(12):
            iay.append(640)
        for i in range(9):
            iay.append(420)
        for i in range(5):
            iay.append(190)
        mx = [15, 27, 33]
        my = [190, 420, 640] #640 420 190
        gsx = [17, 25, 31, 37, 39]
        cx = [7, 20, 27, 34, 36]
        cy = [600, 380, 600, 600, 380] #600 380 150
        bx = [9, 18, 25]
        by = [190, 420, 640] #640 420 190
        cfx = [8, 21, 31]
        cfy = [380, 610, 380]  # 610 380 150
        gjx = [13, 18, 23, 28, 29, 35]
        go_game = True
    elif level_20_text.get_rect(topleft=(565, 433)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 20
        is1s = [1, 2, 3, 8, 9, 10, 11, 12, 17, 19, 21, 23, 28, 29, 30, 35, 36, 40, 41, 42, 45, 47, 49, 51]
        is2s = [4, 6, 7, 8, 13, 14, 25, 26, 28, 30, 31, 33, 37, 38, 39, 52, 53]
        ex = 80
        ig = [10, 15, 23, 26, 33, 35, 39, 40, 41, 49]
        iax = [1, 2, 3, 4, 5, 7, 12, 16, 17, 18, 24, 25, 27, 28, 31, 32, 36, 37, 38, 43, 44, 45, 53, 1, 2, 9, 10, 17, 21, 35, 40, 49, 7, 8, 30, 33, 37]
        iay = [] #640 420 190
        for i in range(23):
            iay.append(640)
        for i in range(9):
            iay.append(420)
        for i in range(5):
            iay.append(190)
        mx = [12, 23, 52]
        my = [420, 420, 190] #640 420 190
        gsx = [17, 22, 23, 28, 33, 38, 44, 47, 50]
        cx = [6, 13, 14, 19, 21, 31, 36, 43, 47]
        cy = [150, 600, 600, 380, 600, 150, 380, 380, 600] #600 380 150
        bx = [4, 6, 25, 28, 30, 45]
        by = [190, 630, 190, 190, 630, 420] #630 420 190
        cfx = [11, 14, 28, 30, 39, 51, 53]
        cfy = [380, 150, 380, 380, 150, 610, 150] #610 380 150
        gjx = [19, 20, 29, 34, 42, 46, 50]
        go_game = True
    elif level_21_text.get_rect(topleft=(665, 433)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 21
        is1s = [2, 4, 10, 13, 17, 18, 19, 20, 21, 25, 27, 29, 33, 34, 35, 40, 43, 45, 46, 47, 50, 51, 53, 54, 58, 59, 60]
        is2s = [1, 6, 7, 8, 14, 15, 20, 21, 22, 28, 29, 30, 31, 32, 37, 38, 48, 49, 50, 54, 55, 56, 57]
        ex = 90
        ig = [12, 17, 25, 30, 35, 42, 44, 51, 55, 58]
        iax = [2, 3, 7, 9, 11, 16, 19, 23, 29, 34, 43, 49, 57, 2, 4, 17, 18, 25, 27, 29, 33, 34, 35, 40, 51, 59, 60, 1, 8, 14, 15, 21, 22, 29, 30, 32, 38, 49, 54, 57]
        iay = [] #640 420 190
        for i in range(13):
            iay.append(640)
        for i in range(14):
            iay.append(420)
        for i in range(13):
            iay.append(190)
        mx = [19, 31, 43]
        my = [420, 640, 420] #640 420 190
        gsx = [17, 19, 22, 28, 32, 37, 41, 47, 48, 53]
        cx = [5, 13, 22, 28, 39, 47, 53, 56]
        cy = [600, 380, 600, 150, 600, 380, 380, 600] #600 380 150
        bx = [6, 13, 21, 33]
        by = [190, 640, 420, 640] #640 420 190
        cfx = [10, 31, 36, 50, 52]
        cfy = [380, 150, 610, 150, 610]  # 610 380 150
        gjx = [15, 20, 21, 26, 32, 37, 41, 46, 50, 54]
        go_game = True
    elif level_22_text.get_rect(topleft=(765, 433)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 22
        is1s = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 23, 24, 25, 26, 27, 28, 29, 30]
        is2s = [6, 7, 8, 9, 10, 11, 27, 28, 29]
        ex = 60
        ig = [10, 11, 12, 13]
        iax = [5, 6, 7, 8, 9]
        iay = [] #640 420 190
        for i in range(5):
            iay.append(640)
        for i in range(0):
            iay.append(420)
        for i in range(0):
            iay.append(190)
        mx = [28, 29, 30]
        my = [640, 640, 640] #640 420 190
        gsx = [30]
        cx = []
        cy = [] #600 380 150
        bx = []
        by = [] #640 420 190
        cfx = []
        cfy = []  #610 380 150
        gjx = [30]
        hx = [1, 2, 3, 4, 6, 6, 7, 7]
        hy = [640, 640, 640, 640, 420, 190, 420, 190] #640 420 190
        gjs = [15]
        go_game = True
    elif level_23_text.get_rect(topleft=(865, 433)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 23
        is1s = [1, 2, 3, 11, 14, 16, 19, 21, 24, 25, 26, 27, 31, 32, 33, 34]
        is2s = [5, 6, 7, 13, 17, 18, 19, 27, 28, 36, 37, 38]
        ex = 60
        ig = [18, 26, 30, 38]
        iax = [5, 8, 9, 16, 19, 22, 34, 2, 11, 14, 32, 33, 6, 7, 28, 36, 38]
        iay = [] #640 420 190
        for i in range(7):
            iay.append(640)
        for i in range(5):
            iay.append(420)
        for i in range(5):
            iay.append(190)
        mx = [13, 26, 35]
        my = [640, 420, 640] #640 420 190
        gsx = [17, 24, 28, 32, 36]
        cx = [7, 16, 20, 31, 36]
        cy = [600, 380, 600, 380, 600] #600 380 150
        bx = [5, 13]
        by = [190, 190] #640 420 190
        cfx = [10, 21, 24, 34]
        cfy = [610, 380, 610, 380]  #610 380 150
        gjx = [17]
        hx = [3, 6, 19, 25, 31]
        hy = [420, 640, 190, 420, 640] #640 420 190
        gjs = [28]
        go_game = True
    elif level_24_text.get_rect(topleft=(965, 433)).collidepoint(mouse_menu) and pygame.mouse.get_pressed()[0]:
        l = 24
        is1s = [1, 2, 3, 9, 10, 11, 13, 14, 21, 22, 23, 29, 32, 34, 73, 38, 39, 42, 43, 44, 48]
        is2s = [5, 6, 7, 17, 19, 27, 36, 37, 45, 46, 47, 48]
        ex = 80
        ig = [20, 28, 38, 41]
        iax = [10, 13, 16, 26, 30, 40, 2, 3, 21, 32, 34, 44, 5, 19, 48]
        iay = [] #640 420 190
        for i in range(6):
            iay.append(640)
        for i in range(6):
            iay.append(420)
        for i in range(3):
            iay.append(190)
        mx = [9, 23, 33]
        my = [420, 420, 640] #640 420 190
        gsx = [13, 30, 35, 42]
        cx = [8, 14, 21, 29, 36, 44]
        cy = [600, 380, 600, 380, 600, 600] #600 380 150
        bx = [4, 6, 17]
        by = [640, 190, 190] #640 420 190
        cfx = [22, 35, 42]
        cfy = [380, 610, 380]  #610 380 150
        gjx = []
        hx = [6, 7, 24]
        hy = [640, 190, 640] #640 420 190
        gjs = [17]
        go_game = True

    if go_game:
        point_t = game(l, is1s, is2s, ex, ey, ig, iax, iay, mx, my, gsx, cx, cy, bx, by, cfx, cfy, gjx, hx, hy, gjs)
        while point_t == -2:
            point_t = game(l, is1s, is2s, ex, ey, ig, iax, iay, mx, my, gsx, cx, cy, bx, by, cfx, cfy, gjx, hx, hy, gjs)
        point[l-1] = point_t
        if point_t == -1:
            play_quit = True
        go_game = False

    if play_quit:
        break

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
            pygame.quit()
