import pyxel

class Player:
    def __init__(self):
        self.x = 50
        self.y = 30
        self.radius = 3
    
    def touch(self, block):
        if (
            self.y + self.radius >= block.y 
            and self.x + self.radius >= block.x
            and self.x - self.radius <= block.x + block.length
            and self.y - self.radius <= block.y + block.width
        ):
            return True 
        else:
            return False 

    def move_left(self):
        self.x -= 1
    
    def move_right(self):
        self.x += 1
    
    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 7)

class Block:
    def __init__(self, x, y, length, width, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.length = length
        self.width = width
        self.restart()

    def move_down(self):
        self.y -= self.speed

    def restart(self):
        self.y = 100
        self.x = pyxel.rndi(0, pyxel.width - self.length)

    def draw(self):
        pyxel.rect(self.x, self.y, self.length, self.width, 0)

class App:
    def __init__(self):
        pyxel.init(100, 100)
        self.restart_game()
        pyxel.run(self.update, self.draw)

    def restart_game(self):
        self.player = Player()
        self.blocks = [Block(0, 90, 40, 8, 1.2), Block(20, 90, 20, 8, 1.5)]  
        self.score = 0
        self.gameover = False
        self.x = 0
        self.y = 0
        self.w = 100
        self.h = 100

    def update_blocks(self):  
        for block in self.blocks:
            block.move_down()
            if block.y < 0:
                block.restart()
                self.score += 10

    def update(self):
        if not self.gameover: 
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.player.move_right()
        
            if pyxel.btn(pyxel.KEY_LEFT):
                self.player.move_left()

            self.update_blocks()  

            for block in self.blocks:
                if self.player.touch(block):
                    self.gameover = True

            if pyxel.frame_count % 30 == 0:
                if self.x < 25:
                    self.x += 1
                    self.y += 1
                    self.w -= 2
                    self.h -= 2

        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.restart_game()


    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, 100, 100, 6)
        pyxel.clip()
        pyxel.text(5, 5, f"Score: {self.score}", 8)
        pyxel.clip(self.x, self.y, self.w, self.h)

        for block in self.blocks: 
            block.draw()

        self.player.draw()

        if self.gameover:
            pyxel.text(35, 30, "Game Over", 7)
            pyxel.text(30, 60, "Press SPACE", 7)


App()
