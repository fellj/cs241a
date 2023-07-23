# Checkpoint 02 a
# 01/11/21
# Requirements:
#              (1) prompt_number - function that prompts for a number
#                                  and keeps re-prompting as long as
#                                  the number is negative. Then it
#                                  returns the number
#              (2) compute_sum   - Accepts and sums three numbers and
#                                  returns the total
#              (3) main          - Calls the prompt_number function 3 times,
#                                  saves the value into three diff variables,
#                                  then passes those three variables to the
#                                  compute_sum function. Finally, it saves
#                                  the value of comput_sum into a variable
#                                  and displays it.
#
#
#
#############################################################################


def prompt_number():
    num = -1
    num = int(input("Enter a positive number: "))
    if num < 0:
        print ("Invalid entry. The number must be positive.")
    return num
    
def compute_sum(num1, num2, num3):
    if not isinstance(num1, int):
        if not isinstance(num1, float):
            print("The first number is not a valid number. Please enter an integer or floating point number.\n")
    elif not isinstance(num2, int):
        if not isinstance(num2, float):
            print("The second number is not a valid number. Please enter an integer or floating point number.\n")            
    elif not isinstance(num3, int):
        if not isinstance(num3, float):
            print("The third number is not a valid number. Please enter an integer or floating point number.\n")            
    else:
        total = num1 + num2 + num3
        return total

def main():
    
    # Create an empty list
    # for the required numbers
    num_list = []
    
    # Prompt for a number
    # three times
    
    while len(num_list) < 3:
        pos_num = prompt_number()
        if pos_num >= 0:
            num_list.append(pos_num)
            print("\n")

    # Compute the sum
    # of the numbers
    # in the list
    sum_total = compute_sum(num_list[0], num_list[1], num_list[2])
    
    # Display the
    # total sum
    print ("The sum is: " + str(sum_total))

if __name__ == "__main__":
    main()