import pygame
import sys

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARKGRAY = (140,140,140)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 250, 205)

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

class AtomMenu:
    def __init__(self, screen, atoms, position, size):
        self.screen = screen
        self.atoms = atoms
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.selected_option = 0  # Initially selected option index
        self.atom_size = 30
        self.atom_spacing = 5

    def draw(self):
        # Draw menu background
        pygame.draw.rect(self.screen, GRAY, self.rect)
        # Draw atoms
        x, y = self.position
        for i, atom in enumerate(self.atoms):
            atom_rect = pygame.Rect(x + self.atom_spacing, y + i * (self.atom_size + self.atom_spacing),
                                     self.atom_size, self.atom_size)
            pygame.draw.rect(self.screen, WHITE, atom_rect)
            pygame.draw.rect(self.screen, BLACK, atom_rect, 1)
            font = pygame.font.SysFont("Roboto", 20)
            text_surface = font.render(atom, True, BLACK)
            text_rect = text_surface.get_rect(center=atom_rect.center)
            self.screen.blit(text_surface, text_rect)
            if i == self.selected_option:
                pygame.draw.rect(self.screen, GREEN, atom_rect, 1)  # Highlight selected atom

    def navigate(self, direction):
        self.selected_option = max(0, min(self.selected_option + direction, len(self.atoms) - 1))

    def select_atom(self):
        return self.atoms[self.selected_option]


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.grid_size = 10
        self.slot_size = 50
        self.grid = [[('', 0) for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.selected_slot = (0, 0)
        self.running = True
        # Dictionary of atoms with their available bonds
        self.atoms = {'H': 1, 'O': 2, 'N': 3, 'C': 4}  # Updated with available bonds
        self.atom_menu = AtomMenu(screen, list(self.atoms.keys()), (600, 20), (150, 200))
        # Dictionary to keep track of bonded atoms
        self.bonded_atoms = {}

    def run(self):
        while self.running:
            self.handle_events()
            self.update_bonding()
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.handle_mouse_click(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.move_selection(0, -1)  # Move up
                elif event.key == pygame.K_s:
                    self.move_selection(0, 1)  # Move down
                elif event.key == pygame.K_a:
                    self.move_selection(-1, 0)  # Move left
                elif event.key == pygame.K_d:
                    self.move_selection(1, 0)  # Move right
                elif event.key == pygame.K_q:
                    self.clear_selection()  # Clear selected slot
                elif event.key == pygame.K_SPACE:
                    self.add_atom_to_slot()
                elif event.key == pygame.K_ESCAPE:
                    self.atom_menu.selected_option = 0  # Reset atom menu selection
                elif event.key == pygame.K_UP:
                    self.atom_menu.navigate(-1)  # Navigate atom menu up
                elif event.key == pygame.K_DOWN:
                    self.atom_menu.navigate(1)  # Navigate atom menu down
                elif event.key == pygame.K_RETURN:
                    atom = self.atom_menu.select_atom()  # Select atom from atom menu
                    if atom:
                        self.grid[self.selected_slot[1]][self.selected_slot[0]] = (atom, self.atoms[atom])

    def handle_mouse_click(self, pos):
        # Check if mouse click is within atom menu
        if self.atom_menu.rect.collidepoint(pos):
            # Calculate clicked atom index
            rel_pos = (pos[0] - self.atom_menu.position[0], pos[1] - self.atom_menu.position[1])
            atom_index = rel_pos[1] // (self.atom_menu.atom_size + self.atom_menu.atom_spacing)
            self.atom_menu.selected_option = atom_index
        else:
            # Calculate the slot clicked based on mouse position
            slot_x = pos[0] // self.slot_size
            slot_y = pos[1] // self.slot_size
            self.selected_slot = (slot_x, slot_y)

    def move_selection(self, dx, dy):
        # Move the selection within the grid boundaries
        new_x = max(0, min(self.selected_slot[0] + dx, self.grid_size - 1))
        new_y = max(0, min(self.selected_slot[1] + dy, self.grid_size - 1))
        self.selected_slot = (new_x, new_y)

    def clear_selection(self):
        # Clear all data associated with the selected slot
        x, y = self.selected_slot
        self.grid[y][x] = ('', 0)
        self.bonded_atoms.clear()
        self.update_bonding()

    def update_bonding(self):
        # Clear existing bonds
        self.bonded_atoms.clear()
        # Update bonding for each atom in the grid
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                atom, bonds_left = self.grid[y][x]
                if atom:
                    # Check neighboring slots for potential bonding
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                            neighbor_atom, neighbor_bonds_left = self.grid[ny][nx]
                            if neighbor_atom and bonds_left > 0 and neighbor_bonds_left > 0:
                                # Bond the atoms
                                self.bonded_atoms[(x, y)] = (nx, ny)
                                self.bonded_atoms[(nx, ny)] = (x, y)
                                self.grid[y][x] = (atom, bonds_left - 1)
                                self.grid[ny][nx] = (neighbor_atom, neighbor_bonds_left - 1)

    def add_atom_to_slot(self):
        atom = self.atom_menu.select_atom()
        if atom:
            self.grid[self.selected_slot[1]][self.selected_slot[0]] = (atom, self.atoms[atom])

    def draw(self):
        self.screen.fill(DARKGRAY)
        # Draw grid
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                rect = pygame.Rect(x * self.slot_size, y * self.slot_size, self.slot_size, self.slot_size)
                pygame.draw.rect(self.screen, GRAY, rect, 1)
                if (x, y) == self.selected_slot:
                    pygame.draw.rect(self.screen, GREEN, rect, 3)  # Highlight selected slot
                atom, bonds_left = self.grid[y][x]
                if atom:
                    # Check if atom is bonded
                    if (x, y) in self.bonded_atoms:
                        bonded_x, bonded_y = self.bonded_atoms[(x, y)]
                        bonded_rect = pygame.Rect(bonded_x * self.slot_size, bonded_y * self.slot_size, self.slot_size,
                                                  self.slot_size)
                        pygame.draw.rect(self.screen, YELLOW, bonded_rect,
                                         3)  # Highlight bonded slot with yellow border
                    elif bonds_left == 0:
                        pygame.draw.rect(self.screen, RED, rect,
                                         3)  # Mark atoms with no available bonds with red border
                    font = pygame.font.SysFont("Roboto", 20)
                    text_surface = font.render(atom + ' (' + str(bonds_left) + ')', True,
                                               BLACK)  # Display atom letter and available bonds
                    text_rect = text_surface.get_rect(center=rect.center)
                    self.screen.blit(text_surface, text_rect)
        # Draw atom menu
        self.atom_menu.draw()

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
        elif self.selected_button == 0:  # Check if it's the "Build Molecule" button
            self.screen.fill(WHITE)  # Clear the screen
            game = Game(self.screen)
            game.run()

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