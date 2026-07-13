"""
벽돌깨기 게임 (Brick Breaker)
- 방향키(←, →) 또는 마우스로 패들 조작
- 스페이스바로 게임 시작 / 재시작
- ESC 로 종료

실행 방법:
    pip install pygame
    python brick_breaker.py
"""

import pygame
import random
import sys

# ---------------------------------------------------------
# 초기 설정
# ---------------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (20, 20, 30)
RED = (231, 76, 60)
ORANGE = (230, 126, 34)
YELLOW = (241, 196, 15)
GREEN = (46, 204, 113)
BLUE = (52, 152, 219)
PURPLE = (155, 89, 182)
GRAY = (149, 165, 166)

BRICK_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("malgungothic", 48)
font_medium = pygame.font.SysFont("malgungothic", 28)
font_small = pygame.font.SysFont("malgungothic", 20)


# ---------------------------------------------------------
# 패들
# ---------------------------------------------------------
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 15
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 40
        self.speed = 8

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx):
        self.x += dx
        self.x = max(0, min(WIDTH - self.width, self.x))

    def set_center_x(self, cx):
        self.x = cx - self.width // 2
        self.x = max(0, min(WIDTH - self.width, self.x))

    def draw(self, surf):
        pygame.draw.rect(surf, WHITE, self.rect, border_radius=6)


# ---------------------------------------------------------
# 공
# ---------------------------------------------------------
class Ball:
    def __init__(self, paddle):
        self.radius = 8
        self.paddle = paddle
        self.reset()

    def reset(self):
        self.x = self.paddle.x + self.paddle.width // 2
        self.y = self.paddle.y - self.radius - 1
        self.speed = 5
        angle_choices = [-1, 1]
        self.dx = self.speed * random.choice(angle_choices) * 0.6
        self.dy = -self.speed
        self.launched = False

    def rect(self):
        return pygame.Rect(
            self.x - self.radius, self.y - self.radius,
            self.radius * 2, self.radius * 2
        )

    def update(self):
        if not self.launched:
            self.x = self.paddle.x + self.paddle.width // 2
            self.y = self.paddle.y - self.radius - 1
            return

        self.x += self.dx
        self.y += self.dy

        # 좌우 벽 충돌
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.dx *= -1
        elif self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius
            self.dx *= -1

        # 위쪽 벽 충돌
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.dy *= -1

    def draw(self, surf):
        pygame.draw.circle(surf, WHITE, (int(self.x), int(self.y)), self.radius)


# ---------------------------------------------------------
# 벽돌
# ---------------------------------------------------------
class Brick:
    def __init__(self, x, y, w, h, color, hp=1):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.color = color
        self.hp = hp
        self.max_hp = hp
        self.alive = True

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.alive = False

    def draw(self, surf):
        if not self.alive:
            return
        # 체력에 따라 밝기 조절
        ratio = self.hp / self.max_hp
        color = tuple(min(255, int(c * (0.5 + 0.5 * ratio))) for c in self.color)
        pygame.draw.rect(surf, color, self.rect, border_radius=4)
        pygame.draw.rect(surf, BLACK, self.rect, width=2, border_radius=4)


def create_bricks(rows=6, cols=10, level=1):
    bricks = []
    margin_top = 60
    margin_side = 20
    gap = 6
    brick_w = (WIDTH - margin_side * 2 - gap * (cols - 1)) / cols
    brick_h = 22

    for r in range(rows):
        for c in range(cols):
            x = margin_side + c * (brick_w + gap)
            y = margin_top + r * (brick_h + gap)
            color = BRICK_COLORS[r % len(BRICK_COLORS)]
            # 위쪽 줄일수록 체력 높게 (레벨이 오를수록 조금 더 단단하게)
            hp = 1
            if r < 2 and level >= 2:
                hp = 2
            bricks.append(Brick(x, y, brick_w, brick_h, color, hp))
    return bricks


# ---------------------------------------------------------
# 게임 상태
# ---------------------------------------------------------
class Game:
    def __init__(self):
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)
        self.level = 1
        self.bricks = create_bricks(level=self.level)
        self.score = 0
        self.lives = 3
        self.state = "ready"  # ready, playing, gameover, win, level_clear

    def reset_ball_and_paddle(self):
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)

    def next_level(self):
        self.level += 1
        self.bricks = create_bricks(level=self.level)
        self.reset_ball_and_paddle()
        self.state = "ready"

    def restart(self):
        self.__init__()

    def update(self):
        if self.state != "playing":
            return

        self.ball.update()

        # 패들 충돌
        if self.ball.rect().colliderect(self.paddle.rect) and self.ball.dy > 0:
            hit_pos = (self.ball.x - self.paddle.x) / self.paddle.width  # 0~1
            angle_factor = (hit_pos - 0.5) * 2  # -1~1
            speed = (self.ball.dx ** 2 + self.ball.dy ** 2) ** 0.5
            self.ball.dx = speed * angle_factor
            self.ball.dy = -abs(self.ball.dy)
            self.ball.y = self.paddle.y - self.ball.radius - 1

        # 벽돌 충돌
        ball_rect = self.ball.rect()
        for brick in self.bricks:
            if brick.alive and ball_rect.colliderect(brick.rect):
                # 충돌 방향 판정 (간단한 방식)
                overlap_x = min(ball_rect.right, brick.rect.right) - max(ball_rect.left, brick.rect.left)
                overlap_y = min(ball_rect.bottom, brick.rect.bottom) - max(ball_rect.top, brick.rect.top)
                if overlap_x < overlap_y:
                    self.ball.dx *= -1
                else:
                    self.ball.dy *= -1
                brick.hit()
                if not brick.alive:
                    self.score += 10 * self.level
                else:
                    self.score += 5
                break

        # 공을 놓쳤을 때
        if self.ball.y - self.ball.radius > HEIGHT:
            self.lives -= 1
            if self.lives <= 0:
                self.state = "gameover"
            else:
                self.reset_ball_and_paddle()
                self.state = "ready"

        # 모든 벽돌 클리어
        if all(not b.alive for b in self.bricks):
            self.state = "level_clear"

    def draw(self, surf):
        surf.fill(BLACK)

        # 상단 UI
        score_text = font_small.render(f"점수: {self.score}", True, WHITE)
        lives_text = font_small.render(f"목숨: {'❤ ' * self.lives}".strip(), True, WHITE)
        level_text = font_small.render(f"레벨: {self.level}", True, WHITE)
        surf.blit(score_text, (20, 15))
        surf.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, 15))
        surf.blit(lives_text, (WIDTH - lives_text.get_width() - 20, 15))

        for brick in self.bricks:
            brick.draw(surf)

        self.paddle.draw(surf)
        self.ball.draw(surf)

        if self.state == "ready":
            self.draw_center_text("스페이스바를 눌러 시작하세요", 0)
        elif self.state == "gameover":
            self.draw_center_text("게임 오버!", -20, big=True)
            self.draw_center_text(f"최종 점수: {self.score}", 30)
            self.draw_center_text("스페이스바를 눌러 다시 시작", 70)
        elif self.state == "level_clear":
            self.draw_center_text(f"레벨 {self.level} 클리어!", -20, big=True)
            self.draw_center_text("스페이스바를 눌러 다음 레벨로", 30)

    def draw_center_text(self, text, y_offset, big=False):
        f = font_big if big else font_medium
        surface = f.render(text, True, WHITE)
        rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
        # 반투명 배경
        bg = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(bg, (0, 0, 0, 120), (0, 0, WIDTH, HEIGHT))
        screen.blit(bg, (0, 0))
        screen.blit(surface, rect)


def main():
    game = Game()
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    if game.state == "ready":
                        game.state = "playing"
                        game.ball.launched = True
                    elif game.state == "gameover":
                        game.restart()
                    elif game.state == "level_clear":
                        game.next_level()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.paddle.move(-game.paddle.speed)
        if keys[pygame.K_RIGHT]:
            game.paddle.move(game.paddle.speed)

        # 마우스로도 조작 가능
        mouse_x, _ = pygame.mouse.get_pos()
        if pygame.mouse.get_focused():
            pass  # 키보드 우선, 마우스는 아래에서 선택적으로 사용 가능

        game.update()
        game.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()