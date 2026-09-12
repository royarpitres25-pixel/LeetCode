#pragma once
#include <vector>
#include <iostream>
#include <string>

// Shared assertion/printing helper for the base-code test harnesses, so each
// problem's driver file doesn't have to reimplement compare-and-print logic.
class TestUtils {
public:
    static void expectEqual(const std::string& testName, const std::vector<int>& expected, const std::vector<int>& actual)
    {
        bool passed = expected.size() == actual.size();
        for (size_t i = 0; passed && i < expected.size(); i++)
        {
            if (expected[i] != actual[i])
                passed = false;
        }

        std::cout << testName << ": " << (passed ? "PASSED" : "FAILED") << std::endl;
        std::cout << "  Expected: " << toString(expected) << std::endl;
        std::cout << "  Actual:   " << toString(actual) << std::endl;
    }

    static void expectEqual(const std::string& testName, int expected, int actual)
    {
        bool passed = expected == actual;
        std::cout << testName << ": " << (passed ? "PASSED" : "FAILED") << std::endl;
        std::cout << "  Expected: " << expected << std::endl;
        std::cout << "  Actual:   " << actual << std::endl;
    }

private:
    static std::string toString(const std::vector<int>& values)
    {
        std::string result = "[";
        for (size_t i = 0; i < values.size(); i++)
        {
            result += std::to_string(values[i]);
            if (i + 1 < values.size())
                result += ", ";
        }
        result += "]";
        return result;
    }
};
