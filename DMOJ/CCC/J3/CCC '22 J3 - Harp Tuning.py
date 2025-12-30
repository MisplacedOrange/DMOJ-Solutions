def main():

    harp = str(input())
        
    strings = ""
    tune = ""
    instruct = ""

    for char in harp:
        if char.isupper():
            if instruct and tune:
                print(f"{strings} {instruct} {tune}")
                strings = ""
                tune = ""
                instruct = ""
            strings += char
        elif char.isdigit():
            tune += char
        elif char == '-':
            instruct = "loosen"
        elif char == '+':
            instruct = "tighten"
    print(f"{strings} {instruct} {tune}")
        
main()