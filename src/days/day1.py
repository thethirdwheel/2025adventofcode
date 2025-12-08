def rotate(pos, instruction, max_pos=99):
    sign = -1 if instruction[0] == 'L' else 1
    new_pos = (pos + sign*int(instruction[1:])) % (max_pos+1)
    return new_pos

def rotate_and_count_zeros(pos, instruction, max_pos=99):
    dial_size = max_pos+1
    sign = -1 if instruction[0] == 'L' else 1
    steps = int(instruction[1:])
    new_pos = rotate(pos, instruction, max_pos)
    
    # Count how many times we're at position 0 during the rotation
    # We check positions: pos+sign*1, pos+sign*2, ..., pos+sign*steps
    # (excluding the starting position, as per test: pos=0, L2 should give zeros=0)
    
    num_zeros = 0
    
    if sign < 0:  # Moving left (negative direction)
        # We're at zero when: (pos + sign*k) % dial_size == 0
        # This means: pos - k ≡ 0 (mod dial_size), so k ≡ pos (mod dial_size)
        # We need k in range [1, steps] such that k ≡ pos (mod dial_size)
        
        # Find the first k >= 1 where we hit zero
        # k = pos + m*dial_size for m >= 0, and k <= steps
        first_zero_step = dial_size if pos == 0 else pos
        
        if first_zero_step <= steps:
            # Count how many zeros: first_zero_step, first_zero_step + dial_size, ... <= steps
            num_zeros = (steps - first_zero_step) // dial_size + 1
    else:  # Moving right (positive direction)
        # We're at zero when: (pos + k) % dial_size == 0
        # This means: pos + k ≡ 0 (mod dial_size), so k ≡ -pos (mod dial_size)
        # k ≡ (dial_size - pos) % dial_size (mod dial_size)
        
        # Find the first k >= 1 where we hit zero
        first_zero_step = dial_size if pos == 0 else dial_size - pos
        
        if first_zero_step <= steps:
            # Count how many zeros: first_zero_step, first_zero_step + dial_size, ... <= steps
            num_zeros = (steps - first_zero_step) // dial_size + 1
    
    return new_pos, num_zeros

def get_day1_code(file="inputs/dial_input.txt", max_pos=99):
    code = 0
    pos = 50
    with open(file, 'r') as f:
        for line in f:
            instruction = line.strip()
            pos = rotate(pos, instruction, max_pos)
            code = code + 1 if pos == 0 else code
    return code

def get_day2_code(file="inputs/dial_input.txt", max_pos=99):
    code = 0
    pos = 50
    #print(f"The dial starts by pointing at {pos}")
    with open(file, 'r') as f:
        for line in f:
            instruction = line.strip()
            new_pos, num_zeros = rotate_and_count_zeros(pos, instruction, max_pos)
            code = code + num_zeros 
            #print(f"The dial is rotated {instruction} to point at {new_pos}, updating code to {code}")
            pos = new_pos
    return code

def main():
    max_pos = 99
    file = "inputs/dial_input.txt"
    code = get_day2_code(file, max_pos)
    print(f"Based on {file} code is {code}")

if __name__ == "__main__":
    main()