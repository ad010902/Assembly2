# Define the input and output file paths
input_file_path = "test.txt"
output_file_path = "test_2.txt"

try:
    # Open the input file for reading
    with open(input_file_path, "r") as input_file:
        # Read lines from the input file
        lines = input_file.readlines()

    # Remove ">" , "|" and all characters after "|" in each line
    modified_lines = []
    for line in lines:
        parts = line.split("|")
        modified_line = parts[0].replace(">", "").strip() + "\n"
        modified_lines.append(modified_line)

    # Write the modified lines to the output file
    with open(output_file_path, "w") as output_file:
        output_file.writelines(modified_lines)

    print("Processing completed. The output file has been created:", output_file_path)

except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading or writing the file.")