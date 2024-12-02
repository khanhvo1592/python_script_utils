# Change phone number starting with 84 to start with 0

input_file = "output_remove_duplicate_and_randomize.txt"
output_file = "randomize_and_remove_duplicate.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if line.strip().startswith("84"):
            line = "0" + line.strip()[2:] + "\n"  # Replace 84 with 0
        outfile.write(line)
