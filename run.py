# Developer notes for me:
# -Will work on adding more variables later but this will require a better sorting algorithm
# -Remember to keep the repo upto date in case anything fails or stops working or any hardware issues
# -Remember to study so you can correctly apply Gause and Gause-Jordan :skull:
# -Remember to add a row echlon function to order the matrix for the Gause function
# -Stop with the stupid mistakes please :sob:


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

# Converts the string matrix to a integer matrix
def toIntegerMatrix(stringMatrix):
    # Main matrix containing all numbers
    mainMatrix = []
    # Loops through rows of the string matrix
    for matrix in stringMatrix:
        # Temporary matrix to store the row
        innerMatrix = []
        for value in matrix:
            # Pushes each value into the row matrix after converting value to integer
            innerMatrix.append(int(value))
        # Pushes the row matrix to the main matrix
        mainMatrix.append(innerMatrix)
    return mainMatrix

# Function to add and multiply rows for gause-elimnation
def addAndMultiplyRows(row1, row2, rowNumber, multiplicate):
    # Final row to be returned
    rowRes = []
    # If row 1 is the one being multiplied
    if rowNumber == 1:
        for value in row1:
            # Pushes every value as the value*the multiplicate
            rowRes.append(value*multiplicate)
        row2Final = row2
        # Adds rows
        rowRes[0] = rowRes[0] + row2Final[0]
        rowRes[1] = rowRes[1] + row2Final[1]
        rowRes[2] = rowRes[2] + row2Final[2]
        rowRes[3] = rowRes[3] + row2Final[3]
    else:
        for value in row2:
            # Pushes every value as the value*the multiplicate
            rowRes.append(value*multiplicate)
            row1Final = row1
        # Adds rows
        rowRes[0] = rowRes[0] + row1Final[0]
        rowRes[1] = rowRes[1] + row1Final[1]
        rowRes[2] = rowRes[2] + row1Final[2]
        rowRes[3] = rowRes[3] + row1Final[3]
    return rowRes

# Function to multiply row by a value, will be used to get an all 1s diagonal
def changeRowValue(row, multiplicate):
    # Row to store new values
    rowRes = []
    # Loops and multiplies row values by multiplicate
    for n in range(4):
        rowRes.append(row[n] * multiplicate)
    return rowRes

# Function to display matrix
def display(matrix):
    for row in matrix:
        print(row, "\n")

# Function to solve using Gause-Elimination
def GauseElimination(matrix):
    # Resultant Matrix
    resMat = []
    # Changes x of row 1 to 1 & pushes first row
    x1 = (matrix[0])[0]
    resMat.append(changeRowValue(matrix[0],1/x1))
    # Changes x of row 2 to 0
    x2 = (matrix[1])[0]
    r2 = addAndMultiplyRows(resMat[0],matrix[1],1,-x2)
    # Changes y of row 2 to 1
    y2 = r2[1]
    r2 = changeRowValue(r2,1/y2)
    # Pushes second row
    resMat.append(r2)
    # Changes x of row 3 to 0
    x3 = (matrix[2])[0]
    r3 = addAndMultiplyRows(resMat[0],matrix[2],1,-x3)
    # Changes y of row 3 to 0
    y3 = r3[1]
    r3 = addAndMultiplyRows(resMat[1],r3,1,-y3)
    # Changes z of row 3 to 1
    z3 = r3[2]
    if z3 != 0:
        r3 = changeRowValue(r3,1/z3)
    resMat.append(r3)
    display(resMat)
matrix = [[1,-2,3,9],[0,1,3,5],[0,0,1,2]]

GauseElimination(matrix)