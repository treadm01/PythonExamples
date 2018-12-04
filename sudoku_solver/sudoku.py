"""This program  takes txt file inputs of sudoku puzzles and
   attempts to solve them. It prints out the original as well as the
   solved puzzles, or the details of any unsolved position
   if the puzzle is unsolved"""

import copy


def read_sudoku(file_name):
    """From the assignment's README. Takes file_name string as a parameter
	to open file_name and returns the data as a 2d list of ints"""
    stream = open(file_name)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))


def convertToSets(problem):
    """Takes the parameter problem, a 2d array of ints
    and returns a copy of it as a 2d array of sets"""
    return generic_convert(problem, set_convert)


def convertToInts(problem):
    """Takes the parameter problem, a 2d array of sets
    and returns a copy of it as a 2d array of ints"""
    return generic_convert(problem, int_convert)


def generic_convert(problem, convert_function):
    """Takes the parameters problem and convert_function. Problem
     is a 2d array of sets or ints, and the convert
     function will be a respective function to convert
     each element of problem to a specific type and value.
     A copy of the converted array is returned."""
    problem_copy = copy.deepcopy(problem)
    unknown_element = 0  # value frequently used to indicate a position in the puzzle that has not been solved
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            problem_copy[i][j] = convert_function(problem_copy[i][j], unknown_element)
    return problem_copy


def int_convert(set_to_convert, unknown_value):
    """A helper function used by convertToInts.
    Takes parameters set_to_convert, a set of ints, and
    unknown_value, the int 0 used to indicate when the
    value of a sudoku cell is unknown.
    Returns either the integer 0 to represent an unknown
    value or the int contained in a set of one element."""
    completed_cell_length = 1
    if len(set_to_convert) != completed_cell_length:
        converted_element = unknown_value
    else:
        converted_element = next(iter(set_to_convert))  # Get single element from the set
    return converted_element


def set_convert(integer_to_convert, unknown_value):
    """A helper function used by convertToSets.
    Takes parameters integer_to_convert and
    unknown_value, the int 0 used to indicate when the
    value of a sudoku cell is unknown.
    Returns either a set containing the values 1-9 if the
    value is unknown or a set containing the single int."""
    full_set = set(range(1, 10))
    if integer_to_convert == unknown_value:
        converted_element = full_set
    else:
        converted_element = {integer_to_convert}
    return converted_element


def string_convert(integer_to_convert, unknown_value):
    """A helper function used by print_sudoku.
    Takes parameters integer_to_convert and
    unknown_value, the int 0 used to indicate when the
    value of a sudoku cell is unknown.
    Returns either the string "." to represent an unknown
    value or a string of the int."""
    if integer_to_convert == unknown_value:
        element_as_string = ". "
    else:
        element_as_string = str(integer_to_convert) + " "  # convert to string, space added for formatting on output
    return element_as_string


def getRowLocations(rowNumber):
    """Takes int rowNumber for the row of the puzzle being checked and
    returns a list of tuples for that entire row"""
    return get_generic_locations(rowNumber, 9)


def getColumnLocations(columnNumber):
    """Takes int columnNumber for the column of the puzzle being checked and
    returns a list of tuples for that entire column"""
    return get_generic_locations(9, columnNumber)


def get_generic_locations(row, col):
    """takes values for the row number and column number and returns a list
    of tuples for the respective row or column"""
    locations = []
    length = 9
    for i in range(length):
        if row != length:  # if a row has been specified, return tuples for that row for all 9 columns
            locations.append((row, i))
        else:
            locations.append((i, col))  # else a column has been specified provide tuples for each row
    return locations


def getBoxLocations(location):
    """Takes parameter location a tuple for
    the row and column of the cell of the puzzle
    being checked and returns a list of tuples
    for the entire box that location is in."""
    box_size = 3
    box_locations = []

    row = box_size * (location[0] // box_size)
    column = box_size * (location[1] // box_size)

    for i in range(box_size):
        for j in range(box_size):
            box_locations.append((i + row, j + column))
    return box_locations


def eliminate(problem, location, listOfLocations):
    """Takes 3 parameters; problem, a 2d array of sets of the puzzle,
    location, a tuple of the row and column of a value to be eliminated,
    and a list of possible locations to be checked in the puzzle.
    Removes the value at location from the other sets in listOfLocations
    and returns the amount of duplicates removed."""
    num_to_remove = problem[location[0]][location[1]]  # set containing a single value to be removed
    num_of_eliminated_values = 0
    for loc in listOfLocations:
        set_to_check = problem[loc[0]][loc[1]]
        if set_to_check != num_to_remove and set_to_check.issuperset(num_to_remove):
            problem[loc[0]][loc[1]] = set_to_check.difference(num_to_remove)  # reassign difference to remove the value
            num_of_eliminated_values += 1
    return num_of_eliminated_values


def isSolved(problem):
    """Takes parameter problem a 2d array of sets of the
    current puzzle and determines whether the puzzle has
    been solved. Returns true if no location in the puzzle
    has more than one element, else false."""
    completed_set_size = 1
    solved = True
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if len(problem[i][j]) > completed_set_size:
                solved = False
                break
    return solved


def solve(problem):
    """Takes 2d array of sets problem and returns the boolean
    value from isSolved. Calls eliminate on all locations in the puzzle
    that contain one value for row, column and box locations
    until all sets are of one element and/or no more can be removed."""
    amount_removed = -1
    completed_set_size = 1
    while amount_removed != 0:
        amount_removed = 0
        for i in range(len(problem)):
            for j in range(len(problem[i])):
                if len(problem[i][j]) == completed_set_size:  # If set is complete, remove value from other locations
                    amount_removed += eliminate(problem, (i, j), getRowLocations(i))
                    amount_removed += eliminate(problem, (i, j), getColumnLocations(j))
                    amount_removed += eliminate(problem, (i, j), getBoxLocations((i, j)))
    return isSolved(problem)


def print_sudoku(problem):
    """Takes 2d array of ints and prints them out
    in the form of a sudoku puzzle"""
    horizontal_divider = "+" + "-------+" * 3 + "\n"
    problem_string = generic_convert(problem, string_convert)  # get copy of array with string values
    puzzle_string = ""  # string to hold all the output

    for row in range(len(problem)):
        puzzle_string += print_on_third(row, horizontal_divider)  # add horizontal_divider every third row
        for col in range(len(problem[row])):
            puzzle_string += print_on_third(col, "| ")  # add box divider every third column
            puzzle_string += problem_string[row][col]  # add number from the puzzle location
        puzzle_string += "|\n"  # add last divider for each line
    print(puzzle_string + horizontal_divider)  # print it all and a final horizontal divider


def print_on_third(row_col, output):
    """A helper function for print_sudoku to add
    parts of the output that only occur as delimiters of
    the puzzles boxes. Takes parameter row_col an int
    indicator of either the row or column in the array
    being checked, and output, a string to be returned
    if the row or column is a multiple of 3"""
    step = 3
    message = ""
    if row_col % step == 0:
        message += output
    return message


def print_possible_locations(problem):
    """checks through all elements of the parameter
    problem array and prints out details of
    cells that have not been solved."""
    completed_set_size = 1
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if len(problem[i][j]) > completed_set_size:
                print("The location (" + str(i) + ", " + str(j) +
                      ") might be one of these:", problem[i][j])


def ask_yes_or_no(prompt):
    """Takes a string as an argument to display any question requiring a
    yes or no answer. Returns True if answer begins with y or Y,
    false if n or N. Any other input and the answer is requested again."""
    valid_input = {"y", "n"}
    affirmative_input = {"y"}
    user_response = ""
    while not user_response in valid_input:
        temp_input = input(prompt).lower()
        try:
            user_response = temp_input[0]
        except:
            print("\nPlease enter Y or N")
    print("\n")
    return user_response in affirmative_input


def main():
    """main function that continues through the main loop
    until the user states they no longer want to solve puzzles.
    Takes input for the puzzle file to be loaded, calls the
    other functions necessary to convert the data and attempt solving
    the puzzle, and prints out the puzzle incomplete and complete/
    the possible locations for completion."""
    solving_a_puzzle = True

    while solving_a_puzzle:
        sudoku_file = input("Please enter a sudoku problem file name: ")
        try:
            sudoku_list = read_sudoku(sudoku_file)
            print_sudoku(sudoku_list)
            sudoku_set = convertToSets(sudoku_list)
            solved = solve(sudoku_set)
            sudoku_list = convertToInts(sudoku_set)
            print_sudoku(sudoku_list)

            if not solved:
                print_possible_locations(sudoku_set)

        except IOError:
            print("\nERROR: No file by that name.")
        finally:
            solving_a_puzzle = ask_yes_or_no("\nWould you like to solve another puzzle? ")


if __name__ == '__main__':
    main()
