from days.day4 import load_rolls, count_neighbor_rolls, count_accessible, count_eventually_accessible

def test_count_accessible_on_test_input():
    roll_matrix = load_rolls("inputs/day4_test_input.txt")
    count = count_accessible(roll_matrix)
    print(f"There are {count} accessible rolls")
    assert count == 13

def test_count_accessible_zero_when_empty():
    m = ["...","...", "..."]
    c = count_accessible(m)
    assert c == 0

def test_count_neighbor_rolls_correctness():
    m = [".@.","@@@", ".@."]
    c = count_neighbor_rolls(1,1,3,3,m)
    assert c == 4

def test_count_eventually_accessible_on_test_input():
    roll_matrix = load_rolls("inputs/day4_test_input.txt")
    count = count_eventually_accessible(roll_matrix)
    print(f"There are {count} accessible rolls")
    assert count == 43