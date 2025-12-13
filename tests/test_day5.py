from days.day5 import can_merge, merge, get_range_start_end, load_freshness_db, count_fresh_ids, merge_ranges, count_ids_in_ranges, get_fresh_ids, get_containing_ranges


def test_count_ids_in_ranges():
    r = ["1-1"]
    count = count_ids_in_ranges(r)
    assert count == 1
    r = ["1-10"]
    count = count_ids_in_ranges(r)
    assert count == 10
    r = ["1-10", "1-10"]
    count = count_ids_in_ranges(r)
    assert count == 10
    r = ["3-5", "10-14", "16-20", "12-18"]
    count = count_ids_in_ranges(r)
    assert count == 14

def test_merge():
    assert can_merge(10, 12, 9, 11)
    assert not can_merge(10, 12, 200, 300)
    ms, me = merge(10, 12, 9, 11)
    assert ms == 9
    assert me == 12
    ms, me = merge(9, 11, 10, 12)
    assert ms == 9
    assert me == 12
    ms, me = merge(9, 11, 9, 11)
    assert ms == 9
    assert me == 11

def test_on_test_input():
    file = "inputs/day5_test_input.txt"
    fresh, available = load_freshness_db(file)
    count = count_fresh_ids(available, fresh)
    assert count == 3
    fresh_range_count = count_ids_in_ranges(fresh)
    assert fresh_range_count == 14

def test_on_full_input():
    file = "inputs/day5_input.txt"
    fresh, available = load_freshness_db(file)
    count = count_fresh_ids(available, fresh)
    assert count == 623

def test_merge_ranges_complete():
    file = "inputs/day5_input.txt"
    fresh, available = load_freshness_db(file)
    fresh_merged_1 = merge_ranges(fresh)
    fresh_merged_2 = merge_ranges(fresh_merged_1)
    assert fresh_merged_1 == fresh_merged_2

def test_merge_duplicate_ranges():
    r = ["10-12", "10-12"]
    f = merge_ranges(r)
    assert len(f) == 1
    r= ["9-11", "10-12"]
    f = merge_ranges(r)
    assert len(f) == 1
    assert "9-12" in f
    r = ["9-11", "200-300", "10-12"]
    f = merge_ranges(r)
    assert len(f) == 2
    assert "9-12" in f
    assert "200-300" in f
    r = ["9-11", "200-300", "10-12", "10-12"]
    f = merge_ranges(r)
    assert len(f) == 2
    assert "9-12" in f

def test_merge_ranges():
    r = ["10-12", "11-14"]
    f = merge_ranges(r)
    assert f[0] == "10-14"
    r = ["10-12", "15-20"]
    f = merge_ranges(r)
    assert len(f) == 2
    assert "10-12" in f
    assert "15-20" in f
    r = ["10-12", "11-15", "4-13"]
    f = merge_ranges(r)
    assert f[0] == "4-15"
    r =["4-8", "1-3", "3-6"]
    f = merge_ranges(r)
    assert f[0] == "1-8"
    r = ["3-6", "4-8", "1-3"]
    f = merge_ranges(r)
    assert f[0] == "1-8"
    r = ["85725281436986-86498280258826", "367393906087255-370176258300954", "428970175235750-429057683979633"]
    f = merge_ranges(r)
    assert f == r

def test_on_trouble_ranges():
    file = "inputs/day5_lost_ranges.txt"
    trouble_ranges  = []
    with open(file, "r") as f:
        for line in f:
            trouble_ranges.append(line.strip())
    r = merge_ranges(trouble_ranges)
    file = "inputs/day5_missing_ids.txt"
    missing_ids = []
    with open(file, "r") as f:
        for line in f:
            missing_ids.append(line.strip())
    unmerged_ids = get_fresh_ids(missing_ids, trouble_ranges)
    merged_ids = get_fresh_ids(missing_ids, r)
    dropped_ids = []
    containing_ranges = {}
    for id in unmerged_ids:
        if id not in merged_ids:
            dropped_ids.append(id)
    for id in dropped_ids:
        containing_ranges[id] = get_containing_ranges(int(id), trouble_ranges)
    print(f"{containing_ranges}")
    assert len(unmerged_ids) == len(merged_ids)
