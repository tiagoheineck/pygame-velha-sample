import py
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((600,400))
    screen.fill((200,200,200))
    pygame.draw.line(screen,(0,0,0),(0,133),(600,133),5)
    pygame.draw.line(screen,(0,0,0),(0,266),(600,266),5)    
    pygame.draw.line(screen,(0,0,0),(200,0),(200,400),5)    
    pygame.draw.line(screen,(0,0,0),(400,0),(400,400),5)    
    pygame.display.flip()

    jogador = 1
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
              mouse_position_x, mouse_position_y = pygame.mouse.get_pos() 
              if(mouse_position_x >= 0 and mouse_position_x <= 133
                and mouse_position_y >= 0 and mouse_position_y <= 200):
                    if (jogador == 1):
                        pygame.draw.circle(screen, (255,0,0),(200/2,130/2),20,100)
                        pygame.display.flip()
                        jogador = 2
                    else:
                        pygame.draw.rect(screen, (0,0,255),pygame.Rect(50,50,50,50))
                        pygame.display.flip()
                        jogador = 1

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__=="__main__":
    # call the main function
    main()