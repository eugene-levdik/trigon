import random
from trigon_rules import shapes_at_once
from trigon_shape import TrigonShape


class ShapeFactory:

    def __init__(self, seed):
        random.seed(seed)
        self.shape_lib = (
            # small triangles
            TrigonShape(True, ((0, 0),)),
            TrigonShape(False, ((0, 0),)),

            # two horizontally
            TrigonShape(True, ((0, 0), (0, 1))),
            TrigonShape(False, ((0, 0), (0, 1))),

            # two vertically
            TrigonShape(True, ((0, 0), (1, 1))),

            # big triangles
            TrigonShape(True, ((0, 0), (0, 1), (0, -1), (1, 1))),
            TrigonShape(False, ((0, 0), (0, 1), (0, -1), (-1, -1))),

            # three lined
            # TrigonShape(True, ((0, 0), (0, 1), (0, -1), (1, 1)))
        )
        pass

    def gen_new_shapes(self):
        new_shapes = []
        for i in range(shapes_at_once):
            new_shapes.append(random.choice(self.shape_lib))
        return tuple(new_shapes)
