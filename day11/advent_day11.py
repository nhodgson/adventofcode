import numpy as np

class MyBoat:

    def __init__(self, arr, seat_tolerance=4):
        self.arr = np.array(arr)
        self.updates = 0 
        self.seat_tolerance = seat_tolerance

    @property
    def shape(self):
        return self.arr.shape

    def update_seat(self, row, col):
        val = self.arr[row, col] 
        if val not in [0,1,2]:
            raise ValueError(f'invalid seat at [{row},{col}]')
        # occupied
        if val == 2:
            if self.adjacent_seats_occupied(row,col) >= self.seat_tolerance:
                return 1
            else:
                return 2
        # empty
        elif val == 1:
            if self.adjacent_seats_occupied(row, col) == 0:
                return 2
            else:
                return 1
        else:
            return 0   
        
    def adjacent_seats_occupied(self, row, col):
  
        if row - 1 < 0: 
            a = 0
        else:
            a = row - 1

        if row + 2 > self.shape[0]: 
            b = self.shape[0]
        else:
            b = row + 2

        if col - 1 < 0: 
            c = 0
        else:
            c = col - 1

        if col + 2 > self.shape[1]:
            d = self.shape[1]
        else:
            d = col + 2

        sub_arr = self.arr[a:b, c:d]
        n_occupied = len(np.where(sub_arr == 2)[0])
        if self.arr[row,col] == 2:
            n_occupied -= 1

        return n_occupied                
 
    def update_all(self):
        arr = np.zeros_like(self.arr)
        for i in range(b.shape[0]):
            for j in range(b.shape[1]):
                arr[i,j] = self.update_seat(i,j)
        
        self.updates += 1
        return arr

    def steady_state(self):
        n=0
        while True:
            #print(f'Iteration {n}')
            arr = self.update_all()
            if np.all(self.arr == arr):
                break
            else:
                n += 1
                self.arr = arr

    @property
    def n_occupied(self):
        return np.count_nonzero(self.arr == 2)

    @classmethod
    def from_file(cls, fname):
        with open(fname) as fid:
            lines = fid.readlines()

        boat = []
        for line in lines:
            line = line.strip()
            row = []
            for s in line:
                if s == 'L':
                    val = 1
                if s == '.':
                    val = 0
                
                row.append(val)

            boat.append(row)

        return cls(np.array(boat))
        
class MyBoat2(MyBoat):

    def __init__(self, arr):
        super().__init__(arr)

    def _check_dir(self, row, col, dir):
        while True:
            row += dir[0]
            col += dir[1]
            if any([row < 0, col < 0, 
                    row > self.shape[0]-1, 
                    col > self.shape[1]-1]):
                return 0
            else:
                val = self.arr[row,col]

            if val == 2:
                return 1
            elif val == 1:
                return 0
            else:
                continue
    
    def adjacent_seats_occupied(self, row, col):
        n_occupied = 0

        directions = [(1,0), (0,1), (-1,0), (0,-1),
                      (1,1), (1,-1), (-1,1), (-1,-1)]    
        
        for dir in directions:
            n_occupied += self._check_dir(row, col, dir)

        return n_occupied


b = MyBoat.from_file('advent_day11.txt')
b.steady_state()
print(f'Number of occupied seats = {b.n_occupied}')

b = MyBoat2.from_file('advent_day11.txt')
b.seat_tolerance = 5
b.steady_state()
print(f'Number of occupied seats = {b.n_occupied}')
