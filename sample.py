
def FizzBuzz(value):
    if value%5 ==0 and value%3 ==0:
        return "FizzBuzz"
    elif value%5==0:
        return "Buzz"
    elif value%3==0:
        return "Fizz"

    else:
        return value