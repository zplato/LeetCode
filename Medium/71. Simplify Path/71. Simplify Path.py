# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.
#
# The rules of a Unix-style file system are as follows:
#
# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:
#
# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

class Solution:
    def simplifyPath(self, path: str) -> str:

        # Given the absolute path, iterate over it one character at a time checking for each of the conditions
        # Utilize one pointer

        # Remove any consecutive slashes
        split_path = path.split("/")
        # print(f"split_path: {split_path}")
        new_path = []

        i = 0
        while i < len(split_path):
            if split_path[i] == ".." and len(new_path) >= 1:
                new_path.pop()  # Remove the last element on the list
            elif split_path[i] == '.' or split_path[i] == '':
                pass  # Skip current dir as its nothing
            elif i == len(split_path) - 1 and split_path[i] != '' and split_path[i] != '.' and split_path[i] != '..':
                # On the last word
                new_path.append(split_path[i])
            elif split_path[i] != "..":
                new_path.append(split_path[i])
            i += 1

        # Add the initial root dir and then join everything together with '/'
        path = '/' + '/'.join(new_path)

        return path

def main():
    sol = Solution()

    test_cases = [
        ("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
        ("/a/./b/../../c/", "/c"),
        ("/a//b////c/d//././/..", "/a/b/c"),
        ("/", "/"),
        ("/./././.", "/"),
        ("/home/../../..", "/"),
        ("/a/b/c/../../../", "/"),
        ("/a/b/c/../../x/y/../z", "/a/x/z"),
    ]

    for i, (path, expected) in enumerate(test_cases):
        result = sol.simplifyPath(path)
        print(f"Test case {i+1}: {'PASS' if result == expected else 'FAIL'}")
        print(f"   Input:    {path}")
        print(f"   Expected: {expected}")
        print(f"   Result:   {result}\n")


if __name__ == "__main__":
    main()

'''
# Approach:

1. Split the given absolute path by '/' to handle directory names and filter out empty strings or current directory references ('.').
2. Use a stack (list) to process each directory:
   - If the directory is '..', pop from the stack if it’s not empty.
   - If the directory is valid (not '.' or empty), push it onto the stack.
3. Join the stack with '/' and prepend a root '/' to return the simplified canonical path.

# Time Complexity:
O(n), where n is the length of the input string. This is because we iterate over each part of the split path once.

# Space Complexity:
O(n), in the worst case, all parts are valid directories and are stored in the stack.
'''