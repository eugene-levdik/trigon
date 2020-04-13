from trigon_rules import size


class Triangle:

    filled = False

    x = 0
    y = 0

    row1 = 0
    row2 = 0
    row3 = 0

    is_up = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

        if x <= size:
            self.is_up = y % 2 == 1
        else:
            self.is_up = y % 2 == 0

        self.row1 = x
        if x <= size:
            self.row2 = int((y + 1) / 2)
        else:
            self.row2 = int(y / 2) + x - size
        self.row3 = (size + 1 + self.row1) - self.row2
        if not self.is_up:
            self.row3 -= 1

    def __repr__(self):
        # return str((self.row1, self.row2, self.row3))
        if not self.filled:
            return str('△' if self.is_up else '▽')
        return str('▲' if self.is_up else '▼')


