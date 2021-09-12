import random

def is_prime(number):
    if number < 2:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
                break
        else:
            return True

def prime_array(*array):
    new_array = [x for x in array if is_prime(x)]
    return new_array

if __name__ == '__main__':
    initial = []
    for i in range(random.randint(5, 20)):
        initial.append(random.randint(0, 100))

    print(f"Initial Array: {initial}")
    print(f"Prime Array: {prime_array(*initial)}")