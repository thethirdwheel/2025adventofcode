import re

def get_ranges(file):
    ranges = []
    with open(file, 'r') as f:
        for line in f:
            ranges.extend(line.split(","))
    return ranges

def check_ranges(ranges, multi_repeats=True):
    matches = []
    invalid_re = r"^(\d+)\1+$" if multi_repeats else r"^(\d+)\1$"      
    for rng in ranges:
        if not re.match(r"\d+-\d+", rng):
            print(f"{rng} is not a valid range. Must match \\d+-\\d+")
        split_range = rng.split("-")
        for i in range(int(split_range[0]), int(split_range[1])+1): #range is left inclusive right exclusive, but semantics of file are right inclusive
            if re.match(invalid_re, str(i)):
                matches.append(i)
    return matches

def main():
    #separate ranges by ,
    #for each range, split on -, iterate from start to end
    #for each iteration, regexmatch {\d*}[2], if it matches, add to list of invalid IDs
    #suminvalid ids
    ranges = get_ranges("inputs/day2_input.txt")
    matches = check_ranges(ranges)
    match_sum = sum(matches)
    print(f"matcheds sum to {match_sum}")
    

if __name__ == "__main__":
    main()
