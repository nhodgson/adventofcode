import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(curr_dir, "advent_day_9.txt"),
    header=None
)

# Part 1.
def find_pair(segment, target):
    answer = False

    for i, r in segment.copy().iterrows():
        pair = segment.copy().drop(i, axis=0)

        if target in (r[0] + pair[0]).values:
            answer = True
            break

    return answer

preamble = 25

for idx, row in df.iterrows():
    if idx < preamble:
        pass
    else:
        seg = df.iloc[idx-preamble:idx, :]
        invalid_number = row[0]

        if not find_pair(seg, invalid_number):
            print(f"Invalid number! {invalid_number}")
            break