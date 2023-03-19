# Developer notes for me:
# -Will work on adding more variables later but this will require a better sorting algorithm
# -Remember to keep the repo upto date in case anything fails or stops working or any hardware issues
# -Remember to study so you can correctly apply Gause and Gause-Jordan :skull:


# | Progam functions start here |
# v                             v

# Function to sort equation into an array
def sort(equation):
    x = equation
    # Array to be returned later
    terms = []
    # Temporary variable to hold value of the terms
    tempvar = " "

    # Starts the sorting process
    for letter in x:
        if letter == 'x' or letter == 'X':
            tempvar = ""
            for letter1 in x:
                # Takes input until letter1 equals x
                if letter1 != letter:
                    tempvar+= letter1
                else:
                    # Pushes x and breaks the inner loop
                    tempvar += letter1
                    break
            # Pushes this current term
            terms.append(tempvar)

        if letter == 'y' or letter == 'Y':
            tempvar = ""
            for letter1 in x:
                # Takes input until letter1 equals y
                if letter1 != letter:
                    tempvar+= letter1
                else:
                    # Pushes y and breaks the inner loop
                    tempvar += letter1
                    break
            # Replaces the first terms with non then pushes this current term
            terms.append(tempvar.replace(terms[0],""))
        if letter == 'z' or letter == 'Z':
            tempvar = ""
            for letter1 in x:
                # Takes input until letter1 equals z
                if letter1 != letter:
                    tempvar+= letter1
                else:
                    # Pushes z and breaks the inner loop
                    tempvar += letter1
                    break
                # Replaces the first terms with non then pushes this current term
            terms.append(tempvar.replace(terms[1],"").replace(terms[0],""))

    # Getting ready to push result of equation
    tempvar = str(x)
    for item in terms:
        # Replaces everything before result by non
        tempvar =tempvar.replace(item,"")
    tempvar = tempvar.replace("=","")
    # Pushes result into array
    terms.append(tempvar)

    # Replaces all veriables so we end up with just numbers to be converted later on
    for item in terms:
        index = terms.index(item)
        item = item.replace('x','')
        item = item.replace('y','')
        item = item.replace('z','')
        item = item.replace('X','')
        item = item.replace('Y','')
        item = item.replace('Z','')
        terms[index] = item
        print(item)

    # Array/List representing one row of an augmented matrix
    equationArr = [terms[0],terms[1],terms[2],terms[3]]
    return equationArr

def toAugmented():
    # Placeholder equation incase userinput isn't possible
    xIn = "x+y+z=0"
    # Augmented matrix goes here 
    mainMatrix =[]
    # Takes user input of 3 items, will be variable later after some testing of later algorithms
    for n in range(3):
        try:
            xIn = input("Enter equation: ")
            mainMatrix.append(sort(xIn))
        except:
            print("Input failed")
    # Shape of matrix now
    # |-             -|
    # | x1 y1 z1 : r1 |
    # | x2 y2 z2 : r2 |
    # | x3 y3 z3 : r3 |
    # |_             -|
    return mainMatrix

print(toAugmented())

