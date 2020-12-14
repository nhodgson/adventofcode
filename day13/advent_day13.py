def get_bus_ids(l):
    return [int(t) for t in l.split(',') if t != 'x']

with open('advent_day13.txt') as fid:
    lines = fid.readlines()

time = int(lines[0].strip())
bus_ids = get_bus_ids(lines[1]) 

next_bus_times = []
for bus in bus_ids:
    mins = time + bus - (time % bus)
    next_bus_times.append(mins)

indx = next_bus_times.index(min(next_bus_times))

next_bus_id = bus_ids[indx]
time_to_next_bus = next_bus_times[indx] - time
print(f'The soonest bus we can catch is BusID: {next_bus_id}')
print(f'BusID: {next_bus_id} departs in {time_to_next_bus} minutes')
print(f'Part 1 ans = {next_bus_id*time_to_next_bus}')