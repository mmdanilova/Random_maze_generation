import random
import pygame

class Maze:
    def __init__(self, row: int, col: int):
        self.used = None
        self.row = row
        self.col = col
        self.nodes = self.row * self.col
        self.g = [[[] for _ in range(self.col)] for _ in range(self.row)]
        self.build_graph()
        self.build_maze()

    def build_graph(self):
        for i in range(self.row):
            for j in range(self.col):
                if i > 0:
                    self.g[i][j].append((i-1, j))
                if i < self.row - 1:
                    self.g[i][j].append((i+1, j))
                if j > 0:
                    self.g[i][j].append((i, j-1))
                if j < self.col - 1:
                    self.g[i][j].append((i, j+1))

    def check(self, i: int, j: int, a: int, b: int):
        if self.used[i][j] == 1:
            return False
        count = 0
        if i - 1 >= 0 and self.used[i-1][j] == 1:
            count += 1
        if i - 1 >= 0 and j + 1 < self.col and self.used[i-1][j+1] == 1:
            count += 1
        if i - 1 >= 0 and j - 1 >= 0 and self.used[i-1][j-1] == 1:
            count += 1
        if j - 1 >= 0 and self.used[i][j-1] == 1:
            count += 1
        if j + 1 < self.col and self.used[i][j+1] == 1:
            count += 1
        if i + 1 < self.row and j - 1 >= 0 and self.used[i+1][j-1] == 1:
            count += 1
        if i + 1 < self.row and j + 1 < self.col and self.used[i+1][j+1] == 1:
            count += 1
        if i + 1 < self.row and self.used[i+1][j] == 1:
            count += 1
        if i == a:
            if a - 1 >= 0 and self.used[a-1][b] == 1:
                count -= 1
            if a + 1 < self.row and self.used[a+1][b] == 1:
                count -= 1
        if j == b:
            if b - 1 >= 0 and self.used[a][b-1] == 1:
                count -= 1
            if b + 1 < self.col and self.used[a][b+1] == 1:
                count -= 1
        if count > 1:
            return False
        else:
            return True

    def backtracker(self, i: int, j: int):
        self.used[i][j] = 1
        random.shuffle(self.g[i][j])
        for u in self.g[i][j]:
            if self.check(u[0], u[1], i, j):
                self.backtracker(u[0], u[1])

    def build_maze(self):
        self.used = [[0] * self.col for _ in range(self.row)]
        self.backtracker(random.randint(0, self.row-1), random.randint(0, self.col-1))

    def __str__(self):
        string = ""
        for i in range(self.row):
            for j in range(self.col):
                string += str((self.used[i][j]+1) % 2)
            string += "\n"
        return string

    def show(self):
        pygame.init()
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        FPS = 3
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("white")
            for i in range(len(self.used)):
                for j in range(len(self.used[i])):
                    if self.used[i][j] == 1:
                        pygame.draw.rect(screen, "#E6FFBA", (10 + i * 20, 10 + j * 20, 20, 20))
                    else:
                        pygame.draw.rect(screen, "black", (10 + i * 20, 10 + j * 20, 20, 20))
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()
n, m = map(int, input().split())
maze = Maze(n, m)
maze.show()
