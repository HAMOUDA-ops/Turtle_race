import pygame
import sys
import random

# 1. إعدادات اللعبة العامة
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird - Hamoud Edition")
clock = pygame.time.Clock()

# الألوان (RGB)
SKY_BLUE = (113, 197, 207)
YELLOW = (247, 216, 54)
GREEN = (115, 191, 46)
WHITE = (255, 255, 255)

# 2. كلاس الطائر (Bird)
class Bird:
    def __init__(self):
        self.x = 80
        self.y = SCREEN_HEIGHT // 2
        self.radius = 16
        self.gravity = 0.25
        self.velocity = 0
        self.jump_strength = -6.5

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        # منع الطائر من الخروج من أسفل الشاشة
        if self.y >= SCREEN_HEIGHT - self.radius:
            self.y = SCREEN_HEIGHT - self.radius
            self.velocity = 0

    def jump(self):
        self.velocity = self.jump_strength

    def draw(self):
        # رسم الطائر كدائرة صفراء
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), self.radius)

# 3. كلاس الأنابيب (Pipe)
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH + 50
        self.width = 60
        self.gap = 150  # الفتحة بين الأنبوب العلوي والسفلي
        # توليد ارتفاع عشوائي للأنبوب العلوي
        self.top_height = random.randint(50, SCREEN_HEIGHT - self.gap - 100)
        self.bottom_height = SCREEN_HEIGHT - (self.top_height + self.gap)
        self.speed = 3
        self.passed = False  # لمعرفة إذا الطائر تجاوز الأنبوب لحساب النقاط

    def move(self):
        self.x -= self.speed

    def draw(self):
        # الأنبوب العلوي
        top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        # الأنبوب السفلي
        bottom_rect = pygame.Rect(self.x, SCREEN_HEIGHT - self.bottom_height, self.width, self.bottom_height)

        pygame.draw.rect(screen, GREEN, top_rect)
        pygame.draw.rect(screen, GREEN, bottom_rect)

    def collide(self, bird):
        # إعداد مستطيلات وهمية (Hitboxes) حول الأنابيب للتأكد من التصادم
        top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        bottom_rect = pygame.Rect(self.x, SCREEN_HEIGHT - self.bottom_height, self.width, self.bottom_height)

        # مستطيل حول الطائر
        bird_rect = pygame.Rect(bird.x - bird.radius, bird.y - bird.radius, bird.radius * 2, bird.radius * 2)

        # التحقق من التصادم أو إذا لمس الأرض
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect) or bird.y <= 0:
            return True
        return False

# 4. دالة عرض النتيجة على الشاشة
def display_score(score):
    font = pygame.font.SysFont('Arial', 32, bold=True)
    score_surface = font.render(f"Score: {score}", True, WHITE)
    score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(score_surface, score_rect)

# 5. الدالة الأساسية لتشغيل اللعبة
def main():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    game_over = False

    # مؤقت لتوليد أنابيب جديدة كل فترة
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1500)  # أنبوب جديد كل 1.5 ثانية

    while True:
        # إدارة الأحداث (Events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_over:
                        bird.jump()
                    else:
                        # إعادة تشغيل اللعبة إذا خسر وضغط Space
                        main()

            # توليد أنبوب جديد
            if event.type == SPAWNPIPE and not game_over:
                pipes.append(Pipe())

        # تحديث عناصر اللعبة (إذا لم يكن هناك Game Over)
        if not game_over:
            bird.update()

            for pipe in pipes:
                pipe.move()

                # التحقق من الخسارة
                if pipe.collide(bird):
                    game_over = True

                # حساب النقاط عند تجاوز الأنبوب
                if not pipe.passed and pipe.x + pipe.width < bird.x:
                    pipe.passed = True
                    score += 1

            # حذف الأنابيب التي خرجت من الشاشة لتخفيف العبء على الذاكرة
            pipes = [pipe for pipe in pipes if pipe.x + pipe.width > 0]

        # رسم كل شيء على الشاشة
        screen.fill(SKY_BLUE)  # تلوين الخلفية باللون الأزرق

        for pipe in pipes:
            pipe.draw()

        bird.draw()
        display_score(score)

        # شاشة الخasارة
        if game_over:
            font = pygame.font.SysFont('Arial', 24, bold=True)
            text_surface = font.render("Game Over! Press SPACE to Restart", True, WHITE)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text_surface, text_rect)

        pygame.display.update()
        clock.tick(60)  # تحديد سرعة اللعبة بـ 60 إطار في الثانية

if __name__ == "__main__":
    main()
