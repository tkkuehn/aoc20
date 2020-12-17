import utils


class PocketDimension3d:
    def __init__(self, pattern):
        self.x_lims = range(-1, len(pattern[0].strip()) + 1)
        self.y_lims = range(-1, len(pattern) + 1)
        self.z_lims = range(-1, 2)
        self.active_cubes = set()
        for y, line in enumerate(pattern):
            for x, seat in enumerate(line.strip()):
                if seat == "#":
                    self.active_cubes.add((x, y, 0))

    def update_state(self):
        new_active = set()
        new_x_lims = self.x_lims
        new_y_lims = self.y_lims
        new_z_lims = self.z_lims
        for x in self.x_lims:
            for y in self.y_lims:
                for z in self.z_lims:
                    prev_active = (x, y, z) in self.active_cubes
                    adjacent_active = sum(
                        [
                            pos in self.active_cubes
                            for pos in adjacent_seats_3d(x, y, z)
                        ]
                    )
                    if (prev_active and (adjacent_active in [2, 3])) or (
                        (not prev_active) and (adjacent_active == 3)
                    ):
                        new_active.add((x, y, z))
                        if x <= self.x_lims.start:
                            new_x_lims = range(x - 1, new_x_lims.stop)
                        if x >= self.x_lims.stop - 1:
                            new_x_lims = range(new_x_lims.start, x + 2)
                        if y <= self.y_lims.start:
                            new_y_lims = range(y - 1, new_y_lims.stop)
                        if y >= self.y_lims.stop - 1:
                            new_y_lims = range(new_y_lims.start, y + 2)
                        if z <= self.z_lims.start:
                            new_z_lims = range(z - 1, new_z_lims.stop)
                        if z >= self.z_lims.stop - 1:
                            new_z_lims = range(new_z_lims.start, z + 2)
        self.active_cubes = new_active
        self.x_lims = new_x_lims
        self.y_lims = new_y_lims
        self.z_lims = new_z_lims


def adjacent_seats_3d(x, y, z):
    return [
        (x + i, y + j, z + k)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        for k in (-1, 0, 1)
        if not (i == j == k == 0)
    ]


def sim_six_cycles_3d(pattern):
    pocket = PocketDimension3d(pattern)
    for _ in range(6):
        pocket.update_state()
    return len(pocket.active_cubes)


class PocketDimension4d:
    def __init__(self, pattern):
        self.x_lims = range(-1, len(pattern[0].strip()) + 1)
        self.y_lims = range(-1, len(pattern) + 1)
        self.z_lims = range(-1, 2)
        self.q_lims = range(-1, 2)
        self.active_cubes = set()
        for y, line in enumerate(pattern):
            for x, seat in enumerate(line.strip()):
                if seat == "#":
                    self.active_cubes.add((x, y, 0, 0))

    def update_state(self):
        new_active = set()
        new_x_lims = self.x_lims
        new_y_lims = self.y_lims
        new_z_lims = self.z_lims
        new_q_lims = self.q_lims
        for x in self.x_lims:
            for y in self.y_lims:
                for z in self.z_lims:
                    for q in self.q_lims:
                        prev_active = (x, y, z, q) in self.active_cubes
                        adjacent_active = sum(
                            [
                                pos in self.active_cubes
                                for pos in adjacent_seats_4d(x, y, z, q)
                            ]
                        )
                        if (prev_active and (adjacent_active in [2, 3])) or (
                            (not prev_active) and (adjacent_active == 3)
                        ):
                            new_active.add((x, y, z, q))
                            if x <= self.x_lims.start:
                                new_x_lims = range(x - 1, new_x_lims.stop)
                            if x >= self.x_lims.stop - 1:
                                new_x_lims = range(new_x_lims.start, x + 2)
                            if y <= self.y_lims.start:
                                new_y_lims = range(y - 1, new_y_lims.stop)
                            if y >= self.y_lims.stop - 1:
                                new_y_lims = range(new_y_lims.start, y + 2)
                            if z <= self.z_lims.start:
                                new_z_lims = range(z - 1, new_z_lims.stop)
                            if z >= self.z_lims.stop - 1:
                                new_z_lims = range(new_z_lims.start, z + 2)
                            if q <= self.q_lims.start:
                                new_q_lims = range(q - 1, new_q_lims.stop)
                            if q >= self.q_lims.stop - 1:
                                new_q_lims = range(new_q_lims.start, q + 2)
        self.active_cubes = new_active
        self.x_lims = new_x_lims
        self.y_lims = new_y_lims
        self.z_lims = new_z_lims
        self.q_lims = new_q_lims


def adjacent_seats_4d(x, y, z, q):
    return [
        (x + i, y + j, z + k, q + m)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        for k in (-1, 0, 1)
        for m in (-1, 0, 1)
        if not (i == j == k == m == 0)
    ]


def sim_six_cycles_4d(pattern):
    pocket = PocketDimension4d(pattern)
    for _ in range(6):
        pocket.update_state()
    return len(pocket.active_cubes)


if __name__ == "__main__":
    parsed_strings = utils.parse_file_lines("day17_input.txt", str)
    print("Part 1: {}".format(sim_six_cycles_3d(parsed_strings)))
    print("Part 2: {}".format(sim_six_cycles_4d(parsed_strings)))
