import sys

class Pass:
    def __init__(self, filename):
        try:
            self.filename = filename
            with open(filename, 'r') as file:
                self.lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            sys.exit(1)
    
    def readlines(self):
        lines = [line.strip() for line in self.lines]
        return lines
    

class Compare(Pass):
    def __init__(self, passkey):
        self.passkey = passkey
        super().__init__("passwords/1000000.txt")
    
    def lengthcheck(self):
        return len(self.passkey) >= 5
    
    def compare(self):
        lines = self.readlines()
        for line in lines:
            if self.passkey in line:
                return True
        return False
    

def main():
    if len(sys.argv) == 2:
        thepass = sys.argv[1]
    elif len(sys.argv) == 1:
        thepass = input("Enter your password: ")
    else:
        print("Too many arguments")
        sys.exit(1)
    
    comp = Compare(thepass)
    if not comp.lengthcheck():
        print("Your password is too short(at least 5 characters)")
        sys.exit(1)
    
    if comp.compare():
        print("Your password is weak")
    else: 
        print("Your password is not in the top 1000000")


if __name__ == "__main__":
    main()
