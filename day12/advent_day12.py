

with open('advent_day12.txt') as fid:
    lines = fid.readlines()

instructions = [line.strip() for line in lines]
instructions = [(line[0],int(line[1:])) for line in lines]

dirs = [0, 1, 2, 3]
current_pos = [0,0]
current_dir = 1

for action, val in instructions:
    if action == 'N':
        current_pos[1] += val
    if action == 'S':
        current_pos[1] -= val
    if action == 'E':
        current_pos[0] += val
    if action == 'W':
        current_pos[0] -= val
    if action == 'L':
        current_dir -= int(val/90)
    if action == 'R':
        current_dir += int(val/90)
    if action == 'F':

        # North
        if dirs[current_dir % 4] == 0:
            current_pos[1] += val
        # East
        elif dirs[current_dir % 4] == 1:
            current_pos[0] += val
        # South
        elif dirs[current_dir % 4] == 2:
            current_pos[1] -= val
        # West
        elif dirs[current_dir % 4] == 3:
            current_pos[0] -= val
        else:
            print(current_dir)

mdist = abs(current_pos[0]) + abs(current_pos[1]) 
x, y = current_pos
print(f'Final position = ({x},{y})')
print(f'Manhatten Distance = {mdist}')
