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

class Block1:
    def __init__(self):
        self.x = 0
        self.y = 90
        self.speed = 1.2
        self.length = 40
        self.width = 8
        self.restart()

    def move_down(self):
        self.y -= self.speed 
    
    def restart(self):
        self.y = 100
        self.x = pyxel.rndi(0, 40)

    def draw(self):
        pyxel.rect(self.x, self.y, self.length, self.width, 0)

class Block2:
    def __init__(self):
        self.x = 0
        self.y = 90 
        self.speed = 1.2
        self.length = 20
        self.width = 8
        self.restart()
    
    def move_down(self):
        self.y -= self.speed 
    
    def restart(self):
        self.y = 100
        self.x = pyxel.rndi(20, 100)
    
    def draw(self):
        pyxel.rect(self.x, self.y, self.length, self.width, 0)    

class App:
    def __init__(self):
        pyxel.init(100, 100)
        self.restart_game()
        pyxel.run(self.update, self.draw)

    def restart_game(self):
        self.player = Player()
        self.block1 = Block1()
        self.block2 = Block2()
        self.score = 0
        self.gameover = False 
        self.x = 0
        self.y = 0
        self.w = 100
        self.h = 100

    def update(self):
        if not self.gameover: 
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.player.move_right()
        
            if pyxel.btn(pyxel.KEY_LEFT):
                self.player.move_left()

            self.block1.move_down()
            self.block2.move_down()

            if self.block1.y < 0:
                self.block1.restart()
                self.score += 5
            
            if self.block2.y < 0:
                self.block2.restart()   
                self.score += 5

            if self.player.touch(self.block1) or self.player.touch(self.block2):
                self.gameover = True
             
            if self.player.touch(self.block1) and self.player.touch(self.block2):
                self.score += 0
            
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
        self.block1.draw()
        self.block2.draw()
        self.player.draw()

        if self.gameover:
            pyxel.text(35, 30, "Game Over", 7)
            pyxel.text(30, 60, "Press SPACE", 7)


App()
