// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {

    public int[] solution(int[] A, int K) {

        // First approach
        // Utilize a Modulo operation - Since rotation (n) times brings the array back to the original state, k can be reduced to k % n
        // Rotate by 1, K times - utilize for loop

        // K %= A.length; // this is because K % A just repeats, so we are capped at the length of A
        // int temp, prev;
        // for (int i = 0; i < K; i++)
        // {
        //     // Get the last char nums[-1]
        //     prev = A[A.length - 1];

        //     // Rotate by 1
        //     for (int j = 0; j <A.length; j++)
        //     {
        //         temp = A[j]; // Store the current num
        //         A[j] = prev;
        //         prev = temp;
        //     }
        // }

        // Approach 2 - Using Reverse
        // k elements from back end of array come to the front and the rest of the elemtns from the front shift backwards
        // In this approach, we reverse all elements of the array. Then reversing the first k elements followed by reversing the rest n-k elements
        if (A.length == 0 || A.length % K == 0)
            return A;

        K %= A.length;
        reverse(A, 0, A.length-1); // Reverse the whole array
        reverse(A, 0, K-1);
        reverse(A, K, A.length-1);

        return A;
    }

    //Helper function which reverses an array
    private void reverse(int[] A, int left, int right)
    {
        // Walk throught the array using 2 pointers, and swap values
        while (left < right) {
            int temp = A[left];
            A[left] = A[right];
            A[right] = temp;
            left++;
            right --;

        }
    }
}