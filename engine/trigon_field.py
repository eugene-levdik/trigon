from triangle import Triangle
import trigon_rules


class Trigon:

    field = None
    current_pars = None

    def __init__(self, size=trigon_rules.default_size):
        self.size = size
        n = size

        field = []
        for x in range(n):
            line = []
            for y in range(2 * (n + x) + 1):
                line.append(Triangle(x + 1, y + 1, self.size))
            field.append(line)
        for x in range(n, 2 * n):
            line = []
            for y in range(4 * n - 1 - 2 * (x - n)):
                line.append(Triangle(x + 1, y + 1, self.size))
            field.append(tuple(line))
        self.field = tuple(field)

    def __repr__(self):
        n = self.size
        s = ''
        for i in range(n):
            s += (' ' * int((n - i - 1)))
            s += ''.join(map(str, self.field[i]))
            s += '\n'
        for i in range(n, 2 * n):
            s += (' ' * (i - n))
            s += ''.join(map(str, self.field[i]))
            s += '\n'
        return s

    def does_fit(self, shape, x, y):
        x -= 1
        y -= 1
        for dx, dy in shape.offsets:
            if x + dx < 0 or x + dx >= len(self.field):
                return False
            if y + dy < 0 or y + dy >= len(self.field[y + dy]):
                return False
            if self.field[x + dx][y + dy].filled:
                return False
        if self.field[x][y].is_up != shape.is_reference_up:
            return False
        return True

    def clear_full_lines(self):
        is_row1_filled = [True] * (2 * self.size)
        is_row2_filled = [True] * (2 * self.size)
        is_row3_filled = [True] * (2 * self.size)

        for line in self.field:
            for triangle in line:
                if not triangle.filled:
                    is_row1_filled[triangle.row1 - 1] = False
                    is_row2_filled[triangle.row2 - 1] = False
                    is_row3_filled[triangle.row3 - 1] = False

        cleared = 0

        for line in self.field:
            for triangle in line:
                if is_row1_filled[triangle.row1 - 1] or is_row2_filled[triangle.row2 - 1] or is_row3_filled[triangle.row3 - 1]:
                    triangle.filled = False
                    cleared += 1
        return cleared

    def put(self, shape, x, y):
        if not self.does_fit(shape, x, y):
            raise IndexError('The shape does not fit')
        for dx, dy in shape.offsets:
            self.field[x - 1 + dx][y - 1 + dy].filled = True
        return self.clear_full_lines()


if __name__ == "__main__":
    trigon = Trigon()
    print(trigon)
