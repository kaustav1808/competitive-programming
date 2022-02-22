seq = input()
dna_type = {"A": 0, "C": 0, "G": 0, "T": 0}
prev_type = "A"
prev_length = 0

for c in seq:
    if (c == prev_type):
        prev_length += 1
    else:
        dna_type[prev_type] = max(dna_type[prev_type], prev_length)
        prev_type = c
        prev_length = 1
dna_type[prev_type] = max(dna_type[prev_type], prev_length)
max_seq_len = 0
for i in dna_type:
    max_seq_len = max(max_seq_len, dna_type[i])
print(max_seq_len)
