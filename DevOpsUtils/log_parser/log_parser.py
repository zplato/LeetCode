'''
Requirements:
Take the log file path as input (you can hardcode it for now)

    Print:
    Total number of errors
    Set of modules that raised errors (e.g., db, web)
    The latest (most recent timestamp) error message

Constraints / Focus
- Handle file reading safely
- Use Python built-ins (with, split, maybe re if needed)
- Output clean and readable summary

Bonus: Wrap logic in functions
'''
import os.path
import sys

def usage():
    print(
            '''
            Usage: python logparser.py logfile-path
            
                - logfile-path: path to the logfile
            
                Takes exactly 1 argument, else a default logfile will be ran 
            '''
          )

def print_report(error_list):
    print(f"Total Errors: {len(error_list)}")
    print(f"Error Components: {[x[0] for x in error_list]}")
    print(f"Last Error Message: {error_list[-1][1]}")

def main():


    if len(sys.argv) == 2:
        logfile = sys.argv[1]
    elif len(sys.argv) > 2:
        print(usage)
        exit(1)
    else:
        logfile = "logfile.log"

    if not os.path.exists(logfile):
        return "ERROR: Logfile {0} does not exist".format(logfile)

    # Open the file, and build the error list out to meet the requirements
    error_list = []
    with open(logfile, 'r') as lines:
        for line in lines:
            if "ERROR" in line:
                line_list = line.split(" ") # Date - Time - Component - Log Level - Message
                component = line_list[2].strip("[]")
                message = ' '.join(line_list[4:])
                error_list.append((component, message)) # component and message

    # Output, print the report
    print_report(error_list)



if __name__ == "__main__":
    main()