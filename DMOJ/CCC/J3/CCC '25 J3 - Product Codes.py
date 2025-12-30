def main():
    
    productcodes = int(input())

    for i in range(0, productcodes):
        code = str(input())
        sum = 0
        upper = ""
        num = ""
        
        for char in code:
            if char.isupper():
              upper += char
            if char.isdigit():
              num += char
            elif char == '-':
                if num != "": # full
                    sum += int(num) # clear
                num = '-' # setup
            else:
                if num != "": # full
                    sum += int(num) #clear
                    num = "" # set up
        if num != "": # just incase if last digit is int
            sum += int(num) 
        print(f"{upper}{sum}")
main()