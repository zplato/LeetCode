/ you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int N) {

        // Implement your solution here
        int longest_gap = 0;
        int curr = 0;
        boolean prevOne = false;
        String binaryString = Integer.toBinaryString(N);
        // Check for preceeding 1, if there is a one, count number of zeros until we get to another 1
        // that one we get to can also be preceeding 1

        for (char c : binaryString.toCharArray())
        {
            if (c == '1'){
                if (prevOne && curr > longest_gap)
                {
                    longest_gap = curr;
                }

                prevOne = true;
                curr = 0;

            }
            else if (prevOne && c == '0')
                curr++;

        }




        return longest_gap;
    }
}