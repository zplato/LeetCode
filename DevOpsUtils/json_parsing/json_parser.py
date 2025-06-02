import json
import os
import sys

def usage():
    usage_msg = '''
    Usage: json_parser.py /path/to/file.json
    Required to pass path to file.json
    '''
    print(usage_msg)

def parse_json(json_file):
    email_set = set()
    with open(json_file, 'r') as file:
        try:
            data = json.load(file)
        except Exception as e:
            print(f"ERROR: Exception occurred {e}")
            exit(1)
        for person in data:
            # print(person) # Debug Flag can be added here
            if person.get("email", None):
                email_set.add(person["email"]) # if it already exists, it will just ignore it and remain unchanged
            email = person.get("contact", {}).get("email", None)
            if email:
                email_set.add(email)

    return email_set


def main():

    if len(sys.argv) < 2 or sys.argv[1].lower() == "-h" or sys.argv[1].lower() == '--help':
        usage()
        exit(1)

    # verify it's a json file
    if os.path.isfile(sys.argv[1]) and sys.argv[1].endswith(".json"):
        email_set = parse_json(sys.argv[1]) # call to parse the json file
    else:
        print(".json file not found, please re-check path and try again")
        exit(1)

    print(f"Found email contacts in json: {email_set}")


if __name__ == "__main__":
    main()