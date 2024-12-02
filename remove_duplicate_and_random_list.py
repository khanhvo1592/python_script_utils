import random

def remove_duplicates_and_randomize(file_path, output_file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    unique_lines = list(set(lines))
    print(f"Number of duplicate lines removed: {len(lines) - len(unique_lines)}")
    random.shuffle(unique_lines)  # Randomize the unique lines
    with open(output_file_path, 'w') as file:
        for line in unique_lines:
            file.write(line.strip() + "\n") 

remove_duplicates_and_randomize("output_chuan_hoa_phone.txt", "output_remove_duplicate_and_randomize.txt")
    