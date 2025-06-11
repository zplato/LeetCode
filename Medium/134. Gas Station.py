from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        """
        What we know:
          1. need to make one full round trip starting at any gas station, where full trip length = len(gas)
          2. gas at station i, costs cost[i] to move from it to the NEXT gas station
          3. to make it to next gas station, compute curr_gas - cost[i], if <= 0, then continue, else move on

        Approach:
            Iterate over range of 0, len(gas), checking if its possible to start at this position and complete. Utilize another loop to check the path at that starting position. Use Modulo operator to treat list as a circular structure
            Return index i upon first completion, if no completions return -1
        """

        # If sum of all gas is less than the sum of the costs, then we can confidently say its impossible to travel to all gas stations given there isn't enough gas to support the cost.
        if sum(gas) < sum(cost):
            return -1

        curr_gas = 0
        start_index = 0

        # greedy approach, find gas station index that provides the most gas
        # we know a solution is possible, given sum(gas) > sum(cost) - we are garunteed a unique solution too
        # As soon as we can't continue from teh current start, we move to the next station, resetting curr_tank.
        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                start_index = i + 1
                curr_gas = 0

        return start_index

"""
Time Complexity - O(n) 
Space Complexity - O(1)
"""

