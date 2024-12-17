import pygame
import os
import button




screen_height = 823
screen_width = 1472

screen = pygame.display.set_mode((screen_width, screen_height ))
pygame.display.set_caption('FIND OBJECTS GAME')

# tải ảnh các nút
start_img = pygame.image.load('images/start.img.png').convert_alpha()
exit_img = pygame.image.load('images/exit.img.png').convert_alpha()


# tạo các phiên bản nút
start_button =  button.Button(180,290, start_img,1)
exit_button =  button.Button(800,350, exit_img,1)
#tuy nhiên nó vẫn ch được hiện lên vì ta ch gọi phương thức vẽ lên chúng , ta sẽ tạo vòng lặp ở bước sau

background =pygame.image.load('images/Add a heading.png').convert_alpha()

run=True
while run:

    # vẽ nền mở đầu sau khi được tải ở trên
    screen.fill((202, 228, 241))  # lấp đầy nền đen bằng nền màu xanh nhạt
    if background: # nếu ta có background thì có thể thay thế vào nó
           screen.blit(background, (0,0))  # Draw the level background image

    # vẽ các nút đã khởi tạo ở trên vào màn hình:
    if start_button.draw(screen) == True: # gọi mã để vẽ
         print('START')
         
    if exit_button.draw(screen) :# vì ta đã tạo tọa độ cho nó trước đó nên bước này ko cần tạo
        run = False
        print('EXIT')


            



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                run =   False


    pygame.display.update()



pygame.quit()