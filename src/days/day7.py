import copy
import re

class DAG:
    
    @classmethod
    def calc_node_name(cls, i, j, processed_manifold):
        return f"{i},{j}:{processed_manifold[i][j]}"
    
    @classmethod
    def get_node_ijval(cls, node_name):
        match = re.search(r"(?P<i>\d+),(?P<j>\d+):(?P<val>.*)", node_name)
        i = None
        j = None
        val = None
        if match:
            i = match["i"]
            j = match["j"]
            val = match["val"]
        return int(i),int(j),val

    def __init__(self, processed_manifold):
        row = 0
        thing = "".join(processed_manifold[row])
        col = thing.find("S")
        self.root = DAG.calc_node_name(row, col, processed_manifold)
        adjacency_list = {}
        leaves = []
        leaves.append(self.root)
        count = 0
        while len(leaves) > 0:
            cur = leaves.pop()
            row, col, val = DAG.get_node_ijval(cur)
            #don't reexamine populated children so that graph construction doesn't take forever
            if cur not in adjacency_list:
                #print(f"examining {cur}")
                adjacency_list[cur] = []
                count = count + 1
                if row < len(processed_manifold) - 1:
                    if processed_manifold[row+1][col] == "^":
                        #print(f"+1,-1: {processed_manifold[row+1][col-1]}")
                        if col > 0 and processed_manifold[row+1][col-1] in "S|":
                            adjacency_list[cur].append(DAG.calc_node_name(row+1,col-1, processed_manifold))
                        #print(f"row+1,col+1: {processed_manifold[row+1][col+1]}")
                        if col < len(processed_manifold[row+1]) - 1 and processed_manifold[row+1][col+1] in "S|":
                            adjacency_list[cur].append(DAG.calc_node_name(row+1,col+1, processed_manifold))
                    elif processed_manifold[row+1][col] == "|":
                        #print(f"row+1,col: {processed_manifold[row+1][col]}")
                        adjacency_list[cur].append(DAG.calc_node_name(row+1,col, processed_manifold))
                leaves.extend(adjacency_list[cur])
        self.adjacency_list = adjacency_list
        print(f"examined {count} nodes")

class DAGNode:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.val = "|"
        self.name = f"{self.row},{self.col},{self.val}"
        self.children = []
        self.visited = False
    
    def add_child(self, child):
        assert(isinstance(child, DAGNode))
        self.children.append(child)

    def __str__(self):
        return f"row: {self.row} col: {self.col} numchildren: {len(self.children)}"

    def add_children(self, processed_manifold):
        row = self.row
        col = self.col
        if row < len(processed_manifold) - 1:
            if processed_manifold[row+1][col] == "^":
                if col > 0 and processed_manifold[row+1][col-1] in "S|":
                    self.children.append(DAGNode(row+1, col-1))
                if col < len(processed_manifold[row+1]) - 1 and processed_manifold[row+1][col+1] in "S|":
                    self.children.append(DAGNode(row+1, col+1))
            elif processed_manifold[row+1][col] == "|":
                self.children.append(DAGNode(row+1, col))


def load_manifold(file):
    manifold = []
    with open(file, "r") as f:
        for line in f:
            manifold.append(list(line.strip()))
    return manifold

def process_line(previous, current):
    processed = current
    for i in range(0, len(current)):
        if current[i] == ".":
            if previous[i] in "S|":
                #print(f"added a beam at {i}")
                processed[i] = "|"
        if current[i] == "^":
            if previous[i] in "S|":
                if i > 0:
                    processed[i-1] = "|"
                if i < len(current) - 1:
                    processed[i+1] = "|"
    return processed

def print_manifold_w_breadcrumbs(processed_manifold, breadcrumbs):
    for i in range(len(processed_manifold)):
        row = ""
        for j in range(len(processed_manifold[i])):
            if processed_manifold[i][j] != "|":
                row = row + processed_manifold[i][j]
            else:
                row = row + processed_manifold[i][j] if (i,j) in breadcrumbs else row + "."
        print(row)

def print_paths_in_dag(node, processed_manifold, breadcrumbs):
    count = 0
    if len(node.children) == 0:
        count = 1
        #print(breadcrumbs)
        #print_manifold_w_breadcrumbs(processed_manifold, breadcrumbs)
    else:
        for child in node.children:
            new_crumb = copy.deepcopy(breadcrumbs)
            new_crumb.append((child.row, child.col))
            count = count + print_paths_in_dag(child, processed_manifold, new_crumb)
    return count

def print_paths_below_node(node, dag, processed_manifold, breadcrumbs):
    count = 0
    if len(dag.adjacency_list[node]) == 0:
        count = 1
        print(breadcrumbs)
        print_manifold_w_breadcrumbs(processed_manifold, breadcrumbs)
    else:
        for child in dag.adjacency_list[node]:
            row, col, val = DAG.get_node_ijval(child)
            new_crumb = copy.deepcopy(breadcrumbs)
            new_crumb.append((row, col))
            count = count + print_paths_below_node(child, dag, processed_manifold, new_crumb)
    return count

#now we need memoization
def count_paths_below_node(node, dag, node_counts):
    count = 0
    if node in node_counts:
        return node_counts[node]
    if len(dag.adjacency_list[node]) == 0:
        count = 1
    else:
        for child in dag.adjacency_list[node]:
            count = count + count_paths_below_node(child, dag, node_counts)
    node_counts[node] = count
    return count

def count_paths_in_dag(node):
    count = 0
    if len(node.children) == 0:
        count = 1
    else:
        for child in node.children:
            count = count + count_paths_in_dag(child)
    return count

def process_manifold(manifold):
    new_manifold = manifold
    for i in range(1, len(new_manifold)):
        transformed_line = process_line(new_manifold[i-1], new_manifold[i])
        new_manifold[i] = transformed_line
    return new_manifold

def count_beam_splits(processed_manifold):
    count = 0
    for i in range(1, len(processed_manifold)):
        for j in range(0, len(processed_manifold[i])):
            if processed_manifold[i][j] == "^" and processed_manifold[i-1][j] == "|":
                #if we have a beam splitter and a beam hits it, count it!
                count = count + 1
    return count

def count_beams(processed_manifold):
    count = 0
    for i in range(1, len(processed_manifold)):
        for j in range(0, len(processed_manifold[i])):
            if processed_manifold[i][j] == "|" and processed_manifold[i-1][j] != "|":
                print(f"at row {i} added beam because {processed_manifold[i-1][j]} above {processed_manifold[i][j]}")
                #saw a new beam
                count = count + 1
    return count

def main():
    #load file
    #iterate through the lines of the file
    #check the previous line, apply transformation rules to the current line
    input = "inputs/day7_input.txt"
    manifold = load_manifold(input)
    processed_manifold = process_manifold(manifold)
    bcount = count_beam_splits(processed_manifold)
    print(f"Saw the beam split {bcount} times")
    dag = DAG(processed_manifold)
    print(f"completed dag construction")
    node_counts = {}
    count = count_paths_below_node(dag.root, dag, node_counts)
    print(f"Saw {count} timelines.")

if __name__ == "__main__":
    main()