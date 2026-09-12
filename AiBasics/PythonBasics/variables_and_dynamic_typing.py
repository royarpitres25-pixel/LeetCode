# Python variables don't need a declared type - the type is attached to the
# VALUE, not the variable name. This is called "dynamic typing".
# You can even reassign the same variable to a completely different type.

# -----------------------------
# 1) basic variable assignment
# -----------------------------
a = 5                       # a is now an int
print(a, type(a))           # type() tells you the current type of a value

b = "this is Arpit"         # b is a str (string)
print(b, type(b))

# -----------------------------
# 2) reassigning a variable to a different type - totally legal in Python
# -----------------------------
c = 10                      # c starts as an int
print(c, type(c))

c = "will this work ?"      # now c is a str - Python doesn't complain
print(c, type(c))

# note: this is different from statically typed languages (C#, Java, C++)
# where a variable's type is fixed once declared (e.g. `int c = 10;`
# then `c = "text";` would be a compile error there, but not here).

# -----------------------------
# 3) other common types, just for reference
# -----------------------------
d = 3.14                    # float
e = True                    # bool
f = None                    # None = Python's "no value" (like null/nil)
g = [1, 2, 3]                # list
h = (1, 2, 3)                # tuple
i = {"key": "value"}         # dict

if __name__ == "__main__":
    print(d, type(d))
    print(e, type(e))
    print(f, type(f))
    print(g, type(g))
    print(h, type(h))
    print(i, type(i))

# -----------------------------
# summary
# -----------------------------
# - no need to write `int a = 5` - just `a = 5`
# - the same name can point to an int, then a string, then a list, etc.
# - use type(x) whenever you want to check what a value currently is
# - dynamic typing = flexible but be careful: reassigning types can hide bugs
#   if you expect a variable to always hold one kind of value
