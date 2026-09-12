# Python has two ways to branch on multiple conditions: if/elif/else and match/case
# This file shows both doing the same job, so you can see how they differ

# -----------------------------
# 1) if / elif / else
# -----------------------------
# - works with ANY condition/expression (ranges, multiple variables, function calls etc.)
# - checks conditions top to bottom, stops at first True
def check_status_if(status):
    if status == 200:
        print("OK")
    elif status == 404:
        print("Not Found")
    elif status == 500:
        print("Server Error")
    elif 400 <= status < 500:          # if/elif is great for ranges like this
        print("Some other client error")
    else:
        print("Unknown status")


# -----------------------------
# 2) match / case (python's version of switch, added in 3.10)
# -----------------------------
# - matches a value against PATTERNS, not just plain conditions
# - reads cleaner when you have many exact values to compare against
# - "case x:" with a plain variable name acts like the default/else
def check_status_match(status):
    match status:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Server Error")
        case _ if 400 <= status < 500:   # you CAN do ranges too, using a guard (if condition)
            print("Some other client error")
        case _:                          # "_" is the wildcard/default case
            print("Unknown status")


# -----------------------------
# where match really shines: pattern matching on structure (not just if/elif)
# -----------------------------
def describe_point(point):
    match point:
        case (0, 0):
            print("origin")
        case (0, y):                    # binds y automatically
            print(f"on the y-axis at {y}")
        case (x, 0):                    # binds x automatically
            print(f"on the x-axis at {x}")
        case (x, y):
            print(f"point at ({x}, {y})")
        case _:
            print("not a point")


if __name__ == "__main__":
    for s in [200, 404, 500, 403, 999]:
        check_status_if(s)
        check_status_match(s)
        print("---")

    describe_point((0, 0))
    describe_point((0, 5))
    describe_point((5, 0))
    describe_point((3, 4))
    describe_point("not a tuple")

# -----------------------------
# summary
# -----------------------------
# if/elif  -> use for general boolean conditions, ranges, comparisons across variables
# match    -> use when comparing ONE value against several exact values or shapes/patterns
#             (dicts, tuples, classes) - it's more readable and can destructure data for you
