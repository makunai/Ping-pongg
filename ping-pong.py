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


font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 50)
lose1 = font2.render('PLAYER 1 LOH', True, (180, 0,0))
lose2 = font2.render('PLAYER 2 LOH', True, (180, 0,0))
win1 = font2.render('PLAYER 1 WIN', True, (180, 0,0))
win2 = font2.render('PLAYER 2 WIN', True, (180, 0,0))



score1 = 0
score2 = 0


game = True
finish = False
clock = time.Clock()
FPS = 60


speed_x = 3
speed_y = 3


while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background,(0,0))
        text_lose = font1.render('Очки першого гравця: ' + str(score1), 1, (0,0,0))
        window.blit(text_lose, (10,20))
        text_winn = font1.render('Очки другого гравця: ' + str(score2), 1, (0,0,0))
        window.blit(text_winn, (10,50))


        racket1.update_l()
        racket2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > win_h - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x > 550:
            finish = True
            window.blit(lose2, (200,200))

        if sprite.collide_rect(racket1, ball):
            score1 += 1

        if sprite.collide_rect(racket2, ball):
            score2 += 1

        if score1 == 1:
            finish = True
            window.blit(win1, (180,250))

        if score2 == 1:
            finish = True
            window.blit(win2, (180,250))

        



        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)