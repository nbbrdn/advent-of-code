WIN_SCORE = 6
LOST_SCORE = 0
DRAW_SCORE = 3

SHAPE_SCORES = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

RESULTS = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

def get_shape(code: str) -> str:
    shapes = {
        'A': 'rock',
        'X': 'rock',
        'B': 'paper',
        'Y': 'paper',
        'C': 'scissors',
        'Z': 'scissors',
    }

    return shapes[code]


def get_score(op_shape: str, me_shape: str) -> int:
    shape_score = SHAPE_SCORES[me_shape]

    if op_shape == 'rock' and me_shape == 'paper':
        return WIN_SCORE + shape_score

    if op_shape == 'rock' and me_shape == 'scissors':
        return LOST_SCORE + shape_score

    if op_shape == 'paper' and me_shape == 'rock':
        return LOST_SCORE + shape_score

    if op_shape == 'paper' and me_shape == 'scissors':
        return WIN_SCORE + shape_score

    if op_shape == 'scissors' and me_shape == 'rock':
        return WIN_SCORE + shape_score

    if op_shape == 'scissors' and me_shape == 'paper':
        return LOST_SCORE + shape_score

    return 0


def calc_me_shape(op_shape :str, result: str) -> str:
    if op_shape == 'rock' and result == 'lose':
        return 'scissors'
    if op_shape == 'rock' and result == 'draw':
        return 'rock'
    if op_shape == 'rock' and result == 'win':
        return 'paper'

    if op_shape == 'scissors' and result == 'lose':
        return 'paper'
    if op_shape == 'scissors' and result == 'draw':
        return 'scissors'
    if op_shape == 'scissors' and result == 'win':
        return 'rock'

    if op_shape == 'paper' and result == 'lose':
        return 'rock'
    if op_shape == 'paper' and result == 'draw':
        return 'paper'
    if op_shape == 'paper' and result == 'win':
        return 'scissors'

    return ''


def main():
    score = 0
    
    with open('input.txt') as f:
        for line in f:
            op_code, result_code = line.split()
            
            result = RESULTS[result_code]
            
            op_shape = get_shape(op_code)
            me_shape = calc_me_shape(op_shape, result)
            
            if op_shape == me_shape:
                score += (DRAW_SCORE + SHAPE_SCORES[me_shape])
            else:
                score += get_score(op_shape, me_shape)

    return score


if __name__ == '__main__':
    result = main()
    print(result)
