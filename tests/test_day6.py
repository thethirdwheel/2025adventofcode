from days.day6 import load_problems, calc_problem, sum_problems

def test_on_test_input():
    problems = load_problems("inputs/day6_test_input.txt")
    total = sum_problems(problems)
    assert total == 4277556

def test_calc_problem():
    p = ["123", "45", "6", "*"]
    assert calc_problem(p) == 33210

def test_load_problems():
    problems = load_problems("inputs/day6_test_input.txt")
    print(f"{problems}")
    assert problems[0] == ["123", "45", "6", "*"]