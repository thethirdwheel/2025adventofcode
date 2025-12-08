from days.day1 import rotate, rotate_and_count_zeros, get_day1_code, get_day2_code

def test_rotate_sign_negative_when_L():
    instruction = 'L1'
    pos = rotate(1, instruction)
    assert pos == 0

def test_rotate_sign_positive_when_R():
    instruction = "R1"
    pos = rotate(1, instruction)
    assert pos  == 2

def test_overflow_behavior():
    pos = 5
    max_pos = 9
    assert rotate(pos, "L6", max_pos) == 9
    assert rotate(pos, "R6", max_pos) == 1
    assert rotate(pos, "L10", max_pos) == pos

def test_zero_counting_with_no_overflow():
    pos = 5
    max_pos = 9
    _, zeros = rotate_and_count_zeros(pos, "L3", max_pos)
    assert zeros == 0
    _, zeros = rotate_and_count_zeros(pos, "R3", max_pos)
    assert zeros == 0
    new_pos, zeros = rotate_and_count_zeros(pos, "L5", max_pos)
    assert zeros == 1
    assert new_pos == 0
    new_pos, zeros = rotate_and_count_zeros(pos, "R5", max_pos)
    assert zeros == 1
    assert new_pos == 0

def test_zero_counting_with_overflow_smol_left():   
    #valid values are 0,1,2
    pos = 1
    max_pos = 2
    #show that we wrap around to 2 and get 1 zero
    new_pos, zeros = rotate_and_count_zeros(pos, "L2", max_pos)
    assert new_pos == 2
    assert zeros == 1
    #show that just going to 0 works
    new_pos, zeros = rotate_and_count_zeros(pos, "L1", max_pos)
    assert new_pos == 0
    assert zeros == 1
    #show that if we land on zero we get a second zero
    new_pos, zeros = rotate_and_count_zeros(pos, "L4", max_pos)
    assert new_pos == 0
    assert zeros == 2
    #show that moving off of 0 doesn't cause us issues
    new_pos, zeros = rotate_and_count_zeros(0, "L2", max_pos)
    assert new_pos == 1
    assert zeros == 0

def test_zero_counting_with_overflow_smol_right():
    #valid values are 0,1,2
    pos = 1
    max_pos = 2
    new_pos, zeros = rotate_and_count_zeros(0, "R2", max_pos)
    assert new_pos == 2
    assert zeros == 0
    new_pos, zeros = rotate_and_count_zeros(pos, "R4", max_pos)
    assert new_pos == 2
    assert zeros == 1
    new_pos, zeros = rotate_and_count_zeros(pos, "R2", max_pos)
    assert new_pos == 0
    assert zeros == 1


def test_zero_counting_with_overflow():
    pos = 5
    max_pos = 9
    _, zeros = rotate_and_count_zeros(pos, "L10", max_pos)
    assert zeros == 1
    _, zeros = rotate_and_count_zeros(pos, "L20", max_pos)
    assert zeros == 2
    new_pos, zeros = rotate_and_count_zeros(pos, "L25", max_pos)
    assert new_pos == 0
    assert zeros == 3
    _, zeros = rotate_and_count_zeros(pos, "R10", max_pos)
    assert zeros == 1
    _, zeros = rotate_and_count_zeros(pos, "R20", max_pos)
    assert zeros == 2
    new_pos, zeros = rotate_and_count_zeros(pos, "R25", max_pos)
    assert new_pos == 0
    assert zeros == 3

def test_r1000():
    new_pos, zeros = rotate_and_count_zeros(50, "R1000")
    assert new_pos == 50
    assert zeros == 10
    new_pos, zeros = rotate_and_count_zeros(50, "L1000")
    assert new_pos == 50
    assert zeros == 10

def test_example_rotations_day_1():
    file = "inputs/dial_test_input.txt"
    code = get_day1_code(file)
    assert code == 3

def test_example_rotations_day_2():
    file = "inputs/dial_test_input.txt"
    code = get_day2_code(file)
    assert code == 6


