import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer with Coins")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

FPS = 60
GRAVITY = 1
PLATFORM_COUNT = 6

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.velocity_y = 0
        self.jumping = False

    def update(self):
        # Horizontal movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Gravity
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Platform collision
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y > 0:
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.jumping = False

        # Keep player on screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def jump(self):
        if not self.jumping:
            self.velocity_y = -15
            self.jumping = True

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, platform):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (platform.rect.x + platform.rect.width // 2, platform.rect.y - 10)

# Score display
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    SCREEN.blit(text_surface, (x, y))

# Main game loop
def main():
    running = True
    clock = pygame.time.Clock()
    score = 0

    # Create player
    global player, platforms
    player = Player()

    # Create platforms and place coins
    platforms = pygame.sprite.Group()
    coins = pygame.sprite.Group()

    platform_height = HEIGHT - 50
    for i in range(PLATFORM_COUNT):
        platform = Platform(random.randint(0, WIDTH - 150), platform_height, 150, 20)
        platforms.add(platform)
        coin = Coin(platform)
        coins.add(coin)
        platform_height -= random.randint(80, 120)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(platforms)
    all_sprites.add(coins)

    while running:
        clock.tick(FPS)
        SCREEN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        # Update player movement
        all_sprites.update()

        # Coin collection logic
        coins_collected = pygame.sprite.spritecollide(player, coins, True)
        if coins_collected:
            score += len(coins_collected)

        # Draw everything
        all_sprites.draw(SCREEN)
        draw_text(f"Score: {score}", 36, BLACK, 10, 10)

        # Update the screen
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
