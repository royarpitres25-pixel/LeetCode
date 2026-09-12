// Black-box driver for LeetCode 303: Range Sum Query - Immutable.
// This file plays the role LeetCode's judge normally plays: it supplies the
// standard includes/using directive, pulls in your solution class as-is,
// runs it through the example plus corner cases, and owns main().
//
// solutions/prefixsum/RangeSumQueryImmutable303.cpp should never need to
// change to be tested here.

#include <vector>
#include <iostream>
#include <string>
using namespace std;

#include "../../solutions/prefixsum/RangeSumQueryImmutable303.cpp"
#include "../common/TestUtils.h"

class RangeSumQueryImmutable303Tests {
public:
    static void run()
    {
        exampleFromProblem();
        singleElementArray();
        sumRangeWithLeftEqualsRight();
        fullRangeSum();
        boundaryValueMagnitudes();
        overlappingAdjacentRanges();
    }

private:
    // Example 1 from the problem statement.
    static void exampleFromProblem()
    {
        vector<int> nums = { -2, 0, 3, -5, 2, -1 };
        NumArray numArray(nums);

        vector<int> expected = { 1, -1, -3 };
        vector<int> actual = {
            numArray.sumRange(0, 2),
            numArray.sumRange(2, 5),
            numArray.sumRange(0, 5)
        };

        TestUtils::expectEqual("Example from problem statement", expected, actual);
    }

    // Corner case: nums.length == 1 (minimum allowed size).
    static void singleElementArray()
    {
        vector<int> nums = { 42 };
        NumArray numArray(nums);

        vector<int> expected = { 42 };
        vector<int> actual = { numArray.sumRange(0, 0) };

        TestUtils::expectEqual("Single element array", expected, actual);
    }

    // Corner case: left == right should just return nums[i] for several indices.
    static void sumRangeWithLeftEqualsRight()
    {
        vector<int> nums = { 5, -3, 8, 0, -7 };
        NumArray numArray(nums);

        vector<int> expected = { 5, -3, 8, 0, -7 };
        vector<int> actual = {
            numArray.sumRange(0, 0),
            numArray.sumRange(1, 1),
            numArray.sumRange(2, 2),
            numArray.sumRange(3, 3),
            numArray.sumRange(4, 4)
        };

        TestUtils::expectEqual("sumRange with left == right", expected, actual);
    }

    // Corner case: left == 0 and right == last index (whole array).
    static void fullRangeSum()
    {
        vector<int> nums = { 1, 2, 3, 4, 5 };
        NumArray numArray(nums);

        vector<int> expected = { 15 };
        vector<int> actual = { numArray.sumRange(0, 4) };

        TestUtils::expectEqual("Full range sum", expected, actual);
    }

    // Corner case: values at the extremes of the constraint (-10^5..10^5).
    static void boundaryValueMagnitudes()
    {
        vector<int> nums = { -100000, 100000, -100000, 100000 };
        NumArray numArray(nums);

        vector<int> expected = { 0, 0, 100000 };
        vector<int> actual = {
            numArray.sumRange(0, 1),
            numArray.sumRange(0, 3),
            numArray.sumRange(1, 1)
        };

        TestUtils::expectEqual("Boundary value magnitudes", expected, actual);
    }

    // Corner case: repeated queries sliding across overlapping ranges.
    static void overlappingAdjacentRanges()
    {
        vector<int> nums = { 4, -1, 2, -3, 5, 6, -2 };
        NumArray numArray(nums);

        vector<int> expected = { 3, 1, -1, 2, 11, 4 };
        vector<int> actual = {
            numArray.sumRange(0, 1),
            numArray.sumRange(1, 2),
            numArray.sumRange(2, 3),
            numArray.sumRange(3, 4),
            numArray.sumRange(4, 5),
            numArray.sumRange(5, 6)
        };

        TestUtils::expectEqual("Overlapping adjacent-pair ranges", expected, actual);
    }
};

int main()
{
    RangeSumQueryImmutable303Tests::run();
    return 0;
}
