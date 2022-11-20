import math
# Error Code to signify a value is uncomputable
cannot_be_computed = -1


class advanced_calculator:
    def __init__(self):
        print("Initialising Advanced Calculator....\nInitialisaiton Successful")

    def sqroot(self, a):
        print("Computing square root of : ", a)
        # Deliberately putting a case for fail, a calculator should throw error
        if (a < 0):
            return 0
        return math.sqrt(a)

    def factorial(self, a):
        print("Computing factorial of ", a)
        result = 1
        # Do note for negative numbers answer will be 1 and hasnt been handled
        for i in range(1, a+1):
            result *= i
        return result

    def natural_log(self, a):
        print("Computing natural log of: ", a)
        # Handling the case of -ve numbers and 0 as expected
        if (a <= 0):
            return cannot_be_computed
        else:
            return math.log(a)

    def power(self, a, b):
        print("Computing power of: ", a)
        # Should work as expected
        return math.pow(a, b)
