The Collatz conjecture is an example of a simple computational process whose behavior is so unpredictable 
that the world's best mathematicians still don't understand it.

Consider the simple function f(n)f(n) (as defined in the Wikipedia page above) 
that takes an integer nn and divides it by two if nn is even and multiplies nn 
by 33 and then adds one to the result if nn is odd.
The conjecture involves studying the value of expressions of the 
form f(f(f(...f(f(n)))))f(f(f(...f(f(n))))) as the number of calls to the function ff increases. 
The conjecture is that, for any non-negative integer nn, 
repeated application of ff to nn yields a sequence of integers that always includes 11.

Your task for this question is to implement the Collatz function ff in Python. 
The key to your implementation is to build a test that determines whether nn
is even or odd by checking whether the remainder when nn is divided by 22 is either zero or one. 
Hint: You can compute this remainder in Python using the remainder opertor \color{red}{\verb|%|}% via the 
    expression \color{red}{\verb|n % 2|}n%2. Note you will also need to use integer division \color{red}{\verb|//|}// when computing ff.

Once you have implemented ff, test the your implementation on the expression 
f(f(f(f(f(f(f(674)))))))
This expression should evaluate to 190. 
Finally, compute the value of the expression
f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))
and enter the result below as an integer. 
Remember to use copy and paste when moving the expressions above into your Python environment. 
Never try to retype expressions by hand.


def f(num):
    if num%2==0:
        return num//2 # 5/2 -- 2.5  5//2- 2
    else:
        return (num*3) +1



print(f(f(f(f(f(f(f(674))))))))

print(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071)))))))))))))))

