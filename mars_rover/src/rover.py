class Rover:
    def __init__(self, coordinates, direction):
        self.coordinates = coordinates
        self.direction = direction

    def forward(self):
        if self.direction == 'N':
            self.coordinates[1] = self.coordinates[1] + 1
        if self.direction == 'E':
            self.coordinates[0] = self.coordinates[0] + 1
        if self.direction == 'W':
            self.coordinates[0] = self.coordinates[0] - 1
        if self.direction == 'S':
            self.coordinates[1] = self.coordinates[1] - 1

    def backwards(self):
        if self.direction == 'N':
            self.coordinates[1] = self.coordinates[1] - 1
        if self.direction == 'E':
            self.coordinates[0] = self.coordinates[0] - 1
        if self.direction == 'W':
            self.coordinates[0] = self.coordinates[0] + 1
        if self.direction == 'S':
            self.coordinates[1] = self.coordinates[1] + 1

    def rotate(self, rotate):
        if rotate == 'R':
            if self.direction == 'N':
                self.direction = 'E'
            elif self.direction == 'E':
                self.direction = 'S'
            elif self.direction == 'S':
                self.direction = 'W'
            elif self.direction == 'W':
                self.direction = 'N'

        if rotate == 'L':
            if self.direction == 'N':
                self.direction = 'W'
            elif self.direction == 'E':
                self.direction = 'N'
            elif self.direction == 'S':
                self.direction = 'E'
            elif self.direction == 'W':
                self.direction = 'S'

