import sys
import os


def usage():
    print('''Usage: python log_parser_2.py path/to/logfile.csv''')

def process_logfile(logfile):

    # Initialize Returned Values
    avg_cpu = 0
    highest_cpu_timestamp = ""
    highest_memory = 0
    total_entries = 0

    # Initialize helper variables
    total_cpu = 0
    highest_cpu = 0


    with open(logfile) as csvfile:
        lines = csvfile.readlines()
        header_line = lines[0]
        lines = lines[1:]  # Remove header
        total_entries = len(lines)
        for line in lines:
            split_line = line.split(',')
            timestamp = split_line[0]
            cpu = float(split_line[1])
            memory = int(split_line[2])

            total_cpu+= cpu

            if cpu > highest_cpu:
                highest_cpu_timestamp = timestamp
                highest_cpu = cpu

            if memory > highest_memory:
                highest_memory = memory

        avg_cpu = total_cpu / total_entries


    return (avg_cpu, highest_cpu_timestamp, highest_memory, total_entries)

def print_report(logfile_output):
    print("Logfile Report")
    print("* Total Entries: " + str(logfile_output[3]))
    print("* Highest Memory: " + str(logfile_output[2]))
    print("* Highest CPU Time: " + str(logfile_output[1]))
    print("* Average CPU: " + str(logfile_output[0]))

def main():

    if len(sys.argv) != 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        usage()
        exit(1)

    logfile = sys.argv[1]
    if not os.path.isfile(logfile):
        print("logfile not found")
        print("using default logfile")
        logfile = "logfile.csv"

    logfile_output = process_logfile(logfile)

    print_report(logfile_output)



if __name__ == '__main__':
    main()