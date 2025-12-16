from days.day7 import process_line, load_manifold, process_manifold, count_beam_splits

def test_process_line():
    lines = [list(".......S......."), list("...............")]
    processed = process_line(lines[0], lines[1])
    assert processed[7] == "|"

def test_count_beams():
    input = "inputs/day7_test_input.txt"
    manifold = load_manifold(input)
#    print(f"manifold")
    processed_manifold = process_manifold(manifold)
#    print(f"{processed_manifold}")
    count = count_beam_splits(processed_manifold)
    assert count == 21
