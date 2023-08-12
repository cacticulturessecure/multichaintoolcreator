import os
import datetime


# Define function to create a unique filename and write to it
def create_unique_file(code):
    # Get the current timestamp and format it to a string
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Create a base filename and append the timestamp to create a unique filename
    base_filename = "output"
    filename = f"{base_filename}_{timestamp}.py"

    # Check if a file already exists with the same name
    counter = 1
    while os.path.isfile(filename):
        # If a file exists, append an additional number to the filename to make it unique
        filename = f"{base_filename}_{timestamp}_{counter}.py"
        counter += 1

    # Open the file with the unique filename in write mode
    with open(filename, "w") as file:
        # Write the extracted code to the file
        file.write(code)

    # Return the unique filename
    return filename



def read_from_file(subdirectory, filename):
    """
    Reads the content of a file from the specified subdirectory and filename.
    :param subdirectory: The subdirectory inside the 'prompts' directory where the file is located.
    :param filename: The name of the file to read.
    :return: The content of the file as a string.
    """
    path = os.path.join('prompts', subdirectory, filename)
    with open(path, 'r') as file:
        return file.read().strip()

def write_to_file(subdirectory, filename, content):
    """
    Writes content to a file in the specified subdirectory and filename.
    :param subdirectory: The subdirectory inside the 'prompts' directory where the file will be created/overwritten.
    :param filename: The name of the file to write.
    :param content: The content to write to the file.
    """
    path = os.path.join('prompts', subdirectory, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        file.write(content)

# Additional utility functions for file handling can be added here.




def save_conversation(messages, filename='saved_conversations.txt'):
    while True:
        save_input = input("Would you like to save any portions of the conversation? (Y/N/EXIT): ")
        if save_input.upper() == 'Y':
            for message in messages:
                print(f"\n[Message Type]: {message['role']}\n[Content]: {message['content']}")
                save_message = input("Would you like to save this message? (Y/N): ")
                if save_message.upper() == 'Y':
                    with open(filename, 'a') as file:
                        file.write(f"[Message Type]: {message['role']}\n[Content]: {message['content']}\n\n")
        elif save_input.upper() == 'EXIT':
            break


