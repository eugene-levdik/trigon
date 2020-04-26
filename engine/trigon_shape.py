from trigon_field import Trigon


class TrigonShape:

    is_reference_up = False
    offsets = ()

    def __init__(self, is_reference_up, offsets, probability):
        self.is_reference_up = is_reference_up
        self.offsets = tuple(offsets)
        self.probability = probability

    def __repr__(self):
        display = Trigon(size=2)
        for x in range(len(display.field) - 1):
            for y in range(len(display.field[x]) - 1):
                try:
                    display.put(self, x + 1, y + 1)
                    # return display.__repr__().replace('△', ' ').replace('▽', ' ')
                    return display.__repr__()
                except IndexError:
                    continue
        raise Exception('Shape is too  big to display')
        # return ('▲ ' if self.is_reference_up else '▼ ') + str(self.offsets)


if __name__ == "__main__":
    shape_1 = TrigonShape(True, ((0, 0), (0, 1)), 0.07)
    print(shape_1)
