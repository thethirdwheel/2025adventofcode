from days.day6 import load_problems, calc_problem, sum_problems, load_problems2, translate_problems2, eval_and_sum

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

def test_translate_problem2():
    array = load_problems2("inputs/day6_test_input.txt")
    problems = translate_problems2(array)
    sum = eval_and_sum(problems)
    print(f"{problems}")
    print(f"{sum}")
    assert sum == 3263827