# `while` loops keep running as long as a condition stays True.
# Unlike `for i in range(...)`, YOU are responsible for updating the loop
# variable yourself - forget to do it and you get an infinite loop.

def countdown_while():
    i = 4
    while i > 0:                # keeps looping while the condition is True
        print("this is loop", i)
        i -= 1                  # without this line, `i` never changes and the
                                 # loop would run forever (infinite loop)


def while_with_break():
    # `break` exits the loop immediately, even if the condition is still True
    i = 0
    while True:                 # `while True` loops forever unless something breaks it
        if i >= 3:
            break
        print("break example, i =", i)
        i += 1


def while_with_continue():
    # `continue` skips the rest of THIS iteration and jumps back to the condition check
    i = 0
    while i < 5:
        i += 1
        if i % 2 == 0:          # skip even numbers
            continue
        print("continue example, i =", i)


if __name__ == "__main__":
    countdown_while()
    print("--------------------")
    while_with_break()
    print("--------------------")
    while_with_continue()

# -----------------------------
# summary
# -----------------------------
# - while <condition>: keeps running the block as long as <condition> is True
# - you must manually update whatever variable the condition depends on
#   (e.g. `i -= 1`) or you'll get an infinite loop
# - `break`    -> exits the loop immediately
# - `continue` -> skips to the next iteration without finishing the current one
