

with open('advent_day12.txt') as fid:
    lines = fid.readlines()

instructions = [line.strip() for line in lines]
instructions = [(line[0],int(line[1:])) for line in lines]

dirs = [0, 1, 2, 3]
current_ship_pos = [0,0]
current_waypoint_pos = [10,1]
current_ship_dir = 1

for action, val in instructions:
    if action == 'N':
        current_waypoint_pos[1] += val
    if action == 'S':
        current_waypoint_pos[1] -= val
    if action == 'E':
        current_waypoint_pos[0] += val
    if action == 'W':
        current_waypoint_pos[0] -= val
    if action in ['L', 'R']:
        nrots = int(val / 90)
        if action == 'L':   
            for i in range(nrots):
                x = -1*current_waypoint_pos[1]
                y = current_waypoint_pos[0]
                current_waypoint_pos = [x, y]
        else:
             for i in range(nrots):
                x = current_waypoint_pos[1]
                y = -1*current_waypoint_pos[0]
                current_waypoint_pos = [x, y]           

    if action == 'F':
        current_ship_pos[0] += val*current_waypoint_pos[0]
        current_ship_pos[1] += val*current_waypoint_pos[1]

mdist = abs(current_ship_pos[0]) + abs(current_ship_pos[1]) 
x, y = current_ship_pos
print(f'Final position = ({x},{y})')
print(f'Manhatten Distance = {mdist}')
