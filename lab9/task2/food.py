from random import randint

fancy_colors = [(255,192,203), (0,191,255), (95,158,160), (255,228,181), (220,20,60)]

class Food:
    block_size = None # default parameters
    color = fancy_colors[randint(0, len(fancy_colors)-1)]
    x = 120
    y = 120
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, game, window):
        game.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size))

    def respawn(self, snake_body): # draws square in random position
        blocks_in_x = (self.bounds[0])//self.block_size
        blocks_in_y = (self.bounds[1])//self.block_size
        # if X size of window is 300, food's X size is 20, then 300/20 = 15 blocks are available to put our food on horizontal axis

        self.x = randint(0, blocks_in_x - 1) * self.block_size
        self.y = randint(0, blocks_in_y - 1) * self.block_size
        food_pos = (self.x, self.y)
        
        if food_pos in snake_body:
        # if food's random position lies on snake's body, it will generate another random position
            self.x = randint(0, blocks_in_x - 1) * self.block_size
            self.y = randint(0, blocks_in_y - 1) * self.block_size
            print("Food on body!")

        self.color = fancy_colors[randint(0, len(fancy_colors)-1)]