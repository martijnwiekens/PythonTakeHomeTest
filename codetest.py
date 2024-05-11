# The different numbers we can divide by, with the corresponding str if the 
# number can by divided by it
#
dividableNumbers: dict[int, str] = {
    3: "Fizz",
    5: "Buzz",
    7: "Fool",
}


def checkNumber(inputNumber: int) -> str:
    # Remember how many numbers work
    result = ""

    # Walk through all the numbers we can divide by
    for dn, replaceNumberWith in dividableNumbers.items():
        if inputNumber % dn == 0:
            result += replaceNumberWith

    # Check if we have any result
    if result != "":
        return result

    # Otherwise print the number
    return str(inputNumber)


if __name__ == "__main__":
    # Walk through the numbers from 1 to 100
    for x in range(1, 101):
        print(checkNumber(x))

    assert checkNumber(1) != "Fizz"
    assert checkNumber(2) == "2"
    assert checkNumber(3) == "Fizz"
    assert checkNumber(5) == "Buzz"
    assert checkNumber(7) == "Fool"
    assert checkNumber(9) == "Fizz"
    assert checkNumber(15) == "FizzBuzz"
    assert checkNumber(70) == "BuzzFool"
