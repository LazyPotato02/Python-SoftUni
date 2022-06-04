def password_check(passwd):

    SpecialSym =['$', '@', '#', '%']
    val = True

    if len(passwd) < 6 or len(passwd) > 10:
        print("Password must be between 6 and 10 characters")
        val = False

    if any(char in SpecialSym for char in passwd):
        print('Password must consist only of letters and digits')
        val = False

    if len([x for x in passwd if x.isdigit()]) < 2:  
        print('Password must have at least 2 digits')
        val = False
    if val:
        return val

# Main method
def main():
    passwd = input()

    if (password_check(passwd)):
        print("Password is valid")
     
if __name__ == '__main__':
    main()