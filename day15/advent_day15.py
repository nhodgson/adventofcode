def play_game(starting_numbers, game_end=2020):
    numbers = {n:i+1 for i,n in enumerate(starting_numbers[:-1])}
    curr_num = starting_numbers[-1]      
    for n in range(len(numbers)+1, game_end):
        if curr_num not in numbers:
            numbers[curr_num] = n
            curr_num = 0
        else:
            nturns = n - numbers[curr_num]
            numbers[curr_num] = n
            curr_num = nturns

    return curr_num

def run_tests():
    tests = [ ((1,3,2), 1),
              ((2,1,3), 10),
              ((1,2,3), 27),
              ((2,3,1), 78),
              ((3,2,1), 438),
              ((3,1,2), 1836)]

    for test in tests:
        ans = play_game(test[0])
        assert ans == test[1]   


starting_numbers = [0,3,1,6,7,5]

ans = play_game(starting_numbers, 2020)  
print(f'Answer to part 1: {ans}')

ans = play_game(starting_numbers, 30000000)
print(f'Answer to part 2: {ans}')
