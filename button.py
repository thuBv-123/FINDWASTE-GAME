import pygame
# tạo lớp của các nút
class Button():
    def __init__(self,x,y, image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale))) # chia tỉ lệ cho phù hợp
        self.rect = self.image.get_rect() #lấy hình chữ nhật
        self.rect.topleft = (x,y)

    # tuy nhiên các nút vẫn ch hiện lên màn hình nên ta dùng phương thức vẽ lên nó:
        self.clicked = False # ban đầu sẽ chuột sẽ ở trạng thái không được CLICK


    def draw(self,surface)  :
        action = False


        #lấy vị trí chuột:
        pos = pygame.mouse.get_pos()
       
       # kiểm tra chuột và các điều kiện được nhấp chuột
        if self.rect.collidepoint(pos):
             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                  self.clicked = True
                  action = True
                  

        if pygame.mouse.get_pressed()[0] == 0:
             self.clicked = False       


        # vẽ nút lên màn hình
        surface.blit(self.image,(self.rect.x, self.rect.y))
        
        return action