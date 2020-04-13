class TrigonShape:

    is_reference_up = False
    offsets = ()

    def __init__(self, is_reference_up, offsets):
        self.is_reference_up = is_reference_up
        self.offsets = tuple(offsets)

    def __repr__(self):
        return ('▲ ' if self.is_reference_up else '▼ ') + str(self.offsets)
