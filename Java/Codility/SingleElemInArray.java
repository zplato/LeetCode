// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // Implement your solution here

        // Approach 1 - Utilize a Hashmap where we store the occurence of each num
        // If map[num] == 2 then its a pair, else its not and return that element
        int soln = 0;
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int num : A) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // Now iterate through the map and find the key by the value
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() % 2 == 1)
            {
                return entry.getKey();
            }
        }

        throw new IllegalArgumentException("No single element found");
    }
}