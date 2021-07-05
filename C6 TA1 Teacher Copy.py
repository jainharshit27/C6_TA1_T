import pygame

pygame.init()

screen = pygame.display.set_mode((400, 200))

game_over = input("Enter your name here: ")
go_font = pygame.font.Font("freesansbold.ttf", 16)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    go = go_font.render(game_over + ", your game is over", True, (0, 0, 0))
    screen.blit(go, (100, 90)) 
    
    pygame.display.update()