def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result) 
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

def main():
    try: 
        num = int(input("Enter a number:  "))
        while num != 1:
            num = collatz(num)
    except ValueError:
        print("Please enter a valid integer. ")

main()
    
    
    
