# Define the input and output file paths
input_file_path = "/home/duonnguyen/scaffolds.filled_clean.fa"
output_file_path = "/home/duongnguyen/scaffolds.filled_clean_format.fa"

try:
    # Open the input file for reading
    with open(input_file_path, "r") as input_file:
        # Read the content of the input file
        file_content = input_file.readlines()

    # Process each line to remove ">" and strings that begin with "|"
    processed_content = []
    for line in file_content:
        # Remove ">" from the line
        line = line.replace(">", "")
        # Remove strings that begin with "|"
        line = " ".join(word for word in line.split() if not word.startswith("|"))
        processed_content.append(line)

    # Write the processed content to the output file
    with open(output_file_path, "w") as output_file:
        output_file.writelines(processed_content)

    print("Processing completed. The output file has been created:", output_file_path)

except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading or writing the file.")
