import re

# Define the input and output file paths
input_file_path = "/home/duongnguyen/scaffolds.filled_clean.fa"
output_file_path = "/home/duongnguyen/scaffolds.filled_clean540.fa"

try:
    # Open the input file for reading
    with open(input_file_path, "r") as input_file:
        # Read lines from the input file
        lines = input_file.readlines()

    # Process each line to insert "_" and remove "|"
    processed_lines = []
    for line in lines:
        # Remove "|" and everything after "|" in the line
        line = re.sub(r'\|.*', '', line)
        # Find the index of the first digit
        match = re.search(r'\d', line)
        if match:
            first_digit_index = match.start()
            # Insert "_" before the first digit
            line = line[:first_digit_index] + "_" + line[first_digit_index:]
        processed_lines.append(line)

    # Write the processed lines to the output file
    with open(output_file_path, "w") as output_file:
        output_file.writelines(processed_lines)

    print("Processing completed. The output file has been created:", output_file_path)

except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading or writing the file.")
