def load_problems(file):
    print(f"Loading problems from {file}")
    problems = []
    with open(file, "r") as f:
        for line in f:
            print(f"saw line: {line}")
            i = 0
            for val in line.split():
                print(f"{i} {len(problems)}")
                if i >= len(problems):
                    print("added a thing to problems")
                    problems.append([])
                problems[i].append(val)
                i = i + 1
    return problems


def construct_problem(start, end, chararray):
    for i in range(end, start-1, -1):
        for j in range(len(chararray)-1, -1, -1):
            cur_string = concat[0:-2][i]






def load_problems2(file):
    chararray = []
    with open(file, "r") as f:
        for line in f:
            chararray.append(list(line))
    operator = chararray[-1][0] # get the operator for the first problem
    operator_pos = 0
    i = 1
    for i in range(1, len(chararray[-1])):
        if chararray[-1][i] != " ":
            #we've reached the end of the current problem
            #the first number starts two columns back (current column, space separator column)
            construct_problem(operator_pos, i-2, chararray)
        
            




def calc_problem(problem):
    #expecting an array with last value as operator
    operator = problem[-1]
    return eval(operator.join(problem[0:-1]))

def sum_problems(problems):
    total = 0
    for problem in problems:
        total = total + calc_problem(problem)
    return total

def main():
    problems= load_problems("inputs/day6_input.txt")
    total = sum_problems(problems)
    print(f"Problem answers sum up to {total}")

if __name__ == "__main__":
    main()