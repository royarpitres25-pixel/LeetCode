# if / elif / else lets you branch based on conditions, and logical operators
# (or, and, not) let you combine multiple conditions into one check.
# (see if_elif_vs_match.py for a deeper comparison of if/elif vs match/case)

def test_function(a, b):
    # `or` -> True if AT LEAST ONE side is True
    if a < 0 or b < 0:
        print("one values are -ve")
    else:
        print(f"both of them are +ve")   # note: no need to return anything if you want void

    if a < 0:
        sum_result = add_two_number(a, b)
        print(sum_result)
    elif b < 0:                          # `elif` = "else if" - checked only if the first `if` was False
        print("this is else fi condition")
    else:
        print(" this is else case")      # runs only if NONE of the above conditions were True


def add_two_number(a, b):
    return a + b


# -----------------------------
# quick reference: logical operators
# -----------------------------
def logical_operator_examples():
    x, y = 5, -3

    print(x > 0 or y > 0)     # True  - at least one side is True
    print(x > 0 and y > 0)    # False - `and` needs BOTH sides True
    print(not (x > 0))        # False - `not` flips a boolean
    print(x > 0 and not y > 0)  # True - operators can be combined


if __name__ == "__main__":
    test_function(-1, -2)   # a < 0 and b < 0 -> "one values are -ve", then hits `if a < 0` branch
    test_function(1, 2)     # both +ve -> "both of them are +ve", then hits the final `else`

    print("--------------------")
    logical_operator_examples()

# -----------------------------
# summary
# -----------------------------
# - if / elif / else: checked top to bottom, first True branch wins, else runs if none matched
# - `or`  -> True if at least one condition is True
# - `and` -> True only if ALL conditions are True
# - `not` -> flips True/False
# - you can nest if-blocks inside each other (as in test_function above)
