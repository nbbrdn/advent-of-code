import os
from pathlib import Path

DATA_FILE = 'input.txt'

CRATES = [
    ['D', 'T', 'W', 'F', 'J', 'S', 'H', 'N',],
    ['H', 'R', 'P', 'Q', 'T', 'N', 'B', 'G',],
    ['L', 'Q', 'V',],
    ['N', 'B', 'S', 'W', 'R', 'Q',],
    ['N', 'D', 'F', 'T', 'V', 'M', 'B',],
    ['M', 'D', 'B', 'V', 'H', 'T', 'R',],
    ['D', 'B', 'Q', 'J',],
    ['D', 'N', 'J', 'V', 'R', 'Z', 'H', 'Q',],
    ['B', 'N', 'H', 'M', 'S',],
]


def make_step(bulk: int, stack_from: int, stack_to: int) -> None:
    for _ in range(bulk):
        crate = CRATES[stack_from].pop()
        CRATES[stack_to].append(crate)


def get_top_crates() -> str:
    result = ''
    for stack in CRATES:
        result += stack[-1]

    return result


def main() -> str:
    script_dir = Path(__file__).parent.absolute()
    file_name = os.path.join(script_dir, DATA_FILE)

    with open(file_name) as instructions:
        for instruction in instructions:
            tokens = instruction.split(' ')
            bulk = int(tokens[1])
            stack_from = int(tokens[3]) - 1 # zero-based
            stack_to = int(tokens[5]) - 1 # zero-based

            make_step(bulk, stack_from, stack_to)


    return get_top_crates()

if __name__ == '__main__':
    res = main()
    print(res)
