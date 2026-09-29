def max(array):
    current_max = array[0]
    for number in array:
        if number > current_max:
            current_max = number

    return current_max


def min(array):
    current_min = array[0]
    for number in array:
        if number < current_min:
            current_min = number

    return current_min


array = list()
while True:
    user_input = input(
        "Please enter a number to add to your list of numbers or type 'no' to stop: ")
    if user_input == "no":
        break
    else:
        array.append(int(user_input))

print(f"Your given list is: {array}.")
print(f"The maximum value in your array is: {max(array)}.")
print(f"The minimum value in your array is: {min(array)}.")
