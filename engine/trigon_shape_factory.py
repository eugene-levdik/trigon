import random
from trigon_rules import shapes_at_once
from trigon_shape import TrigonShape


class ShapeFactory:

    def __init__(self, seed):
        random.seed(seed)
        self.shape_lib = (
            # small triangles
            TrigonShape(True, ((0, 0),), 0.05),
            TrigonShape(False, ((0, 0),), 0.05),

            # two horizontally
            TrigonShape(True, ((0, 0), (0, 1)), 0.07),
            TrigonShape(False, ((0, 0), (0, 1)), 0.07),

            # two vertically
            TrigonShape(True, ((0, 0), (1, 1)), 0.07),

            # big triangles
            TrigonShape(True, ((0, 0), (0, 1), (0, -1), (1, 1)), 0.04),
            TrigonShape(False, ((0, 0), (0, 1), (0, -1), (-1, -1)), 0.04),

            # three lined
            TrigonShape(True, ((0, 0), (0, 1), (0, -1)), 0.04),
            TrigonShape(False, ((0, 0), (0, 1), (0, -1)), 0.04),
            TrigonShape(True, ((0, 0), (1, 1), (0, 1)), 0.04),
            TrigonShape(True, ((0, 0), (1, 1), (1, 0)), 0.04),
            TrigonShape(True, ((0, 0), (1, 1), (1, 2)), 0.04),
            TrigonShape(True, ((0, 0), (1, 1), (0, -1)), 0.04),

            # hexagon
            TrigonShape(True, ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (1, 3)), 0.1),

            # hexagons w/o two
            TrigonShape(True, ((0, 0), (0, -1), (1, 0), (1, 1)), 0.025),
            TrigonShape(True, ((0, 0), (0, 1), (1, 2), (1, 1)), 0.025),
            TrigonShape(True, ((0, 0), (0, -1), (0, -2), (1, 1)), 0.025),
            TrigonShape(True, ((0, 0), (1, 1), (1, 2), (1, 3)), 0.025),
            TrigonShape(True, ((0, 0), (1, 1), (1, 0), (1, -1)), 0.025),
            TrigonShape(True, ((0, 0), (0, 1), (0, 2), (1, 1)), 0.025),

            # long bars
            TrigonShape(True, ((0, 0), (0, 1), (0, 2), (0, 3)), 0.04),
            TrigonShape(True, ((0, 0), (0, -1), (1, 1), (1, 2)), 0.04),
            TrigonShape(True, ((0, 0), (1, 1), (1, 0), (2, 2)), 0.04)
        )
        pass

    def gen_new_shapes(self):
        new_shapes = []
        for i in range(shapes_at_once):
            flag = random.random()
            counter = 0
            for shape in self.shape_lib:
                counter += shape.probability
                if counter <= flag:
                    new_shapes.append(shape)
                    break
        if len(new_shapes) != shapes_at_once:
            raise Exception("Shape library is not correctly defined")
        return tuple(new_shapes)


if __name__ == '__main__':
    factory = ShapeFactory(123)
    for shape in factory.shape_lib:
        print(shape)
