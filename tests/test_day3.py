from days.day3 import load_banks, max_joltage

def test_day3_sample():
    file = "inputs/day3_test_input.txt"
    banks = load_banks(file)
    max_joltages = []
    for bank in banks:
        max_joltages.append(max_joltage(bank, 2))
    joltage_sum = sum(max_joltages)
    assert joltage_sum == 357

def test_max_joltage_on_failing_bank():
    bank = "818181911112111"
    joltage = max_joltage(bank)
    assert joltage == 888911112111

def test_day3_sample_12batteries():
    file = "inputs/day3_test_input.txt"
    banks = load_banks(file)
    max_joltages = []
    for bank in banks:
        max_joltages.append(max_joltage(bank))
    joltage_sum = sum(max_joltages)
    print(f"{max_joltages}")
    assert joltage_sum == 3121910778619