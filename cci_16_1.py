# CCI problem 16.1 Number swapper.  Write a funtion to swap two numbers in place (that is without temporary variable)
# i.e. a = 9, b = 4.  
def numberSwapper(a, b):
    # Add the two numbers and store it in a
    a = a + b
    # Calculate new b as the sum less original b
    b = a - b
    # Calculate new a as the new a less the new b
    a = a - b
    return (a, b)

a = 9
b = 4
print(numberSwapper(a, b))