def load_rolls(file):
    m = []
    with open(file, "r") as f:
        for line in f:
            m.append(list(line))
    return m

def count_neighbor_rolls(x, y, num_rows, num_cols, roll_matrix):
    count = 0
    for i in range(max(x-1,0), min(x+2, num_rows)): #range is end exclusive, so have to add 2 to x/y
        for j in range(max(y-1,0), min(y+2, num_cols)):
            #print(f"considering {i},{j} with value {roll_matrix[i][j]}")
            if (i != x or j != y) and roll_matrix[i][j] in ["@", "X"]:
                count = count + 1
    return count

def mark_accessible(roll_matrix):
    num_rows = len(roll_matrix)
    for x in range(num_rows):
        num_cols = len(roll_matrix[x])
        for y in range(num_cols):
            if roll_matrix[x][y] == "@": #can't be an accessible roll if you aren't a roll!
                neighbors = count_neighbor_rolls(x, y, num_rows, num_cols, roll_matrix)
                if neighbors < 4:
                    roll_matrix[x][y] = "X"
def remove_accessible(roll_matrix):
    num_rows = len(roll_matrix)
    for x in range(num_rows):
        num_cols = len(roll_matrix[x]) 
        for y in range(num_cols):
            if roll_matrix[x][y] == "X":
                roll_matrix[x][y] = "."

def count_accessible(roll_matrix):
    count = 0
    mark_accessible(roll_matrix)
    num_rows = len(roll_matrix)
    for x in range(num_rows):
        num_cols = len(roll_matrix[x])
        for y in range(num_cols):
            if roll_matrix[x][y] == "X": #can't be an accessible roll if you aren't a roll!
                count = count + 1
    return count

def count_eventually_accessible(roll_matrix):
    count = 0
    c = count_accessible(roll_matrix)
    while c > 0:
        count = count + c
        remove_accessible(roll_matrix)
        c = count_accessible(roll_matrix)
    return count

def main():
    #read file into a matrix
    #for each cell m[x][y] look at m[x-1][y=1], m[x][y-1], m[+1][y+1], m[x][y-1], m[x][y+1], m[x+1][y-1], m[x+1][y], m[x+1][y+1]
    #sum # of looked at cells that are @s, if sum < 4 count++
    roll_matrix = load_rolls("inputs/day4_input.txt")
    count = count_eventually_accessible(roll_matrix)
    print(f"There are {count} accessible rolls")

if __name__ == "__main__":
    main()