from typing import List


def compress(chars: List[str]) -> int:
    '''
    Approach -  Iterate the input len(chars)+1, keeping a count of each char, and also a write pointer, which overwrites the input
                Each time we see the same char, increment count += 1, and if we see a new char, then write the old prev char to the list
                at position write, and increment write+1. Then, if we seen the prev more than once,
                write each digit at write position in the list, incrementing write += 1 each time.
    '''

    # Set Variables
    count = 1  # Start at 1 b/c we count the current char, chars[0]
    write = 0  # write pointer for modifying in place

    # Loop over each char, starting at char[1] (because count = 1 already we can skip char[0])
    for i in range(1, len(chars) + 1):

        # if we are not at the last character, and we've seen this one before, then increment count and continue
        if i < len(chars) and chars[i] == chars[i - 1]:
            count += 1

        # this is a new character, so we need to write the previous one to the output
        else:
            chars[write] = chars[i - 1]  # write the previous character since we are now on a new character
            write += 1  # moves to next write positon

            # If we have seen the previous character more than once, we need to write each of its digits
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

                    # Reset for next char
            count = 1

    # Uncomment for debugging
    # print(chars)  #  This will still contain extra chars from the original input list chars[],
    #  chars[:write+1] is the string compression we've written to it
    #  chars[write+1:] is what's left of the original input

    return write  # write == len(chars), which is what we've overwritten from the input list


'''
TimeComplexity  - O(n): Iterate through the input list of length n once 
SpaceComplexity - O(1): We are modifying in place so no additional space is added, using constant space
'''
