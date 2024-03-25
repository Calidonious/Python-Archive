import pygame
import sys

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Button:
    def __init__(self, text, position, size):
        self.text = text
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.hovered = False

    def draw(self, screen):
        color = GRAY if not self.hovered else GREEN
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        font = pygame.font.SysFont("Roboto", 30)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class Checkbox:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.checked = False
        self.rect = pygame.Rect(position[0], position[1], 20, 20)

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect, 2)
        if self.checked:
            pygame.draw.line(screen, BLACK, (self.rect.left + 2, self.rect.top + 2), (self.rect.right - 2, self.rect.bottom - 2), 2)
            pygame.draw.line(screen, BLACK, (self.rect.right - 2, self.rect.top + 2), (self.rect.left + 2, self.rect.bottom - 2), 2)
        font = pygame.font.SysFont("Roboto", 20)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(left=self.rect.right + 10, centery=self.rect.centery)
        screen.blit(text_surface, text_rect)

    def handle_click(self, pos):
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.checked = not self.checked

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.buttons = [
            Button("Build Molecule", (200, 200), (400, 50)),
            Button("Exit", (200, 300), (400, 50))
        ]
        self.checkboxes = [
            Checkbox("Full-screen", (400, 400)),
            Checkbox("Mute Music", (400, 450))
        ]
        self.selected_button = 0
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.handle_click(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_button = (self.selected_button + 1) % len(self.buttons)
                elif event.key == pygame.K_UP:
                    self.selected_button = (self.selected_button - 1) % len(self.buttons)
                elif event.key == pygame.K_RETURN:
                    self.handle_enter()

    def handle_mouse_motion(self, pos):
        for i, button in enumerate(self.buttons):
            if button.rect.collidepoint(pos):
                self.selected_button = i
                button.hovered = True
            else:
                button.hovered = False
        for checkbox in self.checkboxes:
            checkbox.handle_click(pos)

    def handle_click(self, pos):
        for i, button in enumerate(self.buttons):
            if button.rect.collidepoint(pos):
                if i == len(self.buttons) - 1:  # Check if it's the "Exit" button
                    pygame.quit()
                    sys.exit()
                else:
                    self.handle_enter()
        for checkbox in self.checkboxes:
            checkbox.handle_click(pos)
            if checkbox.text == "Full-screen":
                if checkbox.checked:
                    pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
                else:
                    pygame.display.set_mode((800, 600))

    def handle_enter(self):
        button = self.buttons[self.selected_button]
        if self.selected_button == len(self.buttons) - 1:  # Check if it's the "Exit" button
            pygame.quit()
            sys.exit()
        else:
            button.draw(self.screen)  # Simulate button press

    def draw(self):
        self.screen.fill(WHITE)
        for i, button in enumerate(self.buttons):
            button.hovered = (i == self.selected_button)
            button.draw(self.screen)
        for checkbox in self.checkboxes:
            checkbox.draw(self.screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Molecule Builder")

    menu = Menu(screen)
    menu.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
