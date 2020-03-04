from sample import FizzBuzz
def test_fizzbuzz():
    assert FizzBuzz(15)=="FizzBuzz"

def test_buzz():
    assert FizzBuzz(5)=="Buzz"

def test_fizz():
    assert FizzBuzz(3)=="Fizz"

def test_nothing():
    assert FizzBuzz(2)==2