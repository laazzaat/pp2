from enum import Enum # flexible to work more than with numbers

SCORE = 0

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Snake:
    direction = None # default parameters
    color = (255, 255, 255)
    length = None
    body = []
    block_size = None
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()
        
    def respawn(self): # respawns snake in the given position after game ends
        self.length = 3
        self.body = [(20,20),(20,40),(20,60)] # if snake grows, new snake square will append in the list
        self.direction = Direction.DOWN

        global SCORE
        SCORE = 0

    def draw(self, game, window):
        for segment in self.body:
            game.draw.rect(window, self.color, (segment[0],segment[1],self.block_size, self.block_size))

    def move(self):
        curr_head = self.body[-1] # adds 20x20 block according to the direction
        if self.direction == Direction.DOWN:
            next_head = (curr_head[0], curr_head[1] + self.block_size)
            # next_head now has (20, 80) because it's going to up
            self.body.append(next_head)
        elif self.direction == Direction.UP:
            next_head = (curr_head[0], curr_head[1] - self.block_size)
            self.body.append(next_head)
        elif self.direction == Direction.RIGHT:
            next_head = (curr_head[0] + self.block_size, curr_head[1])
            self.body.append(next_head)
        elif self.direction == Direction.LEFT:
            next_head = (curr_head[0] - self.block_size, curr_head[1])
            self.body.append(next_head)

        if self.length < len(self.body): 
            # because we added new block after move, we must delete oldest block
            self.body.pop(0)
        
    
    def steer(self, direction): 
        # to control snake movement and check snake wont move up when it was previously going down, same for left and right
        if self.direction == Direction.DOWN and direction != Direction.UP:
            self.direction = direction
        elif self.direction == Direction.UP and direction != Direction.DOWN:
            self.direction = direction
        elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
            self.direction = direction
        elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
            self.direction = direction
    
    def eat(self):
        self.length += 1
        global SCORE
        SCORE += 1
    
    def check_for_food(self, food): # sees if the head of the snake is over the food
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            food.respawn(self.body)
    
    def check_tail_collision(self):
        head = self.body[-1]
        has_eaten_tail = False

        for i in range(len(self.body) - 1):
            segment = self.body[i]
            if head[0] == segment[0] and head[1] == segment[1]:
            # if one of the old blocks and newest block are intersecting
                has_eaten_tail = True

        return has_eaten_tail
    
    def check_bounds(self): # so snake wont escape window
        head = self.body[-1]
        if head[0] >= self.bounds[0]:
            return True
        if head[1] >= self.bounds[1]:
            return True

        if head[0] < 0:
            return True
        if head[1] < 0:
            return True

        return False
    
    def get_score():
        global SCORE
        return SCORE