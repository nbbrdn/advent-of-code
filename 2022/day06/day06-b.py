import os
from pathlib import Path

DATA_FILE = 'input.txt'
MARKER_LENGTH = 14


def find_marker(stream :str) -> int:
    curr_pos = MARKER_LENGTH
    stream_length = len(stream)

    while curr_pos < stream_length:
        stream_slice = stream[curr_pos - MARKER_LENGTH:curr_pos]
        if len(set(stream_slice)) == len(stream_slice):
            return curr_pos
        curr_pos += 1

    return -1


def main() -> None:
    script_dir = Path(__file__).parent.absolute()
    file_name = os.path.join(script_dir, DATA_FILE)

    with open(file_name) as f:
        data_stream = f.read()
    
    ch_cnt = find_marker(data_stream)
    print(ch_cnt)

if __name__ == '__main__':
    main()
