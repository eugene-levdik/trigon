from trigon_field import Trigon
from trigon_shape_factory import ShapeFactory
import random


class TrigonGame:

    trigon = None
    score = 0

    current_shapes = ()

    def __init__(self, seed=None):
        self.trigon = Trigon()
        self.shape_factory = ShapeFactory(seed)
        self.current_shapes = self.shape_factory.gen_new_shapes()

    def place_shape(self, shape_index, x, y):
        shape_to_put = self.current_shapes[shape_index]
        if not self.trigon.does_fit(shape_to_put, x, y):
            return False
        self.score += len(shape_to_put.offsets)
        self.score += self.trigon.put(shape_to_put, x, y)
        self.current_shapes = self.current_shapes[:shape_index] + self.current_shapes[shape_index + 1:]
        if len(self.current_shapes) == 0:
            self.current_shapes = self.shape_factory.gen_new_shapes()
        return True


if __name__ == "__main__":
    game = TrigonGame(seed=566)
    print(game.current_shapes)
    for i in range(100):
        x, y = 1, 1
        while not game.place_shape(0, x, y):
            x = random.randint(1, 15)
            y = random.randint(1, 15)
        print(game.trigon)

    print(game.trigon)
