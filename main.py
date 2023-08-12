from chatbots import unit_tests_from_function
from interactions import tool_creation_task_list
import os
from documentation import generate_tool_documentation



# (All previous imports and other functions remain unchanged.)

def get_user_function_input() -> str:
    """
    Prompt the user to input a function line-by-line until they enter 'END' or 'EXIT'.
    Returns:
        The user's function as a string, or `None` if the user chooses to exit.
    """
    print("Please paste the function you want to test:")
    print("(End your input by typing 'END' on a new line)")
    print("(Exit by typing 'EXIT' on a new line)")

    user_function = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        elif line.strip().upper() == "EXIT":
            return None
        user_function.append(line)

    return "\n".join(user_function)

from interactions import tool_creation_task_list

# tool creation function loop
# Main loop
while True:
    user_function = get_user_function_input()

    # Exit the loop if the user enters "EXIT"
    if user_function is None:
        print("Exiting the program.")
        break

    # Create the tool
    tool_creation = tool_creation_task_list(
        user_function,
        approx_min_cases_to_cover=10,
        print_text=True
    )
    print("Tool creation complete.")

    # Generate the documentation
    documentation = generate_tool_documentation(tool_creation)
    print("Documentation creation complete.")

    # Print or save the documentation as desired
    print(documentation)
    # Optionally, you could write the documentation to a file, send it to another system, etc.

# Usage: Unit test creation
#while True:
 #   user_function = get_user_function_input()

    # Exit the loop if the user enters "EXIT"
  #  if user_function is None:
   #     print("Exiting the program.")
    #    break

    #unit_tests = unit_tests_from_function(
     #   user_function,
      #  approx_min_cases_to_cover=10,
       # print_text=True
    #)
    #print(unit_tests)



