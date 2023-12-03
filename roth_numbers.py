from itertools import combinations
import time

def has_arithmetic_progression(seq):
    """
    Checks if a given sequence has an arithmetic progression of length 3.
    """
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            for k in range(j + 1, len(seq)):
                if seq[j] - seq[i] == seq[k] - seq[j]:
                    return True
    return False

def find_max_a_sequence(n):
    """
    Finds the maximum length of sequences without arithmetic progressions
    in the range from 1 to n.
    """
    max_length = 0
    max_sequences = []

    for r in range(1, n + 1):
        candidates = list(combinations(range(1, n + 1), r))
        valid_sequences = []

        for candidate in candidates:
            if not has_arithmetic_progression(candidate):
                valid_sequences.append(candidate)

        if len(valid_sequences) > 0:
            if r > max_length:
                max_length = r
                max_sequences = valid_sequences
            elif r == max_length:
                max_sequences.extend(valid_sequences)

    return max_length, max_sequences

# Prompt the user to input the value of n
n = int(input("Enter the value of n: "))

start_time = time.time()
length, sequences = find_max_a_sequence(n)
end_time = time.time()

print(f"r({n}) = {length}")
print(f"Number of maximal sets of r({n}): {len(sequences)}")
print("Maximal Sequences:")
for seq in sequences:
    print(seq)

elapsed_time = end_time - start_time
print("Execution Time:")

if elapsed_time < 60:
    print(f"{elapsed_time:.2f} seconds")
elif elapsed_time < 3600:
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    print(f"{minutes:.0f} minutes {seconds:.2f} seconds")
else:
    hours = elapsed_time // 3600
    remaining_time = elapsed_time % 3600
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    print(f"{hours:.0f} hours {minutes:.0f} minutes {seconds:.2f} seconds")
