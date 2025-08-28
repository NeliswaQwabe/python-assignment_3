# Ask the user to enter the name of the file they want to read
filename = input("Enter the name of the file to read: ")

try:
    # Try to open the file in read mode
    file = open(filename, "r")

    # Read the content of the file
    content = file.read()

    # Always close the file after reading
    file.close()

    # Convert the content to uppercase
    modified_content = content.upper()

    # Create a new file to write the modified content
    new_filename = "modified_" + filename

    # Open the new file in write mode
    new_file = open(new_filename, "w")

    # Write the modified content to the new file
    new_file.write(modified_content)

    # Close the new file after writing
    new_file.close()

    # Inform the user that the process was successful
    print(f"Modified content was written to '{new_filename}'.")

except FileNotFoundError:
    # Handle the case where the file doesn't exist
    print("Error: The file does not exist. Please check the filename and try again.")

except IOError:
    # Handle other input/output errors (like permissions or disk issues)
    print("Error: There was a problem reading or writing the file.")
