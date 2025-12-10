def load_banks(file):
    banks = []
    with open(file, "r") as f:
        for line in f:
            banks.append(line.strip())
    return banks

def select_batteries(bank, num_batteries=12):
    vals = []
    val = 0
    pos = 0
    for i in range(0, len(bank) + 1 - num_batteries): #range operator is end exclusive
        if int(bank[i]) > val:
            val = int(bank[i])
            pos = i
    vals.append(str(val))
    #print(f"Selected {val} from {bank} at {pos} with numbatteries {num_batteries} implying {bank[0:len(bank) - num_batteries]}")
    if num_batteries > 1:
        vals.extend(select_batteries(bank[pos+1:], num_batteries-1))
    return(vals)

def max_joltage(bank, num_batteries=12):
    vals = select_batteries(bank, num_batteries)
    max_joltage = int("".join(vals))
    print(f"{max_joltage}")
    return max_joltage
    

def main():
    # load the battery banks
    # for each bank of length N find the largest value of positions 0 to N-2, select the earliest instance of that value
    #   then, select the largest value following the position of the instance you selected
    #   max joltage for that bank is int(selection1+selection2)
    # sum the max joltages
    banks = load_banks("inputs/day3_input.txt")
    max_joltages = []
    for bank in banks:
        max_joltages.append(max_joltage(bank))
    joltage_sum = sum(max_joltages)
    print(f"{max_joltages}")
    print(f"Total joltage is {joltage_sum}")

if __name__ == "__main__":
    main()