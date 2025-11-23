import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH = 480
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Bắn Máy Bay")

clock = pygame.time.Clock()

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_img = pygame.Surface((50, 40))
player_img.fill((0, 150, 255))
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 60))
player_speed = 6

# Đạn
bullets = []
BULLET_SPEED = -8

# Kẻ địch
enemy_img = pygame.Surface((40, 30))
enemy_img.fill((255, 50, 50))
enemies = []
ENEMY_SPEED = 3
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 700)

# Hàm vẽ
def draw():
    screen.fill((0, 0, 0))
    screen.blit(player_img, player_rect)

    for b in bullets:
        pygame.draw.rect(screen, WHITE, b)

    for e in enemies:
        screen.blit(enemy_img, e)

    pygame.display.flip()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Bắn đạn
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10)
                bullets.append(bullet)

        # Sinh kẻ địch
        if event.type == SPAWN_EVENT:
            x = random.randint(0, WIDTH - 40)
            enemy_rect = enemy_img.get_rect(topleft=(x, -40))
            enemies.append(enemy_rect)

    # Điều khiển máy bay
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed

    # Di chuyển đạn
    for b in bullets[:]:
        b.y += BULLET_SPEED
        if b.bottom < 0:
            bullets.remove(b)

    # Di chuyển kẻ địch
    for e in enemies[:]:
        e.y += ENEMY_SPEED
        if e.top > HEIGHT:
            enemies.remove(e)

    # Va chạm
    for e in enemies[:]:
        for b in bullets[:]:
            if e.colliderect(b):
                enemies.remove(e)
                bullets.remove(b)
                break

    draw()
    clock.tick(60)
