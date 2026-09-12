# Functions in Python are defined with `def`, and f-strings are the standard
# way to build formatted strings that embed variable values.

# -----------------------------
# 1) defining a function that returns a value
# -----------------------------
def add_two_number(a, b):              # parameters a, b - no type annotations required
    print("hello")
    print(f"the sum is: {a + b}")      # f-string: put an expression inside {} and it
                                        # gets evaluated and inserted into the string.
                                        # (like $"the sum is: {a+b}" in C#, or
                                        #  `the sum is: ${a+b}` template literals in JS)
    return a + b                       # `return` sends a value back to the caller


# -----------------------------
# 2) a "void" function - no return statement needed if you don't want a value back
# -----------------------------
def greet(name):
    print(f"Hello, {name}!")           # just does something, doesn't return anything
    # implicitly returns None here


# -----------------------------
# 3) more f-string tricks
# -----------------------------
def fstring_examples():
    pi = 3.14159
    name = "Arpit"
    count = 3

    print(f"Hi {name}")                        # simple variable substitution
    print(f"Pi rounded: {pi:.2f}")             # format spec: 2 decimal places -> 3.14
    print(f"{name} has {count} items")          # multiple variables in one string
    print(f"Upper: {name.upper()}")             # you can call methods inside {}
    print(f"Math: {2 + 3 * 4}")                 # you can even do full expressions


if __name__ == "__main__":
    sum_result = add_two_number(10, 20)   # sum_result holds the returned value
    print(sum_result)

    greet("Arpit")                        # this returns None, but we don't use it here

    print("--------------------")
    fstring_examples()

# -----------------------------
# summary
# -----------------------------
# - `def function_name(params): ...` defines a function
# - `return value` sends data back; without `return`, the function returns None
# - f-strings: f"...{expression}..." - cleanest way to build strings with variables
#   - supports format specs like {value:.2f} for 2 decimal places
#   - supports calling methods/expressions directly inside the braces
