from pygame import*

win_w = 600
win_h = 500
window = display.set_mode((win_w,win_h))
display.set_caption("Ping-pong")
background = transform.scale(image.load("fon.jpg"), (800,700))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, w = 110, h = 130):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    


class Player(GameSprite):
    def update_r(self):
        keys  = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_h - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys  = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_h - 80:
            self.rect.y += self.speed


racket1 = Player('racket-removebg-preview.png', 30, 200,8,50,150)
racket2 = Player('racket-removebg-preview.png', 520,200,8,50,150)
ball = GameSprite('miya.png', 200,200,4,100,110)




game = True
fihish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not fihish:
        window.blit(background,(0,0))

        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)