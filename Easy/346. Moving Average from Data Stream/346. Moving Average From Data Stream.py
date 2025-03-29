class MovingAverage:
    """
    Problem:
    Design a class that calculates the moving average of the last `size` elements from a stream of integers.

    Approach:
    - Initialize an empty list `window` to store the current elements in the window.
    - Keep track of the number of elements in the window with `count`.
    - For each call to `next(val)`:
        - If the window is not yet full, append the new value.
        - If the window is full, remove the oldest value (pop from the front) and append the new value.
        - Return the average of the current window by summing and dividing by the count.

    Time Complexity: O(k) for each call to `next()`, where k = size of the window (due to sum).
    Space Complexity: O(k), storing up to `size` elements in memory.
    """

    def __init__(self, size: int):
        self.size = size
        self.window = []
        self.count = 0

    def next(self, val: int) -> float:
        if self.count < self.size:
            self.window.append(val)
            self.count += 1
        else:
            self.window.pop(0)  # Remove the oldest element
            self.window.append(val)

        return sum(self.window) / self.count


def main():
    m = MovingAverage(3)
    test_stream = [1, 10, 3, 5]
    expected_results = [1.0, (1 + 10) / 2, (1 + 10 + 3) / 3, (10 + 3 + 5) / 3]

    print("Testing MovingAverage with window size 3:")
    for i, val in enumerate(test_stream):
        result = m.next(val)
        expected = expected_results[i]
        print(f"Input: {val}, Output: {result:.4f}, Expected: {expected:.4f}")
        assert abs(result - expected) < 1e-5, f"Test failed at input {val}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()