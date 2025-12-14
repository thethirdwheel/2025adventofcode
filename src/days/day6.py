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

def load_problems2(file):
    chararray = []
    with open(file, "r") as f:
        for line in f:
            chararray.append(list(line))
    transposed_chararray = [list(row) for row in zip(*chararray)]
    transposed_chararray.reverse()
    return transposed_chararray

def translate_problems2(chararray):
    problems = []
    vals = []
    for line in chararray:
        val = "".join(line[0:len(line)-1]).strip()
        if val != "":
            vals.append(val)
        operator = line[len(line)-1]
        if operator in "*+":
            calc = operator.join(vals)
            problems.append(calc)
            operator = ""
            vals = []
    return problems

def eval_and_sum(problems):
    sum = 0
    for p in problems:
        sum = sum + eval(p)
    return sum

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
    problems2 = load_problems2("inputs/day6_input.txt")
    translated_problems = translate_problems2(problems2)
    total2 = eval_and_sum(translated_problems)
    print(f"Second interpretation answers sum up to {total2}")

if __name__ == "__main__":
    main()