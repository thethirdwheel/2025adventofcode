from tkinter import W


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
                if i < len(current) - 2:
                    processed[i+1] = "|"
    return processed


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
    count = count_beam_splits(processed_manifold)
    print(f"Saw the beam split {count} times")
    pass

if __name__ == "__main__":
    main()