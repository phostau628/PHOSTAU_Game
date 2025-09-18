import sys
import math
import random
import os
import pygame
from pygame.math import Vector2

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def load_image(file):
    try:
        return pygame.image.load(resource_path(file))
    except Exception as e:
        # 显示友好错误提示
        pygame.quit()
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("游戏启动失败",
            f"缺少关键文件：{file}\n\n"
            "请确保以下文件与游戏程序在同一目录：\n"
            "player.jpg, enemy.jpg, boss1~4.jpg")
        sys.exit(1)

pygame.init()



class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, color, trail_color, is_boss=False):
        super().__init__()
        # 修正创建 Surface 对象的语法错误
        size = (6, 20) if color == (255, 0, 0) else (4, 15)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.velocity = velocity
        self.trail = []
        self.trail_color = trail_color
        self.start_time = pygame.time.get_ticks()
        self.is_boss = is_boss

        # 圆形BOSS子弹
        if self.is_boss:
            self.image = pygame.Surface((10, 10), pygame.SRCALPHA)  # 透明背景
            pygame.draw.circle(self.image, color, (5, 5), 5)  # 绘制红色圆形
        # 玩家子弹
        elif color == (200, 200, 200):
            self.image = pygame.Surface((4, 15))
            self.image.fill(color)
        # 普通敌人子弹
        else:
            self.image = pygame.Surface((6, 20))
            self.image.fill(color)

        self.rect = self.image.get_rect(center=pos)

    def update(self):
        # 增强子弹可见性
        time_alive = (pygame.time.get_ticks() - self.start_time) / 1000
        self.rect.x += self.velocity.x * (1 + math.sin(time_alive * 3))
        self.rect.y += self.velocity.y * 1.2

        self.trail.append(self.rect.center)
        if len(self.trail) > 15:
            self.trail.pop(0)

        # 自动清理边界外的子弹
        if self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        try:
            self.orig_image = pygame.image.load(resource_path("chart/3D03487997CF31B6E196BCC5AD61E1D1.jpg"))  
        except Exception as e:
            print(f"玩家图片加载失败: {e}")
            sys.exit()
        self.orig_image = pygame.transform.scale(self.orig_image, (50, 80))
        self.image = self.orig_image.copy()
        self.rect = self.image.get_rect(center=self.game.screen_rect.center)
        self.speed = 5
        self.health = 2880
        self.shoot_delay = 100
        self.last_shot = 0


    def update1(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        self.rect.clamp_ip(self.game.screen_rect)

        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                self.shoot1()

    def shoot1(self):
        for angle in [-24, -12, 0, 12, 24]:
            velocity = Vector2(0, -12).rotate(angle)
            bullet = Bullet(
                self.rect.midtop,
                velocity,
                (192, 192, 192),  # 改为亮灰色
                (192, 192, 192)
            )
            self.game.bullets.add(bullet)

    def update2(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        self.rect.clamp_ip(self.game.screen_rect)

        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                self.shoot2()

    def shoot2(self):
        for angle in [-36,-24,-12,0,12,24,36]:
            velocity = Vector2(0, -9).rotate(angle)
            bullet = Bullet(
                self.rect.midtop,
                velocity,
                (144, 238, 144),  # 改为浅绿
                (144, 238, 144)
            )
            self.game.bullets.add(bullet)

    def update3(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        self.rect.clamp_ip(self.game.screen_rect)

        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                self.shoot3()

    def shoot3(self):
        for angle in [-45,-36,-24,-12,0,12,24,36,45]:
            velocity = Vector2(0, -8).rotate(angle)
            bullet = Bullet(
                self.rect.midtop,
                velocity,
                (173, 216, 230),  # 改为亮灰色
                (173, 216, 230)
            )
            self.game.bullets.add(bullet)

    def update4(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        self.rect.clamp_ip(self.game.screen_rect)

        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                self.shoot4()

    def shoot4(self):
        for angle in [-72, -56, -45, -36, -30, -24, -12, 0, 12, 24, 30, 36, 45, 56, 72]:
            velocity = Vector2(0, -6).rotate(angle)
            bullet = Bullet(
                self.rect.midtop,
                velocity,
                (64, 64, 64),
                (64, 64, 64)
            )
            self.game.bullets.add(bullet)
BOSS_TYPES = {
    1: {
        "image_path": "chart/2EF80F6C18C57E37D25365CA2A8E4FD6.jpg",
        "size": (140, 140),
        "health": 2000,
        "speed_range": (-3, 3),
        "bullet_speed": 4
    },
    2: {
        "image_path": "chart/62200DD83E5F8819034E6D058F452E5F.jpg",
        "size": (160 , 160),
        "health": 6666,
        "speed_range": (-4, 4),
        "bullet_speed": 5
    },
    3: {
        "image_path": "chart/75CCE7B5E1B58922D3B49B6455844113.jpg",
        "size": (180, 180),
        "health": 22222,
        "speed_range": (-1.5, 1.5),
        "bullet_speed": 6
    },
    4: {
        "image_path": "chart/58EBE0C66C49A01BE71264AC79DD0AF0.jpg",
        "size": (170, 170),
        "health": 38888,
        "speed_range": (-6, 6),
        "bullet_speed": 3
    },
    5: {
        "image_path": "chart/2A5AFB066FB306E54DD6EDAB5EF294E6.jpg",
        "size": (170, 170),
        "health":38888 ,
        "speed_range": (-5, 5),
        "bullet_speed": 10
    }

}
class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, pos, boss_type=None):
        super().__init__()
        self.game = game
        self.is_boss = boss_type is not None
        self.boss_type = boss_type  # 新增属性
        
        self.vertical_cooldown = 0  # 冷却计时器（毫秒）
        self.vertical_cooldown_max = 1000  # 每次转向后，强制持续移动1秒（1000毫秒）
        self.last_vertical_switch = pygame.time.get_ticks()  # 上次转向的时间

        try:
            if self.is_boss:
                # 根据boss_type加载不同配置
                config = BOSS_TYPES[boss_type]
                self.orig_image = pygame.image.load(resource_path(config["image_path"]))
                size = config["size"]
                self.health = config["health"]
                self.speed_range = config["speed_range"]
                self.bullet_speed = config["bullet_speed"]
            else:
                # 普通敌人保持原有逻辑
                img_path = resource_path("chart/5D12D4322F494C8D40ACB659FA2536DD.jpg")
                self.orig_image = pygame.image.load(img_path)
                size = (60, 60)
                self.health = 888
        except Exception as e:
            print(f"图片加载失败: {e}")
            sys.exit()

        self.orig_image = pygame.transform.scale(self.orig_image, size)
        self.image = self.orig_image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.max_health = self.health
        # 根据BOSS类型初始化速度
        self.speed = Vector2(
            random.uniform(*self.speed_range) if self.is_boss else random.choice([-2, 2]),
            random.uniform(0.5, 1.5)
        )
        self.fire_delay = 416 if self.is_boss else 999
        self.last_shot = 0
        self.min_y = 100 if self.is_boss else 50

    def update(self):
        # 改进移动逻辑
        prev_x = self.rect.x
        current_time = pygame.time.get_ticks()
        
        if self.is_boss:
            edge_threshold = 50
            near_edge = self.rect.left < edge_threshold or self.rect.right > 1000 - edge_threshold
            if near_edge and random.random() < 0.3:  # 30%概率转向
                self.speed.x *= -1
            elif random.random() < 0.03:  # 保持原有3%随机转向概率
                self.speed.x = random.uniform(*self.speed_range) 

            vertical_min = 60
            vertical_max = 320

            near_upper_edge = self.rect.top <= vertical_min + 30  # 上边界（60+30=90）
            near_lower_edge = self.rect.bottom >= vertical_max - 30  # 下边界（320-30=290）

            in_vertical_cooldown = (current_time - self.last_vertical_switch) < self.vertical_cooldown_max

            if not in_vertical_cooldown:
                # 1：靠近上/下边界→强制反向，同时启动冷却
                if near_upper_edge or near_lower_edge:
                    self.speed.y *= -1  # 反向垂直方向
                    self.last_vertical_switch = current_time 
                # 2.2 10%概率随机更新垂直速度（让移动更灵活）
            elif random.random() < 0.1:
                self.speed.y = random.uniform(1.8, 2.8)  # 垂直速度：0.8~1.8
                # 随机决定垂直方向（50%向下，50%向上）
                if random.random() < 0.5:
                    self.speed.y *= -1
                self.last_vertical_switch = current_time

        else:
            if random.random() < 0.08:
                self.speed.x = random.choice([-2, 2])

        # 应用移动并限制位置
        self.rect.move_ip(self.speed)
        self.rect.x = pygame.math.clamp(self.rect.x, 0, 1000 - self.rect.width)
        self.rect.y = pygame.math.clamp(self.rect.y, self.min_y, 250)  # 限制垂直移动范围

        if self.is_boss and self.rect.x == prev_x:
            self.speed.x *= -1  # 立即反转水平速度
            self.speed.x *= 1.2  # 增加速度避免卡顿

        # 射击逻辑优化
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.fire_delay:
            self.last_shot = now
            self.shoot()

    def shoot(self):
        if self.is_boss:
            # 根据不同BOSS类型实现不同射击模式
            if self.boss_type == 1:
                # 类型1：旋转弹幕
                base_angle = (pygame.time.get_ticks() // 20) % 360
                for angle in range(base_angle, base_angle + 360, 30):
                    velocity = Vector2(0, self.bullet_speed).rotate(angle)
                    self._create_boss_bullet(velocity)

            elif self.boss_type == 2:
                # 类型2：双向螺旋弹
                phase = pygame.time.get_ticks() // 15
                for angle in range(0, 360, 22):
                    v1 = Vector2(0, self.bullet_speed).rotate(angle + phase)
                    v2 = Vector2(0, self.bullet_speed).rotate(angle - phase)
                    self._create_boss_bullet(v1)
                    self._create_boss_bullet(v2)

            elif self.boss_type == 3:
                # 类型3：随机散射
                for angle in range(0, 360, 28):
                    velocity = Vector2(0, self.bullet_speed).rotate(angle)
                    self._create_boss_bullet(velocity)

                # 追踪弹（3发）
                player_pos = Vector2(self.game.player.rect.center)
                direction = (player_pos - Vector2(self.rect.center)).normalize()
                for _ in range(3):
                    velocity = direction * self.bullet_speed
                    self._create_boss_bullet(velocity)

            elif self.boss_type == 4:
                # 类型4：追踪弹+环形弹
                # 环形弹


                for _ in range(25):
                    angle = random.uniform(0, 360)
                    velocity = Vector2(0, self.bullet_speed).rotate(angle)
                    self._create_boss_bullet(velocity)

            elif self.boss_type == 5:
                for angle in [-90,-45,-25,0,25, 45,90]:
                    velocity = Vector2(0, self.bullet_speed).rotate(angle)
                    self._create_boss_bullet(velocity)
        else:


            for angle in [-45, 0, 45]:
                velocity = Vector2(0, 5).rotate(angle)
                bullet = Bullet(
                    self.rect.midtop,
                    velocity,
                    (255, 0, 0),  # 改为亮灰色
                    (255,130,120)
                )
                self.game.enemy_bullets.add(bullet)

    def _create_boss_bullet(self, velocity):
        bullet = Bullet(
            self.rect.center,
            velocity,
            (random.randint(100, 255), random.randint(50, 150), 50),  # 不同颜色
            (255,50,50),
            is_boss=True
        )
        self.game.enemy_bullets.add(bullet)

    def draw_health(self, surface):
        bar_width = 60 if self.is_boss else 40
        health_width = int(bar_width * (self.health / self.max_health))
        pygame.draw.rect(surface, (255, 0, 0), (self.rect.centerx - bar_width // 2, self.rect.top - 20, bar_width, 8))
        pygame.draw.rect(surface, (0, 255, 0),
                         (self.rect.centerx - bar_width // 2, self.rect.top - 20, health_width, 8))


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Zimin's Fighter")
        self.clock = pygame.time.Clock()
        self.screen_rect = self.screen.get_rect()

        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = Player(self)
        self.wave = 0
        self.game_over = False
        self.victory = False
        self.in_start_menu = True
        self.font = pygame.font.Font(None, 48)

        self.max_wave = 20
        # self.spawn_wave()

    def spawn_wave(self):
        self.wave += 1
        if self.wave % 5 == 0 and self.wave <= 20:
            if self.wave == 20:  # 当波数为15时
                boss_type1 = 4  # 可以自行指定第一个BOSS的类型
                boss_type2 = 5  # 可以自行指定第二个BOSS的类型
                enemy1 = Enemy(
                    self,
                    pos=(random.randint(200, 400), 150),  # 随机生成第一个BOSS的位置
                    boss_type=boss_type1  # 传入第一个BOSS类型
                )
                self.enemies.add(enemy1)
                enemy2 = Enemy(
                    self,
                    pos=(random.randint(600, 800), 150),  # 随机生成第二个BOSS的位置
                    boss_type=boss_type2  # 传入第二个BOSS类型
                )
                self.enemies.add(enemy2)
            else:  # 每5波生成BOSS直到20波
                boss_type = (self.wave // 5) % 4  # 计算BOSS类型（1-4）
                if boss_type == 0: boss_type = 5

                enemy = Enemy(
                    self,
                    pos=(random.randint(200, 800), 150),
                    boss_type=boss_type  # 传入BOSS类型
                )
                self.enemies.add(enemy)

        else:
            # 普通敌人生成在屏幕外上方
            for _ in range(8):
                x = random.randrange(50, 950)
                y = random.randrange(-300, -100)
                enemy = Enemy(self, (x, y))
                self.enemies.add(enemy)




    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.in_start_menu and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1=鼠标左键
                        self.in_start_menu = False  # 切换到游戏状态
                        self.spawn_wave()  # 生成第一波敌人
                # 合并处理game_over和victory的点击事件
                if (self.game_over or self.victory) and event.type == pygame.MOUSEBUTTONDOWN:
                    if self.again_rect.collidepoint(event.pos):
                        self.__init__()

            keys = pygame.key.get_pressed()

            if self.in_start_menu:
                self.screen.fill((30, 30, 60))  # 背景色（和游戏一致）
                
                # 绘制标题
                title_font = pygame.font.Font(None, 72)  
                title_text = title_font.render("Please sign the Death and Life Agreement", True, (201, 31, 55))  #
                title_rect = title_text.get_rect(center=(500, 200))
                self.screen.blit(title_text, title_rect)
                
                # 绘制开始提示
                start_font = pygame.font.Font(None, 48)
                start_text = start_font.render("CLICK TO SIGN", True, (179, 0, 0))
                start_rect = start_text.get_rect(center=(500, 350))
                self.screen.blit(start_text, start_rect)
                
                # 绘制操作说明
                tip_font = pygame.font.Font(None, 32)
                tip1_text = tip_font.render("Movement: WASD Keys | Attack: Spacebar (Holdable)", True, (180, 180, 180))
                tip1_rect = tip1_text.get_rect(center=(500, 450))
                self.screen.blit(tip1_text, tip1_rect)
                
                pygame.display.flip()  # 更新屏幕
                self.clock.tick(30)  # 降低开始界面帧率，减少资源占用
                continue  # 跳过后面的游戏逻辑，停留在开始界面

            if not self.game_over and not self.victory:

                # 原有的游戏逻辑更新
                if self.wave<=5:
                    self.player.update1(keys)
                    self.player.shoot_delay=60
                elif self.wave<=10:
                    self.player.update2(keys)
                    self.player.shoot_delay=60
                elif self.wave<=15:
                    self.player.update3(keys)
                    self.player.shoot_delay=50
                else:
                    self.player.update4(keys)
                    self.player.shoot_delay=35

                self.enemies.update()

                # 碰撞检测优化
                if pygame.sprite.spritecollide(self.player, self.enemy_bullets, True):
                    self.player.health = max(0, self.player.health - 5)
                    if self.player.health <= 0:
                        self.game_over = True

                # 使用更精确的碰撞检测
                hits = pygame.sprite.groupcollide(
                    self.enemies, self.bullets, False, True,
                    collided=pygame.sprite.collide_rect_ratio(0.8)
                )
                for enemy, _ in hits.items():
                    enemy.health -= 12
                    if enemy.health <= 0:
                        enemy.kill()

                if not self.enemies and self.wave < self.max_wave:
                    self.spawn_wave()
                elif not self.enemies and self.wave >= self.max_wave:
                    self.victory = True

                self.bullets.update()
                self.enemy_bullets.update()

            # 绘制优化
            self.screen.fill((30, 30, 60))  # 改为深色背景

            # 绘制子弹轨迹（增强可见性）
            for bullet in self.enemy_bullets:
                for i, pos in enumerate(bullet.trail):
                    alpha = int(200 * (i / len(bullet.trail)))
                    width = 4 - i * 0.25
                    # 确保颜色元组拼接正确
                    color = bullet.trail_color + (alpha,)
                    pygame.draw.line(
                        self.screen,
                        color,
                        pos,
                        bullet.trail[i - 1] if i > 0 else pos,
                        int(width)
                    )

            for bullet in self.bullets:
                for i, pos in enumerate(bullet.trail):
                    alpha = int(200 * (i / len(bullet.trail)))
                    width = 3 - i * 0.2
                    # 确保颜色元组拼接正确
                    color = bullet.trail_color + (alpha,)
                    pygame.draw.line(
                        self.screen,
                        color,
                        pos,
                        bullet.trail[i - 1] if i > 0 else pos,
                        int(width)
                    )

            self.screen.blit(self.player.image, self.player.rect)
            for enemy in self.enemies:
                self.screen.blit(enemy.image, enemy.rect)
                enemy.draw_health(self.screen)

            # 绘制UI
            health_text = self.font.render(f"HP: {self.player.health}", True, (255, 255, 255), (50, 50, 50))
            self.screen.blit(health_text, (10, 10))

            wave_text = self.font.render(f"Wave: {self.wave}", True, (200, 200, 255))
            self.screen.blit(wave_text, (10, 50))

            if self.game_over:
                overlay = pygame.Surface((1000, 600), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 180))
                self.screen.blit(overlay, (0, 0))

                text = self.font.render("GAME OVER", True, (255, 50, 50))
                text_rect = text.get_rect(center=(500, 250))
                self.screen.blit(text, text_rect)

                again_text = self.font.render("CLICK TO RESTART", True, (200, 200, 200))
                self.again_rect = again_text.get_rect(center=(500, 350))
                self.screen.blit(again_text, self.again_rect)

            if self.victory:
                overlay = pygame.Surface((1000, 600), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 180))
                self.screen.blit(overlay, (0, 0))

                text = self.font.render("VICTORY!", True, (255, 50, 50))
                text_rect = text.get_rect(center=(500, 250))
                self.screen.blit(text, text_rect)

                again_text = self.font.render("CLICK TO RESTART", True, (200, 200, 200))
                self.again_rect = again_text.get_rect(center=(500, 350))
                self.screen.blit(again_text, self.again_rect)


            pygame.display.flip()
            self.clock.tick(90)


if __name__ == "__main__":
    Game().run()