import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 900, 700
CELL_SIZE = 20
MAZE_WIDTH, MAZE_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
WALL_COLOR = (0, 0, 0)
PLAYER_COLOR = (128, 0, 128)  # Purple
EXIT_COLOR = (0, 255, 0)  # Green
BG_COLOR = (255, 255, 255)
FONT_COLOR = (0, 255, 0)  # Green
FONT_SIZE = 36


class MazeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Advanced Maze Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Roboto", FONT_SIZE)
        self.start_time = pygame.time.get_ticks()
        self.total_time = 2 * 60 * 1000  # 3 minutes in milliseconds

        self.maze = self.generate_maze()
        self.player_pos = self.find_start_position()
        self.exit_pos = self.find_end_position()

    @staticmethod
    def generate_maze():
        maze = [[1] * MAZE_HEIGHT for _ in range(MAZE_WIDTH)]

        def carve(x, y):
            maze[x][y] = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze[nx][ny] == 1:
                    maze[x + dx][y + dy] = 0
                    carve(nx, ny)

        carve(random.randrange(1, MAZE_WIDTH, 2), random.randrange(1, MAZE_HEIGHT, 2))
        return maze

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def find_start_position(self):
        for x in range(MAZE_WIDTH):
            for y in range(MAZE_HEIGHT):
                if self.maze[x][y] == 0:
                    return x, y
        return None

    def find_end_position(self):
        for x in range(MAZE_WIDTH - 1, 0, -1):
            for y in range(MAZE_HEIGHT - 1, 0, -1):
                if self.maze[x][y] == 0:
                    return x, y
        return None

    def draw_maze(self):
        for x in range(MAZE_WIDTH):
            for y in range(MAZE_HEIGHT):
                if self.maze[x][y] == 1:
                    pygame.draw.rect(self.screen, WALL_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_player(self):
        pygame.draw.rect(self.screen, PLAYER_COLOR,
                         (self.player_pos[0] * CELL_SIZE, self.player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_exit(self):
        pygame.draw.rect(self.screen, EXIT_COLOR,
                         (self.exit_pos[0] * CELL_SIZE, self.exit_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def move_player(self, dx, dy):
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        if MAZE_WIDTH > new_x > 0 == self.maze[new_x][new_y] and 0 < new_y < MAZE_HEIGHT:
            self.player_pos = (new_x, new_y)

    def check_win_condition(self):
        return self.player_pos == self.exit_pos

    def check_lose_condition(self):
        return pygame.time.get_ticks() - self.start_time >= self.total_time

    def run(self):
        while True:
            self.screen.fill(BG_COLOR)
            self.handle_events()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.move_player(-1, 0)
            if keys[pygame.K_RIGHT]:
                self.move_player(1, 0)
            if keys[pygame.K_UP]:
                self.move_player(0, -1)
            if keys[pygame.K_DOWN]:
                self.move_player(0, 1)

            self.draw_maze()
            self.draw_exit()
            self.draw_player()

            if self.check_win_condition():
                print("You Win!")
                pygame.quit()
                sys.exit()
            if self.check_lose_condition():
                print("You Lose!")
                pygame.quit()
                sys.exit()

            # Draw timer
            time_remaining = max(0, (self.total_time - (pygame.time.get_ticks() - self.start_time)) // 1000)
            timer_surface = self.font.render(f"Time: {time_remaining // 60:02}:{time_remaining % 60:02}", True,
                                             FONT_COLOR)
            self.screen.blit(timer_surface, (10, 10))

            pygame.display.flip()
            self.clock.tick(30)


if __name__ == "__main__":
    game = MazeGame()
    game.run()





