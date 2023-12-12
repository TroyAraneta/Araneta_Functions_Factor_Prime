def smallest_factor(integer):
    for num in range(2, integer):
        factor = integer % num
        if factor == 0:
            print(f"The smallest factor other than 1 for {integer} is {num}")
            break
    else:
        print(f"{integer} is a prime number")



def prime(start_num, end_num):
    print(f"Prime numbers between {start_num} and {end_num} are: ", end="")
    for num in range(start_num, end_num + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=" ")
    print("\n")


p_or_f = int(input("[1] Find the smallest Factor of number"
                   "\n[2] Find the Prime Numbers within the range"
                   "\n Choose an Option: "))
if p_or_f == 1:
    integer = int(input("Enter an integer >= 2: "))
    if integer <= 2:
        print("Invalid input. Enter a number greater than 2.")
    smallest_factor(integer)
elif p_or_f == 2:
    while True:
        StartNum = int(input("Enter a number [start]: "))
        if StartNum == 0:
            break
        elif StartNum < 0:
            print("Enter non-negative numbers.\n ")
            continue
        EndNum = int(input("Enter a number [end]: "))

        if EndNum < 0:
            print("Enter non-negative numbers.\n ")
        elif EndNum <= StartNum:
            print(f"Enter a number greater than {StartNum}.\n ")
        else:
            prime(StartNum, EndNum)
