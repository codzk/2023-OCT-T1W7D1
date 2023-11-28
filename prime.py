# if a number is prime or not

def is_prime(number):
    for i in range (2, number):
        if (number % i == 0) :
            print ("not a prime")
            break

    else:
        print("a prime")

is_prime(5)
is_prime(55)
