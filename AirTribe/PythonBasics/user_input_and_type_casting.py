# input() reads a line typed by the user - it ALWAYS returns a string,
# even if the user types a number. To use it as a number, you must
# explicitly convert ("cast") it, e.g. with int() or float().

def read_array_length():
    # input("prompt") shows the prompt text, then waits for the user to type + press Enter
    length = int(input("length of an array : "))   # int(...) casts the string "5" -> the number 5
    # without int(), `length` would be the string "5" and `range(length)` would error out

    for i in range(0, length, 1):
        print("Array at i = ", i)


def type_casting_examples():
    # input() always gives you back a str - here we simulate what it returns
    raw_text = "42"                 # imagine this came from input()

    as_int = int(raw_text)          # "42" -> 42       (whole numbers)
    as_float = float(raw_text)      # "42" -> 42.0     (decimal numbers)
    as_str_again = str(as_int)      # 42   -> "42"     (back to string)

    print(raw_text, type(raw_text))
    print(as_int, type(as_int))
    print(as_float, type(as_float))
    print(as_str_again, type(as_str_again))

    # gotcha: int("3.5") would crash (ValueError) - int() can't parse decimal text directly.
    # you'd need float("3.5") first, then int(float("3.5")) if you want to truncate it to 3.


if __name__ == "__main__":
    type_casting_examples()
    print("--------------------")
    read_array_length()   # this one will actually prompt you for input when run

# -----------------------------
# summary
# -----------------------------
# - input("prompt") -> always returns a str, no matter what the user types
# - int(x)   -> converts to a whole number (crashes on non-numeric or decimal-looking text)
# - float(x) -> converts to a decimal number
# - str(x)   -> converts back to a string
# - always cast input() before doing math with it, or you'll get type errors
#   (e.g. "5" + "3" gives "53", not 8, because + on strings means "concatenate")
