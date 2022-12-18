import os

from pathlib import Path

DATA_FILE = 'input.txt'

def str2int(string : str) -> tuple[int, int]:
    nums = string.split('-')
    return (int(nums[0]), int(nums[1]))

def main() -> int:
    script_dir = Path(__file__).parent.absolute()
    file_name = os.path.join(script_dir, DATA_FILE)
    
    cnt = 0

    with open(file_name) as f:
        for pair in f:
            ranges = pair.rstrip().split(',')
            range_0 = str2int(ranges[0])
            range_1 = str2int(ranges[1])
            if range_1[0] >= range_0[0] and range_1[1] <= range_0[1]:
                cnt += 1
            elif range_0[0] >= range_1[0] and range_0[1] <= range_1[1]:
                cnt += 1

    return cnt
            

if __name__ == '__main__':
    result = main()
    print(result)
