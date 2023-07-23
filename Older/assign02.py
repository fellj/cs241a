# Title:   Team Activity
# Name:    read_report_file.py
# Purpose: Receive a file from the user and report on its contents
# Date:    01/12/2021
#
# 
##############################################################################

##################################################################
# Requirements: 
# 
#                   (1) Prompt the user for a filename.
#
#                   (2) Open the requested file and read through it line by line.
#
#                   (3) Ignore the first line, as it contains header information.
#
#                   (4) Find the column for comm_rate and keep track of it as needed. (You may assume the file will have a consistent ordering of columns.)
#
#                   (5) After parsing through the complete file, display the average (mean) commercial rate across all zip codes.
#
#                   (6) Display the utility company, zip code, state, and rate for the zip code with the highest commercial rate in the file.
#
#                   (7) Display the utility company, zip code, state, and rate for the zip code with the lowest commercial rate in the file.
#
#                   (8) If there is a tie for the highest or lowest rate, you should display the zip code that came first in the file.
#
#
#
#
#
##################################################################
# Example Output
#              
# Please enter the data file: /home/cs241/assign02/rates.csv
#
# The average commercial rate is: 0.08402623352821378
#
# The highest rate is:
# Napakiak Ircinraq Power Co (99634, AK) - $0.839779005525
#
# The lowest rate is:
# Sierra Pacific Power Co (89496, NV) - $0.0
#
##################################################################

# This function prompts the user for a filename
def prompt_filename():
    """prompt_filename() - This function prompts the user for the full path of a text file. The return object is the filename path that will be used later. The function verifies the existance of the file. If the user does not enter a valid file after 5 attempts, they are prompted if they would like to exit the program.\n """
    import os.path
 
    valid = False
    attempts = 0
    yes_value = "yes"
    no_value  = "no"
    exit_program = no_value
    while not valid and exit_program != yes_value:
        in_file = str(input("Please enter the data file: "))
        if os.path.isfile(in_file):
            valid = True
            return in_file
        elif attempts > 4:
            exit_program = input("\nWould you like to exit the program (yes/no)? ")
        else:
            print("\nThis is not a valid file path. Please enter a valid file path with extension.")
            attempts += 1
            
# Display required values for a given commercial rate
def display_utility(input_line, rate):
    """display_utility(input_line, rate): - Receives a list of strings representing an electric utility and displays them in the required format. The commercial rate is included as an additional input parameter."""
    
    # Helper variables
    # for reporting output
    spacer                = " "
    open_paren            = "("
    close_paren           = ")"
    comma                 = ","
    dash                  = "-"
    dollar                = "$"
    zip_code              =  0
    utility               =  2
    state_abbr            =  3
    
    print (input_line[utility] + spacer + open_paren + \
           input_line[zip_code] + comma  + spacer +
           input_line[state_abbr] + close_paren + \
           spacer + dash + spacer + \
           dollar + rate)
    
def get_first_zip(input_list, rate, comm_index):
    """get_first_zip() - This function breaks a tie between utilties with identical rates selecting the utility located first in the file."""
    
    # Helper variables
    comma = ","
    
    # Identify if there is a duplicate rate
    duplicate = 0
    
    # A list for line values to
    # store the duplicate
    store_line     = []
    duplicate_line = []
    return_line    = []
    
    for line in input_list:
        utility_line = line.split(comma)
        if rate == utility_line[comm_index] and duplicate == 0:
            store_line = utility_line
            duplicate += 1
        elif rate == utility_line[comm_index] and duplicate == 1:
            duplicate_line = store_line
            
    if not duplicate_line:
        return_line = store_line
    else:
        return_line = duplicate_line

    return return_line
            
            
# This function reads the input file and displays the contents line by line
# ignoring the first line having headers
def parse_file_lines(input_file):
    """parse_file_lines() - This function reads a file and prints it line by line for the user. The first line is ignored because it contains a header."""
    
    # Initialize value lists
    comm_rate             =  []
    comm_rate_idx         =  6
    all_but_first         =  1
    
    # Open data file and read
    # contents storing the comm_rate
    # into the comm_rate list
    with open(input_file, encoding = 'cp850') as file:
        read_lines = file.readlines()
        read_lines = read_lines[all_but_first:]
        for line in read_lines:
            split_line = line.split(",")
            comm_rate.append(float(split_line[comm_rate_idx]))

        # Calculate the average comm_rate
        comm_rate_avg = str(sum(comm_rate) / len(comm_rate))
    
        # Find the lowest and highest comm_rate
        # Note: Converting the comm_rate_low value
        #       from float to integer because of
        #       how this program finds the lowest
        #       commercial rate utility. This rate
        #       is stored as an integer but needs
        #       to be reported as a floating point
        #       number. Both values are stored.
        ###########################################
        comm_rate_low_int = str(int(min(comm_rate)))
        comm_rate_low_flt = str(min(comm_rate))
        comm_rate_high    = str(max(comm_rate))
        
        # Debug only
#         print("\nLow commercial rate: " + comm_rate_low)
#         print("\nHigh commercial rate: " + comm_rate_high)
        
        # Report the average comm_rates
        ###########################################
        print("\nThe average commercial rate is: " + comm_rate_avg)
        
        # Low and high comm_rates should
        # be printed in the following format:
        ###########################################
        #
        # Utility name (zip, state) - comm_rate
        #
        ###########################################
        
        # Low and high comm rate data
        # holders
        high_line = ''
        low_line  = ''
        no_value  = ''
        
        # Loop through each line in
        # the data file and find the
        # high and low comm_rate
        # utilities and associated
        # information
        low_line = get_first_zip(read_lines, comm_rate_low_int, comm_rate_idx)
        high_line = get_first_zip(read_lines, comm_rate_high, comm_rate_idx)
        
                
        # Print the related information
        # for high and low commercial
        # rate utilities
        if not high_line == no_value:
            print("\nThe highest rate is:")
            display_utility(high_line, comm_rate_high)
        else:
            print("\nCould not find the highest commercial rate.")

        if not low_line == no_value:
            print("\nThe lowest rate is:")
            display_utility(low_line, comm_rate_low_flt)
        else:
            print("\nCould not find the lowest commercial rate.")

# The main function executing the requirements of the program               
def main():
    """main() - The main function executing the requirements of the program."""
    input_file = prompt_filename()
    parse_file_lines(input_file)
    
if __name__ == "__main__":
    main()    