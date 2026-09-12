# `for` loops in Python usually iterate over `range(...)`, which generates a
# sequence of numbers without you having to manage a counter variable yourself.
#
# range(stop)                 -> 0, 1, ..., stop-1
# range(start, stop)           -> start, start+1, ..., stop-1
# range(start, stop, step)     -> start, start+step, ... (stops before reaching stop)
#   - start is INCLUSIVE, stop is EXCLUSIVE, step defaults to 1

def basic_range():
    for i in range(5):                     # equivalent to range(0, 5, 1) -> 0,1,2,3,4
        print(f"this is {i}th loop")


def range_with_start_stop_step_positive():
    for i in range(0, 5, 2):               # start=0 (inclusive), stop=5 (exclusive), step=2
        print(f"this is {i}th loop")       # -> 0, 2, 4


def range_with_bigger_step():
    for i in range(0, 10, 4):              # step of 4
        print(f"this is {i}th loop")       # -> 0, 4, 8


def range_counting_down():
    for i in range(5, 0, -1):              # negative step -> counts DOWN
        print(f"this is {i}th loop")       # -> 5, 4, 3, 2, 1 (stops before 0)


if __name__ == "__main__":
    basic_range()
    print("--------------------")
    range_with_start_stop_step_positive()
    print("--------------------")
    range_with_bigger_step()
    print("--------------------")
    range_counting_down()

# -----------------------------
# summary
# -----------------------------
# - range(stop)               : 0 up to (not including) stop
# - range(start, stop)        : start up to (not including) stop
# - range(start, stop, step)  : jumps by `step` each time (can be negative to count down)
# - the "stop" value is NEVER included in the output
