from days.day7 import DAG, print_paths_below_node, count_paths_below_node, process_line, count_paths_in_dag, load_manifold, process_manifold, count_beam_splits, DAGNode, print_paths_in_dag

def test_process_line():
    lines = [list(".......S......."), list("...............")]
    processed = process_line(lines[0], lines[1])
    assert processed[7] == "|"
    lines = [list(".|.|||.||.||.|."),list("|^|^|^|^|^|||^.")]
    processed = process_line(lines[0], lines[1])
    assert processed[-1] == "|"

def test_count_beams():
    input = "inputs/day7_test_input.txt"
    manifold = load_manifold(input)
#    print(f"manifold")
    processed_manifold = process_manifold(manifold)
#    print(f"{processed_manifold}")
    count = count_beam_splits(processed_manifold)
    assert count == 21

def test_count_paths_in_dag():
    input = "inputs/day7_simplest_input.txt"
    manifold = load_manifold(input)
    processed_manifold = process_manifold(manifold)
    dag = DAG(processed_manifold)
    #print(processed_manifold)
    #print(dag.adjacency_list)
    count = print_paths_below_node(dag.root, dag, processed_manifold, [])
    assert count == 2
    input = "inputs/day7_test_input.txt"
    manifold = load_manifold(input)
    processed_manifold = process_manifold(manifold)
    #for row in processed_manifold:
    #    print("".join(row))
    dag = DAG(processed_manifold)
    node_counts = {}
    count = count_paths_below_node(dag.root, dag, node_counts)
    assert count == 40