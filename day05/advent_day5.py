
def binary_split(s, keep, lower='F', upper='B'):

    n = int(len(s) / 2) 
    if keep == lower:
        return s[:n]
    elif keep == upper:
        return s[n:]
    else:
        raise ValueError('expected B or F, got {}'.format(keep))


with open('advent_day5.txt') as fid:
    lines = fid.readlines()

seat_ids = []
for line in lines:
    line = line.strip()
    rows = list(range(128))
    for l in line[:7]:
        rows = binary_split(rows, l)

    seats = list(range(8))
    for s in line[7:]:
        seats = binary_split(seats, s, 'L', 'R')
    
    row = int(rows[0])
    seat = int(seats[0])
    seat_id = row * 8 + seat
    print('Row = {} Seat = {} SeatID = {}'.format(row, seat, seat_id))
    seat_ids.append(seat_id)