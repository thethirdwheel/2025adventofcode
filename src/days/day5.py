import re

def count_ids_in_ranges(ranges):
    count = 0
    f = merge_ranges(ranges)
    for r in f:
        s, e = get_range_start_end(r)
        count = count + ((e + 1) - s)
    return count

def check_range(id, rng):
    split_rng = rng.split("-")
    start = int(split_rng[0])
    end = int(split_rng[1])+1
    if id in range(start, end):
        return True
    return False

def can_merge(rstart, rend, fstart, fend):
    mergeable = False
    if (rstart >= fstart and rstart <= fend) or (rend >= fstart and rend <= fend):
        mergeable = True
    return mergeable

def merge(rstart, rend, fstart, fend):
    assert(can_merge(rstart, rend, fstart, fend))
    cstart = min(rstart, fstart)
    cend = max(rend, fend)
    return cstart, cend

def get_range_start_end(rng):
    splitr = rng.split("-")
    return int(splitr[0]), int(splitr[1])

def merge_ranges(ranges): 
    final_ranges = []
    for r in ranges:
        rstart, rend = get_range_start_end(r)
        candidate_start = rstart
        candidate_end = rend
        subsumed_ranges = []
        for i in range(0, len(final_ranges)):
            fstart, fend = get_range_start_end(final_ranges[i])
            if can_merge(candidate_start, candidate_end, fstart, fend):
                candidate_start, candidate_end = merge(candidate_start, candidate_end, fstart, fend)
                subsumed_ranges.append(final_ranges[i])
        for r in subsumed_ranges:
            if r in final_ranges:
                final_ranges.remove(r)
        final_ranges.append(f"{candidate_start}-{candidate_end}")
    return final_ranges

def load_freshness_db(file):
    fresh = []
    available = []
    with open(file, "r") as f:
        for line in f:
            if re.match(r"^\d+-\d+$", line):
                fresh.append(line.strip())
            elif re.match(r"^\d+$", line):
                available.append(line.strip())
    return fresh, available

def get_fresh_ids(ids, fresh):
    fresh_ids = {}
    for id in ids:
        for rng in fresh:
            if check_range(int(id), rng):
                fresh_ids[id] = 1
    return fresh_ids

def get_containing_ranges(id, ranges):
    containing_ranges = []
    for r in ranges:
        if check_range(id, r):
            containing_ranges.append(r)
    return containing_ranges

def count_fresh_ids(ids, fresh): #brute force and ignorance!
    count = len(get_fresh_ids(ids,fresh))
    return count

def main():
    file = "inputs/day5_input.txt"
    fresh, available = load_freshness_db(file)
    fresh2 = merge_ranges(fresh)
    count = count_fresh_ids(available, fresh2)
    fresh_range_count = count_ids_in_ranges(fresh2)
    print(f"{count} of the ingredients are available")
    print(f"There are {fresh_range_count} fresh ids in the database")

if __name__ == "__main__":
    main()