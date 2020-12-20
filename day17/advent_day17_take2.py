from itertools import product

def get_input(fname):
    with open(fname) as fid:
        lines = fid.readlines()

    out = []
    for i, line in enumerate(lines):
        out.append([])
        for l in line.strip():
            if l == '.':
                out[i].append(0)
            else:
                out[i].append(1)

    return out

class Grid:

    def __init__(self, initial_state, grid_dimensions):
        self.initial_state = initial_state
        self.grid_dimensions = grid_dimensions
        self.grid = {}
        self.initial_dx = len(initial_state)
        self.initial_dy = len(initial_state[0])
        self.updates = 0
        for i in range(self.initial_dx):
            for j in range(self.initial_dy):
                coords = [i,j] + [0]*(grid_dimensions - 2)
                self.grid[tuple(coords)] = initial_state[i][j]
        

    def _grow_grid(self,n):
        r = []
        dx = self.initial_dx
        for _ in range(self.grid_dimensions):
            r.append(range(-n,dx+n))
        
        for c in product(*r):
            if not c in self.grid:
                self.grid[c] = 0 

    def _get_neighbor_coords(self, c):
        r = []
        for i in c:
            r.append(range(i-1,i+2)) 
        a = list(product(*r))
        a.remove(c)
        return a

    def update_state(self):
        grid = self.grid.copy()
        for i in self.grid:
        
            is_active = bool(self.grid[i])
            neighbor_coords = self._get_neighbor_coords(i)

            n_active_neighbors = 0
            for nc in neighbor_coords:
                try:
                    n_active_neighbors += self.grid[nc]
                except KeyError:
                    grid[nc] = 0

            if is_active:
                if n_active_neighbors in [2,3]:
                    grid[i] = 1
                else:
                    grid[i] = 0
            else:
                if n_active_neighbors == 3:
                    grid[i] = 1
        
        self.grid = grid
        self.updates += 1

    def run_updates(self,n):
        for i in range(n):
            self._grow_grid(i+1)
            self.update_state()
            

    @property
    def n_active(self):
        c = 0 
        for i in self.grid:
            c += self.grid[i]
        return c

out = get_input('advent_day17.txt')

dims = len(out)

g = Grid(out,3)
g.run_updates(6) 
print(f'Number of active cells = {g.n_active}') 

g = Grid(out,4)
g.run_updates(6) 
print(f'Number of active cells = {g.n_active}') 