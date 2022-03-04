def isalnum(x):
    for i in range(len(x)):
        i += 1
        if x[i - 1].isalnum() == True:
            print("True")
            break
        else:
            if i == len(x):
                print("False")
                break

            elif i != len(x):
                pass

            else:
                print("False")
                break

def isalpha(x):
    for i in range(len(x)):
        i += 1
        if x[i - 1].isalpha() == True:
            print("True")
            break
        else:
            if i == len(x):
                print("False")
                break
            
            elif i != len(x):
                pass

            else:
                print("False")
                break

def isdigit(x):
    for i in range(len(x)):
        i += 1
        if x[i - 1].isdigit() == True:
            print("True")
            break
        else:
            if i == len(x):
                print("False")
                break
            
            elif i != len(x):
                pass

            else:
                print("False")
                break

def islower(x):
    for i in range(len(x)):
        i += 1
        if x[i - 1].islower() == True:
            print("True")
            break
        else:
            if i == len(x):
                print("False")
                break
            
            elif i != len(x):
                pass

            else:
                print("False")
                break

def isupper(x):
    for i in range(len(x)):
        i += 1
        if x[i - 1].isupper() == True:
            print("True")
            break
        else:
            if i == len(x):
                print("False")
                break
            
            elif i != len(x):
                pass

            else:
                print("False")
                break

if __name__ == '__main__':
    s = input()

    isalnum(s)
    isalpha(s)
    isdigit(s)
    islower(s)
    isupper(s)



