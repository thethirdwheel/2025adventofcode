from days.day2 import get_ranges, check_ranges

def test_sample_ranges():
    file = "inputs/day2_test_input.txt"
    ranges = get_ranges(file)
    matches = check_ranges(ranges, False)
    print(f"{matches}")
    match_sum = sum(matches)
    assert match_sum == 1227775554
    matches = check_ranges(ranges, True)
    match_sum = sum(matches)
    print(f"{matches}")
    assert match_sum == 4174379265