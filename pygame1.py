import pygame, random

pygame.init()
w, h = 600, 400
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

player = pygame.Rect(300, 200, 20, 20)
enemies = []
vel = []

score = 0
font = pygame.font.SysFont(None, 36)

def spawn_enemy():
    side = random.choice(['top','bottom','left','right'])
    if side == 'top':
        return pygame.Rect(random.randint(0,w), 0, 10, 10), (0, random.randint(2,5))
    if side == 'bottom':
        return pygame.Rect(random.randint(0,w), h, 10, 10), (0, -random.randint(2,5))
    if side == 'left':
        return pygame.Rect(0, random.randint(0,h), 10, 10), (random.randint(2,5), 0)
    return pygame.Rect(w, random.randint(0,h), 10, 10), (-random.randint(2,5), 0)

running = True
spawn_timer = 0

while running:
    screen.fill((10,10,20))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: player.y -= 20
    if keys[pygame.K_DOWN]: player.y += 20
    if keys[pygame.K_LEFT]: player.x -= 20
    if keys[pygame.K_RIGHT]: player.x += 20

    player.clamp_ip(screen.get_rect())

    spawn_timer += 1
    if spawn_timer > 30:
        r, v = spawn_enemy()
        enemies.append(r)
        vel.append(v)
        spawn_timer = 0

    for i, e in enumerate(enemies[:]):
        e.x += vel[i][0]
        e.y += vel[i][1]

        if e.colliderect(player):
            running = False

    pygame.draw.rect(screen, (0,255,150), player)

    for e in enemies:
        pygame.draw.rect(screen, (255,50,50), e)

    score += 1
    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Final Score:", score)