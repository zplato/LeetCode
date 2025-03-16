from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ranges = []
        # Utilize loop 1 as the start of a range (i)
        # Utilize loop 2 to find the end of a range (j)
        i = 0
        while i < len(nums):
            start_i = nums[i]
            #print("i_index: {0}, i_num: {1}".format(i, start_i))

            # If we are on the last number, then just append it b/c its not a range if we made it here
            if i == len(nums) - 1:
                ranges.append(str(nums[i]))

            j = i + 1
            while j < len(nums):
                stop_j = nums[j]
                prev_j = nums[j - 1]
                #print(stop_j)
                #print(prev_j)
                # Check if the previous number is not sequential to current num
                if prev_j + 1 < stop_j:
                    if prev_j == start_i:
                        ranges.append(str(start_i))  # Single value to return, e.g., "0"
                        break
                    else:
                        ranges.append("{0}->{1}".format(str(start_i), str(prev_j)))
                        i = j - 1
                        break
                elif j == len(nums) - 1:
                    # hit last number
                    ranges.append("{0}->{1}".format(str(start_i), str(stop_j)))
                    i = j
                    break
                else:
                    # They are sequential, so continue
                    j += 1
                    continue
            i += 1

        print(ranges)
        return ranges


def main():
    soln = Solution()
    test_case_1 = [0,1,2,4,5,7]
    solution_1 = ["0->2","4->5","7"]
    ret = soln.summaryRanges(nums=[0,1,2,4,5,7])
    passed = (ret == solution_1)
    print("Test Case 1 | input: {0} | return {1} | solution: {2} | passed: {3}"
          .format(test_case_1, ret, solution_1, passed))

if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------------------------------------------------#

# Time Complexity: O(n) Explanation: Loops are additive so it's O(n) + O(n) = O(n)
# Space Complexity: O(n)
