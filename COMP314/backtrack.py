import time


class knight_tour:
    def __init__(self, start=(0, 0), N=0):
        self.size = N
        self.step_count = 1

        # All the possible moves for the knight
        self.moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
        self.start = start  # Initialize starting position

        self.solution = [[-1 for _ in range(self.size)]
                         for _ in range(self.size)]

    def knight_tour(self, i, j, step_count):

        # Check total coverage
        if step_count == (self.size**2+1):
            return True

        for k in range(8):
            next_i = i+self.moves_x[k]
            next_j = j+self.moves_y[k]

            # Check if the room is preoccupied or not
            if(self.is_valid(next_i, next_j)):
                self.solution[next_i][next_j] = step_count
                if(self.knight_tour(next_i, next_j, step_count+1)):
                    return True
                self.solution[next_i][next_j] = -1  # Else Backtracking occurs
        return False

    def is_valid(self, next_i, next_j):
        # Check place is in range and not assigned yet
        if(next_i >= 0 and next_i <= self.size-1 and next_j >= 0 and next_j <= self.size-1):
            # Check Backtracking
            if(self.solution[next_i][next_j] == -1):
                return True
        return False

    def start_tour(self):
        # Initialize and start the Knight's tour
        i, j = self.start
        self.solution[i][j] = self.step_count
        if(self.knight_tour(i, j, 2)):
            for i in range(self.size):
                print(self.solution[i])
            return True
        return False


if __name__ == '__main__':
    coordinates = input(
        "Enter the initial position of the Knight: ")
    points = tuple(int(x) for x in coordinates.split())
    size = int(input("Enter the size of N*N chessboard: "))
    knight = knight_tour(points, size)
    start_time = time.time()
    print(knight.start_tour())
    end_time = time.time()
    diff_time = (end_time-start_time)
    print('The time required for solution: ', diff_time)
