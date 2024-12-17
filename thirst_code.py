import pygame
from pygame.mask import from_surface

pygame.init()
pygame.mixer.init()
#tạo khung trò chơi
screen_height = 823
screen_width = 1472
display_time=100
screen = pygame.display.set_mode((screen_width, screen_height ))
pygame.display.set_caption('FIND OBJECTS GAME')
# Biến trò chơi
game_paused = False
#định nghĩa phông chữ
font =  pygame.font.SysFont('arialblack',40)
# định nghĩa màu chữ
TEXT_COL = (255,255,255)
# đặt văn bản vào màn hình
def draw_text(text,font,text_col,x,y):
     img = font.render(text, True, text_col)
     screen.blit(img,(x,y))
# tải âm thanh, nhạc nền:
music_background = pygame.mixer.music.load('sounds/puzzle-game-bright-casual-video-game-music-249202.mp3')
transition_sound = pygame.mixer.Sound('sounds/purchase-succesful-ingame-230550.mp3')
pick_up_sound = pygame.mixer.Sound('sounds/pick_up_sound.mp3')
false_sound = pygame.mixer.Sound('sounds/false.mp3')
win_sound = pygame.mixer.Sound('sounds/nhạc chiến thắng.mp3')
sowing_sound = pygame.mixer.Sound('sounds/gieo hò chiến thắng.wav')
win2_sound = pygame.mixer.Sound('sounds/sound chiến thắng.wav')
game_over_sound = pygame.mixer.Sound('sounds/nhạc thua cuộc.wav')
pygame.mixer.music.play(-1)  
pygame.mixer.music.set_volume(1.6)
# tải ảnh các nút
start_img = pygame.image.load('images/start.png').convert_alpha()
exit_img = pygame.image.load('images/exit.img.png').convert_alpha()
return_img = pygame.image.load('images/return_button.png').convert_alpha()
level1_img = pygame.image.load('images/level1.png').convert_alpha()
level2_img = pygame.image.load('images/level2.png').convert_alpha()
level3_img = pygame.image.load('images/level3.png').convert_alpha()
level4_img = pygame.image.load('images/level4.png').convert_alpha()
level5_img = pygame.image.load('images/level5.png').convert_alpha()
replay_img = pygame.image.load('images/replay_button.png').convert_alpha()
home_img = pygame.image.load('images/home_button.png').convert_alpha()
continue_img = pygame.image.load('images/next_button.png').convert_alpha()
# tải ảnh đồ vật trong game
thùng_rác_thực_phẩm_img = pygame.image.load('images/thùng rác thực phẩm.png').convert_alpha()
thùng_rác_tái_chế_img = pygame.image.load('images/thùng rác tái chế.png').convert_alpha()
thùng_rác_khác_img = pygame.image.load('images/thùng rác các loại rác khác.png').convert_alpha()
nắp_thùng_rác_tp_img = pygame.image.load('images/nắp thùng rác tp.png').convert_alpha()
nắp_thùng_rác_tc_img = pygame.image.load('images/nắp thùng rác tc.png').convert_alpha()
nắp_thùng_rác_khác_img = pygame.image.load('images/nắp thùng rác khác.png').convert_alpha()
garbage_bags_img =  pygame.image.load('images/garbage bags.png').convert_alpha()
bánh_mì_img =  pygame.image.load('images/bánh mì.png').convert_alpha()
bình_cồn_y_tế_img = pygame.image.load('images/bình cồn y tế .png').convert_alpha()
cục_xà_phòng_img= pygame.image.load('images/cục xà phòng.png').convert_alpha()
chai_mứt_img = pygame.image.load('images/chai mứt.png').convert_alpha()
kem_ốc_quế_img = pygame.image.load('images/kem ốc quế.png').convert_alpha()
kem_ốc_quế_2_img= pygame.image.load('images/kem ốc quế 2.png').convert_alpha()
kem_tràng_tiền_img= pygame.image.load('images/kem tràng tiền.png').convert_alpha()
phô_mai_img= pygame.image.load('images/phô mai.png').convert_alpha()
trứng_vịt_img= pygame.image.load('images/trứng vịt.png').convert_alpha()
trứng_img= pygame.image.load('images/trứng.png').convert_alpha()
vỉ_thuốc_img= pygame.image.load('images/vỉ thuốc.png').convert_alpha()
vỉ_trứng_img= pygame.image.load('images/vỉ trứng.png').convert_alpha()

# lớp các đồ vật trong level
class Object():
    def __init__(self,x,y, img,scale):
        #lấy tọa độ ban đầu của vật để có thể replay
        self.start_x = x
        self.start_y = y
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img,(int(width*scale),int(height*scale))) # chia tỉ lệ cho phù hợp
        self.rect = self.image.get_rect() #lấy hình chữ nhật
        self.rect.topleft = (x,y)
        self.mask = from_surface(self.image)
    # tuy nhiên các nút vẫn ch hiện lên màn hình nên ta dùng phương thức vẽ lên nó:
        self.clicked = False # ban đầu sẽ chuột sẽ ở trạng thái không được CLICK
        self.sound_played = False  
    def draw(self):
        moving = False
         #lấy vị trí chuột:
        screen.blit(self.image,(self.rect.x, self.rect.y))  
        return moving
# tạo đồ vật trong trò chơi:
thùng_rác_thực_phẩm = Object(1280,20, thùng_rác_thực_phẩm_img, 0.7)
thùng_rác_tái_chế = Object(1280,290, thùng_rác_tái_chế_img, 0.68)
thùng_rác_khác = Object(1285,565, thùng_rác_khác_img, 0.66)
nắp_thùng_rác_tp = Object(1331,25, nắp_thùng_rác_tp_img, 0.15)
nắp_thùng_rác_tc = Object(1328,293, nắp_thùng_rác_tc_img, 0.15)
nắp_thùng_rác_khác = Object(1330,569, nắp_thùng_rác_khác_img, 0.15)
garbage_bags = Object(1000,569, garbage_bags_img , 0.5)
bánh_mì =  Object(1000,569, bánh_mì_img , 0.5)
bình_cồn_y_tế = Object(1000,569, bình_cồn_y_tế_img , 0.5)
cục_xà_phòng= Object(1000,569, cục_xà_phòng_img , 0.5)
chai_mứt = Object(1000,569, chai_mứt_img , 0.5)
kem_ốc_quế = Object(1000,569, kem_ốc_quế_img , 0.5)
kem_ốc_quế_2 = Object(1000,569, kem_ốc_quế_2_img, 0.5)
kem_tràng_tiền= Object(1000,569, kem_tràng_tiền_img , 0.5)
phô_mai= Object(1000,569, phô_mai_img , 0.5)
trứng_vịt= Object(1000,569, trứng_vịt_img , 0.5)
trứng= Object(1000,569, trứng_img , 0.5)
vỉ_thuốc= Object(1000,569, vỉ_thuốc_img , 0.5)
vỉ_trứng= Object(1000,569, vỉ_trứng_img , 0.5)

# danh sách rác thải thực phẩm:
fish_bone = pygame.image.load('images/fish bone.png').convert_alpha()
apple_core =  pygame.image.load('images/apple core.png').convert_alpha()
banana_peel =  pygame.image.load('images/banana peel.png').convert_alpha()
bánh_mì_mốc =  pygame.image.load('images/bánh mì mốc.png').convert_alpha()
bánh_mì_thừa =  pygame.image.load('images/bánh mì thừa.png').convert_alpha()
bánh_quy_thừa =  pygame.image.load('images/bánh quy thừa.png').convert_alpha()
cà_rốt_thừa =  pygame.image.load('images/cà rốt thừa.png').convert_alpha()
đùi_gà_thừa=  pygame.image.load('images/đùi gà thừa.png').convert_alpha()
lá_rau =  pygame.image.load('images/lá rau.png').convert_alpha()
ngũ_cốc_hết_hạn =  pygame.image.load('images/ngũ cốc hết hạn.png').convert_alpha()
những_bánh_mì_mốc=  pygame.image.load('images/những bánh mì mốc.png').convert_alpha()
vỏ_dưa_hấu =  pygame.image.load('images/vỏ dưa hấu.png').convert_alpha()
vỏ_táo =  pygame.image.load('images/vỏ táo.png').convert_alpha()
pizza_thừa = pygame.image.load('images/pizza thừa.png').convert_alpha()
#danh sách rác thải tái chế:
can =  pygame.image.load('images/can.png').convert_alpha()
oil_tank =  pygame.image.load('images/oil tank.png').convert_alpha()
milk_bottles =  pygame.image.load('images/milk bottles.png').convert_alpha()
plastic_bottle =  pygame.image.load('images/plastic bottles.png').convert_alpha()
bình_thủy_tinh =  pygame.image.load('images/bình thủy tinh.png').convert_alpha()
cốc_nước_thừa =  pygame.image.load('images/cốc nước thừa.png').convert_alpha()git
cốc_nhựa =  pygame.image.load('images/cốc nhựa.png').convert_alpha()
cốc_nhựa_2 =  pygame.image.load('images/cốc nhựa2.png').convert_alpha()
chai_nước_khoáng =  pygame.image.load('images/chai nước khoáng.png').convert_alpha()
chai_rượu =  pygame.image.load('images/chai rượi.png').convert_alpha()
hộp_sữa_không =  pygame.image.load('images/hộp sữa không.png').convert_alpha()
hộp_thiếc =  pygame.image.load('images/hộp thiếc.png').convert_alpha()
lõi_giấy =  pygame.image.load('images/lõi giấy.png').convert_alpha()
sách_cũ =  pygame.image.load('images/sách cũ.png').convert_alpha()
xấp_giấy_cũ =  pygame.image.load('images/sấp giấy cũ.png').convert_alpha()
thư_tay =  pygame.image.load('images/thư tay.png').convert_alpha()
vụn_kính=  pygame.image.load('images/vụn kính.png').convert_alpha()
trà_sữa = pygame.image.load('images/trà sữa thái xanh.png').convert_alpha()
thùng_xốp = pygame.image.load('images/thùng xốp.png').convert_alpha()
#danh sách các rác thải khác:
old_toothbrush = pygame.image.load('images/bàn chải cũ.png').convert_alpha()
lighter = pygame.image.load('images/bật lửa .png').convert_alpha()
bọc_thuốc_hỏng = pygame.image.load('images/bọc thuốc hỏng.png').convert_alpha()
bình_xịt_côn_trùng = pygame.image.load('images/bình xịt côn trùng.png').convert_alpha()
bóng_đèn_vỡ= pygame.image.load('images/bóng đèn vỡ.png').convert_alpha()
bông_tẩy_trang = pygame.image.load('images/bông tẩy trang.png').convert_alpha()
cành_cây_khô = pygame.image.load('images/cành cây khô.png').convert_alpha()
chai_xịt_tóc_cũ= pygame.image.load('images/chai xịt tóc cũ.png').convert_alpha()
dép = pygame.image.load('images/dép mất.png').convert_alpha()
hạt_đậu_thừa = pygame.image.load('images/hạt đậu thừa.png').convert_alpha()
vỏ_hạt_óc_chó = pygame.image.load('images/hạt óc chó thừa.png').convert_alpha()
kẹo_hết_hạn = pygame.image.load('images/kẹo hết hạn.png').convert_alpha()
kim_tiêm = pygame.image.load('images/kim tiêm .png').convert_alpha()
khăn_ướt = pygame.image.load('images/khăn ướt.png').convert_alpha()
khẩu_trang_hỏng = pygame.image.load('images/khẩu trang hỏng.png').convert_alpha()
khẩu_trang_cũ = pygame.image.load('images/khẩu trang cũ.png').convert_alpha()
ống_hút = pygame.image.load('images/ống hút.png').convert_alpha()
phân_đv = pygame.image.load('images/phân động vật.png').convert_alpha()
que_diêm = pygame.image.load('images/que diêm.png').convert_alpha()
tã_em_bé = pygame.image.load('images/tã em bé.png').convert_alpha()
than = pygame.image.load('images/than.png').convert_alpha()
trứng_vỡ = pygame.image.load('images/trững vỡ.png').convert_alpha()
vỉ_thuốc_hỏng = pygame.image.load('images/vỉ thuốc hỏng.png').convert_alpha()
vỉ_thuốc_không = pygame.image.load('images/vỉ thuốc không.png').convert_alpha()
vỏ_bim_bim = pygame.image.load('images/vỏ bim bim.png').convert_alpha()
vỏ_trứng = pygame.image.load('images/vỏ trứng.png').convert_alpha()
vỏ_pin = pygame.image.load('images/vỏ pin.png').convert_alpha()
vỏ_bình_cồn = pygame.image.load('images/vỏ bình cồn.png').convert_alpha()

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
        self.sound_played = False
    def draw(self)  :
        action = False
        #lấy vị trí chuột:
        pos = pygame.mouse.get_pos()       
       # kiểm tra chuột và các điều kiện được nhấp chuột
        if self.rect.collidepoint(pos):
             if pygame.mouse.get_pressed()[0] == 1 and not self.clicked :
                  self.clicked = True
                  action = True
                  if not self.sound_played:
                       transition_sound.play()
                       transition_sound.set_volume(0.8)
                       self.sound_played = True
        if pygame.mouse.get_pressed()[0] == 0:
             self.clicked = False       
             self.sound_played = False
        # vẽ nút lên màn hình
        screen.blit(self.image,(self.rect.x, self.rect.y))       
        return action
# tạo các phiên bản nút
start_button =  Button(1040,700, start_img,1.5)
exit_button =  Button(1110,600, exit_img,1)
return_button =  Button(-20,-20, return_img,0.15)
level1_button = Button(770,70 ,level1_img,1)
level2_button = Button(1150,180,level2_img,1)
level3_button = Button(780,280,level3_img,1)
level4_button = Button(1160,380,level4_img,1)
level5_button = Button(770,480,level5_img,1)
replay_button = Button(690,600,replay_img, 0.7)
home_button = Button(480,600,home_img,0.08)
continue_button = Button(770,480,continue_img,1)
#tuy nhiên nó vẫn ch được hiện lên vì ta ch gọi phương thức vẽ lên chúng , ta sẽ tạo vòng lặp ở bước sau
# tải các background
background =pygame.image.load('images/Add a healing.png').convert_alpha()
background_menu_level = pygame.image.load('images/background_menu_level.png').convert_alpha()
background_level_1 = pygame.image.load('images/green_study.png').convert_alpha()
background_level_2 = pygame.image.load('images/bàn học.png').convert_alpha()
background_level_3 = pygame.image.load('images/hành lang.png').convert_alpha()
background_level_4 = pygame.image.load('images/phòng ngủ.png').convert_alpha()
background_level_5 = pygame.image.load('images/thư viện.png').convert_alpha()
win_background = pygame.image.load('images/win_background2.png').convert_alpha()
game_over_background =  pygame.image.load('images/game_over.png').convert_alpha()
# xử lý trò chơi
class Game:
     def __init__(self):
        pygame.init()
        #tạo các danh sách phân theo các loại rác
        # danh sách rác hữa cơ
        self.organic_wastes_level_1 = [
             Object(736,395, apple_core, 1.4),Object(300,700, banana_peel, 1),
             Object(300,720, fish_bone, 0.06)
                   ]
        #danh sách rác tái chế
        self.Recycled_Waste_level_1 = [
             Object(40,480, milk_bottles, 1.6),Object(900,700, oil_tank, 1),
             Object(355,663, can, 1),Object(824,634, plastic_bottle, 0.7)
                   ]
        #danh sách rác không thuộc hai nhóm trên
        self.other_waste_level_1 = [
             Object(76,682, old_toothbrush , 0.2),Object(1126,406, lighter, 0.1)     
                   ]
        self.organic_wastes_level_2 = [
             Object(347,608,bánh_mì_mốc, 0.4),Object(532,666, bánh_quy_thừa, 0.3),
             Object(646,692, apple_core, 1.5),Object(668,738, vỏ_táo, 0.06)
                   ]
        #danh sách rác tái chế
        self.Recycled_Waste_level_2 = [
             Object(1035,665, cốc_nước_thừa, 0.4),Object(392,522,chai_nước_khoáng, 0.3),
             Object(859,730,sách_cũ, 0.5),Object(13,603, plastic_bottle, 1)
                   ]
        #danh sách rác không thuộc hai nhóm trên
        self.other_waste_level_2 = [
             Object(249,639, khăn_ướt , 0.2),Object(748,611, hạt_đậu_thừa, 0.15)     
                   ]
        self.organic_wastes_level_3 = [
             Object(432,605,bánh_mì_thừa, 0.07),Object(800,730, banana_peel,0.8),
             Object(300,720, pizza_thừa, 0.1),Object(274,727, fish_bone, 0.03)
                   ]
        #danh sách rác tái chế
        self.Recycled_Waste_level_3 = [
             Object(1024,631, can, 0.4),Object(64,658,chai_nước_khoáng, 0.15),
             Object(759,560, plastic_bottle, 0.3),Object(576,749,lõi_giấy, 0.2)   
                   ]
        #danh sách rác không thuộc hai nhóm trên
        self.other_waste_level_3 = [
            Object(878,587, lighter, 0.08),Object(540,701,vỏ_bình_cồn, 0.2),
             Object(543,573,bình_xịt_côn_trùng, 0.12),Object(100,550,bọc_thuốc_hỏng, 0.08),Object(554,648,cành_cây_khô, 0.2),Object(399,597,kim_tiêm, 0.1)
               
                   ]
        self.organic_wastes_level_4 = [
             Object(1096,575,bánh_mì_mốc, 0.2),Object(42,290, cà_rốt_thừa, 0.16),
             Object(735,465, pizza_thừa, 0.12),Object(300,200, lá_rau, 0.18),Object(816,484, vỏ_dưa_hấu, 0.11)
                   ]
        #danh sách rác tái chế
        self.Recycled_Waste_level_4 = [
             Object(623,419, cốc_nhựa, 0.15),Object(22,620,chai_nước_khoáng, 0.2),
             Object(450,720, cốc_nhựa_2, 0.15),Object(97,711,lõi_giấy, 0.17) , Object(152,674,chai_rượu, 0.2),Object(849,335,trà_sữa, 0.2) 
                   ]
        #danh sách rác không thuộc hai nhóm trên
        self.other_waste_level_4 = [
            Object(478,410, vỏ_bim_bim, 0.2),Object(696,644,ống_hút, 0.1),
             Object(35,770,bình_xịt_côn_trùng, 0.2),Object(200,360,bọc_thuốc_hỏng, 0.09),Object(520,720,phân_đv, 0.08),Object(12,484,tã_em_bé, 0.13),
             Object(1020,500,khẩu_trang_hỏng, 0.13)
                  ]
        self.organic_wastes_level_5 = [
             Object(468,744,bánh_quy_thừa, 0.18),Object(314,617, đùi_gà_thừa, 0.18),
             Object(370,608, pizza_thừa, 0.1),Object(150,616, những_bánh_mì_mốc, 0.2),Object(974,739, vỏ_táo, 0.2),Object(335,582, ngũ_cốc_hết_hạn, 0.14)
                   ]
        #danh sách rác tái chế
        self.Recycled_Waste_level_5= [
             Object(405,713, xấp_giấy_cũ, 0.17),Object(1064,571,chai_nước_khoáng, 0.15),
             Object(410,567, cốc_nhựa_2, 0.12),Object(-20,750,thùng_xốp, 0.6) , Object(988,654,chai_rượu, 0.18),Object(345,750,hộp_thiếc, 0.12),
             Object(535,620,hộp_sữa_không, 0.07)  
                   ]
        #danh sách rác không thuộc hai nhóm trên
        self.other_waste_level_5 = [
            Object(530,573, vỏ_bim_bim, 0.1),Object(134,110,bóng_đèn_vỡ, 0.1),
             Object(669,765,bông_tẩy_trang, 0.11),Object(835,716,chai_xịt_tóc_cũ, 0.14),Object(512,760,vỏ_hạt_óc_chó, 0.1),Object(665,625,vỏ_pin, 0.07),
             Object(882,770,kẹo_hết_hạn, 0.1),Object(470,678,than, 0.12),Object(464,692,que_diêm, 0.1),Object(254,625,khẩu_trang_cũ, 0.12)
                  ]
        #làm mờ background khi thắng hoặc thua
        self.overlay_surface = pygame.Surface((screen_width, screen_height))  # Create a surface for the overlay
        self.overlay_surface.fill((0, 0, 0))  # Fill it with black color
        self.overlay_surface.set_alpha(150)  # Set the transparency (0 is fully transparent, 255 is fully opaque)
        #các biến ở trạng thái ban đầu
        self.moving = False
        self.level = 0
        self.game_paused = False
        self.game_won = False
        self.game_over = False
        # đồ vật khác trong trò chơi
        self.objects = [
            thùng_rác_thực_phẩm,
            thùng_rác_tái_chế,
            thùng_rác_khác,
            nắp_thùng_rác_tp,
            nắp_thùng_rác_tc,
            nắp_thùng_rác_khác,
            garbage_bags,bánh_mì,bình_cồn_y_tế,cục_xà_phòng,chai_mứt,kem_ốc_quế,kem_ốc_quế_2,kem_tràng_tiền,phô_mai,trứng_vịt,trứng,vỉ_thuốc,vỉ_trứng
               ]
        # tạo các level
        self.levels =  {
             0: {
                'objects': [],
                'background': background,  # Menu background (replace 'background' with actual image)
                'win_condition': lambda: False ,
                'game_over_condition':lambda: False # No win condition for menu level
              },
            1:{
               'objects':self.organic_wastes_level_1 + self.Recycled_Waste_level_1 +  self.other_waste_level_1,
               'background':background_level_1,
               'win_condition': lambda: all (obj.rect.x < 0 and obj.rect.y < 0 for obj in self.levels[self.level]['objects']),
               'game_over_condition': lambda:sum(1 for obj in self.levels[self.level]['objects'] if obj.rect.x > 1900 and obj.rect.y > 1900) == 3
        
              },
            2:{
               'objects': self.organic_wastes_level_2 + self.Recycled_Waste_level_2 +  self.other_waste_level_2,
               'background':background_level_2,
               'win_condition': lambda: all(obj.rect.x < 0 and obj.rect.y < 0 for obj in self.levels[self.level]['objects']),
               'game_over_condition': lambda: sum(1 for obj in self.levels[self.level]['objects'] if obj.rect.x > 1900 and obj.rect.y > 1900) == 3
        
              },
            3:{
               'objects': self.organic_wastes_level_3 + self.Recycled_Waste_level_3 +  self.other_waste_level_3,
               'background':background_level_3,
               'win_condition': lambda: all(obj.rect.x < 0 and obj.rect.y < 0 for obj in self.levels[self.level]['objects']),
               'game_over_condition': lambda: sum(1 for obj in self.levels[self.level]['objects'] if obj.rect.x > 1900 and obj.rect.y > 1900) == 3
        
              },
            4:{
               'objects': self.organic_wastes_level_4 + self.Recycled_Waste_level_4 +  self.other_waste_level_4,
               'background':background_level_4,
               'win_condition': lambda: all(obj.rect.x  < 0 and obj.rect.y < 0 for obj in self.levels[self.level]['objects']),
               'game_over_condition': lambda: sum(1 for obj in self.levels[self.level]['objects'] if obj.rect.x > 1900 and obj.rect.y > 1900) == 3
        
              },
            5:{
               'objects': self.organic_wastes_level_5 + self.Recycled_Waste_level_5 +  self.other_waste_level_5,
               'background':background_level_5,
               'win_condition': lambda: all(obj.rect.x < 0 and obj.rect.y < 0 for obj in self.levels[self.level]['objects']),
               'game_over_condition': lambda: sum(1 for obj in self.levels[self.level]['objects'] if obj.rect.x > 1900 and obj.rect.y > 1900) == 3
        
              }
            } 
        # lập thư viện các nút                  
        self.buttons = {
             'start' :start_button,
             'exit' :exit_button,
             'return' :return_button,
             'level1' :level1_button,
             'level2' :level2_button,
             'level3' :level3_button,
             'level4' :level4_button,
             'level5' :level5_button,
             'replay' :replay_button,
             'home' :home_button,
             'continue' :continue_button
        }
     # hàm quay lại level nếu người chơi nhấp'replay'   
     def reset_level(self):
        for obj in self.levels[self.level]['objects']:
            obj.rect.x = obj.start_x
            obj.rect.y = obj.start_y 
        if self.level > 0 and not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1, 0.0)    
     # hàm xửa lý level( làm cho các level chạy)
     def handle_level(self):
        self.moving_obj = None
        screen.blit( self.levels[self.level]['background'], (0, 0))      
        # xử lý điều kiện giữa các obj:
        for obj in  self.levels[self.level]['objects']:
            obj.draw()
            # tại level 1
            if obj in self.organic_wastes_level_1:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)
            if obj in self.Recycled_Waste_level_1:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = -100
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
            if obj in self.other_waste_level_1:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)  
             # tại level 2           
            if obj in self.organic_wastes_level_2:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)
            if obj in self.Recycled_Waste_level_2:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = -100
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
            if obj in self.other_waste_level_2:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)
              # tại level3          
            if obj in self.organic_wastes_level_3:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)
            if obj in self.Recycled_Waste_level_3:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = -100
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
            if obj in self.other_waste_level_3:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)                   
            #tại level 4
            if obj in self.organic_wastes_level_4:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)
            if obj in self.Recycled_Waste_level_4:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = -100
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
            if obj in self.other_waste_level_4:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)
            # tại level 5
            if obj in self.organic_wastes_level_5:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)
            if obj in self.Recycled_Waste_level_5:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = -100
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = 2000 
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
            if obj in self.other_waste_level_5:    
                if obj.rect.colliderect(nắp_thùng_rác_tp.rect):
                    offset = (nắp_thùng_rác_tp.rect.x - obj.rect.x, nắp_thùng_rác_tp.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tp.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1)   
                elif obj.rect.colliderect(nắp_thùng_rác_tc.rect):
                    offset = (nắp_thùng_rác_tc.rect.x - obj.rect.x, nắp_thùng_rác_tc.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_tc.mask, offset):
                        obj.rect.x = 2000
                        obj.rect.y = 2000
                        false_sound.play()
                        false_sound.set_volume(1) 
                elif obj.rect.colliderect(nắp_thùng_rác_khác.rect):
                    offset = (nắp_thùng_rác_khác.rect.x - obj.rect.x, nắp_thùng_rác_khác.rect.y - obj.rect.y)
                    if obj.mask.overlap(nắp_thùng_rác_khác.mask, offset):
                        obj.rect.x = -100 
                        obj.rect.y = -100
                        pick_up_sound.play()
                        pick_up_sound.set_volume(1)  
        #kiểm tra điều kiện thắng                          
        if self.check_win_condition():
            self.game_won = True   
        # kiểm tra điều kiện thua    
        if self.check_game_over_condition():
            self.game_over = True
        # nếu thua:    
        if self.game_over:
            screen.blit(self.overlay_surface, (0, 0))
            screen.blit(game_over_background, (-10, -30))
            pygame.mixer.music.stop()
            game_over_sound.play()
            # nếu nhấn nút 'replay'
            if self.buttons['replay'].draw():
                self.game_over = False
                game_over_sound.stop()
                pygame.mixer.music.stop()
                self.reset_level()
                return True 
            # nếu nhấn nút 'home'
            if self.buttons['home'].draw():
                self.game_over = False
                self.game_paused = True
                game_over_sound.stop()
                pygame.mixer.music.stop()
                self.draw_menu()
                return True
        # nếu thắng (cũng tương tự như thua):
        if self.game_won : 
            screen.blit(self.overlay_surface, (0, 0))
            screen.blit(win_background, (-10, -30))
            sowing_sound.play()
            sowing_sound.set_volume(1) 
            win2_sound.play()
            win2_sound.set_volume(1)  
            win_sound.play()
            win_sound.set_volume(1) 
            pygame.mixer.music.stop()
            if self.buttons['replay'].draw():
                self.game_won = False
                sowing_sound.stop()
                win2_sound.stop()
                win_sound.stop()
                pygame.mixer.music.stop()
                self.reset_level()
                return True 
            if self.buttons['home'].draw():
                self.game_won = False
                self.game_paused = True
                sowing_sound.stop()
                win2_sound.stop()
                win_sound.stop()
                pygame.mixer.music.stop()
                self.draw_menu()
            if self.buttons['continue'].draw():
                self.game_won = False
                sowing_sound.stop()
                win2_sound.stop()
                win_sound.stop()
                pygame.mixer.music.stop()
                self.next_level()
                return True   
        return False
     # điều kiện thua:
     def check_game_over_condition(self):
        return self.levels[self.level]['game_over_condition']()   
     #điều kiện thắng
     def check_win_condition(self):
        return self.levels[self.level]['win_condition']()
     # hàm xảy ra nếu nhấn vào nút ' next'
     def next_level(self):
        # tất cả các vật trong level mới ở vị trí ban đầu:
        for obj in self.levels[self.level]['objects']:
            obj.rect.x = obj.start_x
            obj.rect.y = obj.start_y 
        # thêm điều kiện để nhạc nền chạy    
        if self.level > 0 and not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1, 0.0) 
        # dịch chuyển qua level mới    
        if self.level < len(self.levels) - 1:
            self.level += 1
            self.game_paused = False
            self.update_timer()
        else:
            print('Alrealy at the last level!')  
     # vẽ menu trò chơi  
     def draw_menu(self):
             if not pygame.mixer.music.get_busy():
                 pygame.mixer.music.play(-1, 0.0)
             screen.blit(background_menu_level, (0, 0))
             # vẽ nút quay lại màn hình chính
             if self.buttons['return'].draw():
                 self.game_paused = False
                 self.level = 0
             # vẽ nút vào level1,2,3,4,5
             if self.buttons['level1'].draw():
                self.game_paused = False
                self.level = 1
                for obj in self.levels[self.level]['objects']:
                    obj.rect.x = obj.start_x
                    obj.rect.y = obj.start_y 
             if self.buttons['level2'].draw():
                self.game_paused = False
                self.level = 2
                for obj in self.levels[self.level]['objects']:
                    obj.rect.x = obj.start_x
                    obj.rect.y = obj.start_y  
             if self.buttons['level3'].draw():
                self.game_paused = False
                self.level = 3
                for obj in self.levels[self.level]['objects']:
                    obj.rect.x = obj.start_x
                    obj.rect.y = obj.start_y   
             if self.buttons['level4'].draw():
                self.game_paused = False
                self.level = 4
                for obj in self.levels[self.level]['objects']:
                    obj.rect.x = obj.start_x
                    obj.rect.y = obj.start_y  
             if self.buttons['level5'].draw():
                self.game_paused = False
                self.level = 5
                for obj in self.levels[self.level]['objects']:
                    obj.rect.x = obj.start_x
                    obj.rect.y = obj.start_y 
             # vẽ nút play để bắt đầu chơi từ level 1                            
             if self.level == 0 and self.buttons['start'].draw():
                 self.game_paused = False
                 self.level = 1   
     # hàm vẽ khác                
     def draw(self):
        if not self.game_paused:
            self.handle_level()  # Handle the level logic
        else:
            self.draw_menu()  # Draw the pause menu

      # Handle button clicks (make sure you're interacting with Button objects)
        for button in self.buttons.values():
            button.draw()  # Each button will draw itself and handle mouse click checks
         
                      
     if game_paused:
          # hiện ra menu
        screen.blit(background_menu_level,(0,0))
        level = 0
        game_won = False
        
        draw_menu()
# chạy game
def main():
        game = Game()
        while True:
            game.draw()
            if game.level == 0 :
                if background_menu_level: # nếu ta có background thì có thể thay thế vào nó
                    screen.blit(background_menu_level, (0,0))  # Draw the level background image
            if game.level > 0:   
                game.game_paused = False
                screen.fill((0, 0 ,0))
                thùng_rác_khác.draw()  
                thùng_rác_tái_chế.draw()
                thùng_rác_thực_phẩm.draw()
                nắp_thùng_rác_tp.draw()
                nắp_thùng_rác_tc.draw()
                nắp_thùng_rác_khác.draw()
                game.handle_level() 
            # chạy các điều kiện        
            game.check_win_condition()  
            game.check_game_over_condition()
            # nếu nhấn nút cách thì trở lại menu
            if game.game_paused: 
                game.draw_menu()
            else:
                game.handle_level()            
            # vẽ nút thoát khỏi trò chơi
            if not game.game_paused and game.level == 0 and exit_button.draw() :# vì ta đã tạo tọa độ cho nó trước đó nên bước này ko cần tạo
                pygame.quit() 
                quit() 
                print('EXIT')
  # xử lý chuột bàn phím và nút:
            for event in pygame.event.get():
                #khi nhấn nút cách:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        transition_sound.play()
                        game.game_paused = not game.game_paused
                        print('PAUSE')
                # điều kiện có thể ko cần thiết         
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        space_sound_played = False  
                # khi nhất nút thoát khỏi màn hình trò chơi
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    quit() 
                    print('EXIT')  
             # khi nhấn chuột trái (lấy obj và di chuyển chúng)     
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for obj in game.levels[game.level]['objects']:
                        if obj.rect.collidepoint(event.pos): 
                             game.moving_obj = obj     
                             game.moving = True
                             break
                    else:
                        game.moving = False
                elif event.type == pygame.MOUSEMOTION and game.moving:
                    obj.rect.x += event.rel[0]  # Update the x position of the fish_bone
                    obj.rect.y += event.rel[1]  # Update the y position of the fish_bone
                elif event.type == pygame.MOUSEBUTTONUP:
                    game.moving_obj = None
                    game.moving = False         
            pygame.display.update()
if __name__=='__main__':
   main()