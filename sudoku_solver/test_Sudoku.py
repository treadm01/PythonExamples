from sudoku import *


def testConvertToSets():
    s = set(range(1, 10))
    ary = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    assert ([[s, {1}, {2}], [{1}, s, {2}], [s, {1}, s]] == convertToSets(ary))
    assert (type(ary[0][0]) is int), "The original array has been changed."

    ary = [[0, 0], [0, 0]]
    assert ([[s, s], [s, s]] == convertToSets(ary))
    assert (type(ary[0][0]) is int), "The original array has been changed."

    ary = [[5, 6], [3, 2]]
    assert ([[{5}, {6}], [{3}, {2}]] == convertToSets(ary))
    assert (type(ary[0][0]) is int), "The original array has been changed."

    ary = [[5], [3, 2]]
    assert ([[{5}], [{3}, {2}]] == convertToSets(ary))
    assert (type(ary[0][0]) is int), "The original array has been changed."

    ary = [[5], [0]]
    assert ([[{5}], [s]] == convertToSets(ary))
    assert (type(ary[0][0]) is int), "The original array has been changed."

    # ragged array row and column check
    ary = [[5], [1, 2, 4], [1, 2]]
    assert ([[{5}], [{1}, {2}, {4}], [{1}, {2}]] == convertToSets(ary))
    assert (type(ary[0][0]) is int), "The original array has been changed."

    ary = [[0]]
    assert ([[s]] == convertToSets(ary))
    assert ([[{1, 2, 3, 4, 5, 6, 7, 8, 9}]] == convertToSets(ary))
    assert (type(ary[0][0]) is int), "The original array has been changed."

    ary = []
    assert ([] == convertToSets(ary))

    ary = [[4, 0, 0, 0, 0, 3, 0, 7, 0, 2, 5, 7],
           [0, 0, 1, 0, 0, 9, 5, 0, 8, 2, 5, 7],
           [0, 0, 0, 6, 0, 8, 4, 1, 3, 2, 5, 7],

           [0, 1, 0, 9, 0, 0, 3, 0, 0, 2, 5, 7],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 2, 5, 7],
           [0, 0, 4, 0, 0, 6, 0, 8, 0, 2, 5, 7],

           [7, 9, 2, 8, 0, 5, 0, 0, 0, 2, 5, 7],
           [3, 0, 5, 4, 0, 0, 9, 0, 0, 2, 5, 7],
           [0, 4, 0, 2, 0, 0, 8, 0, 5, 2, 5, 7],

           [7, 9, 2, 8, 0, 5, 0, 0, 0, 2, 5, 7],
           [3, 0, 5, 4, 0, 0, 9, 0, 0, 2, 5, 7],
           [0, 4, 0, 2, 0, 0, 8, 0, 5, 2, 5, 7]]

    assert (len(ary) == len(convertToSets(ary)))


def testConvertToInts():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
    assert ([[0, 3, 4], [1, 0, 2], [0, 2, 3]] == convertToInts(sets))
    assert (type(sets[0][0]) is set), "The original array has been changed."

    sets = [[{1, 2, 3, 4, 5, 6, 7, 8, 9}, {3}, {4}], [{1}, {3}, {2}], [{2}, {2}, {3}]]
    assert ([[0, 3, 4], [1, 3, 2], [2, 2, 3]] == convertToInts(sets))
    assert (type(sets[0][0]) is set), "The original array has been changed."

    sets = [[{1}, {3}], [{2}, {3}]]
    assert ([[1, 3], [2, 3]] == convertToInts(sets))
    assert (type(sets[0][0]) is set), "The original array has been changed."

    sets = [[{1}, {}], [{2, 3, 4}, {3}]]
    assert ([[1, 0], [0, 3]] == convertToInts(sets))
    assert (type(sets[0][0]) is set), "The original array has been changed."

    sets = [[{}]]
    assert ([[0]] == convertToInts(sets))

    sets = [[{1}]]
    assert ([[1]] == convertToInts(sets))


def testGetRowLocations():
    lst = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    assert (set(lst) == set(getRowLocations(5)))

    lst = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]
    assert (set(lst) == set(getRowLocations(0)))

    lst = [(54, 0), (54, 1), (54, 2), (54, 3), (54, 4), (54, 5), (54, 6), (54, 7), (54, 8)]
    assert (set(lst) == set(getRowLocations(54)))

    lst = [(-5, 0), (-5, 1), (-5, 2), (-5, 3), (-5, 4), (-5, 5), (-5, 6), (-5, 7), (-5, 8)]
    assert (set(lst) == set(getRowLocations(-5)))

    lst = [(0.5, 0), (0.5, 1), (0.5, 2), (0.5, 3), (0.5, 4), (0.5, 5), (0.5, 6), (0.5, 7), (0.5, 8)]
    assert (set(lst) == set(getRowLocations(0.5)))

    expected = (8, 8)
    result = getRowLocations(8)
    assert (expected == result[8])


def testGetGenericLocations():
    lst = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    assert (set(lst) == set(get_generic_locations(5, 9)))

    lst = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]
    assert (set(lst) == set(get_generic_locations(0, 9)))

    lst = [(54, 0), (54, 1), (54, 2), (54, 3), (54, 4), (54, 5), (54, 6), (54, 7), (54, 8)]
    assert (set(lst) == set(get_generic_locations(54, 9)))

    lst = [(-5, 0), (-5, 1), (-5, 2), (-5, 3), (-5, 4), (-5, 5), (-5, 6), (-5, 7), (-5, 8)]
    assert (set(lst) == set(get_generic_locations(-5, 9)))

    lst = [(0.5, 0), (0.5, 1), (0.5, 2), (0.5, 3), (0.5, 4), (0.5, 5), (0.5, 6), (0.5, 7), (0.5, 8)]
    assert (set(lst) == set(get_generic_locations(0.5, 9)))

    expected = (8, 8)
    result = get_generic_locations(8, 9)
    assert (expected == result[8])


def testGetColumnLocations():
    lst = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    assert (set(lst) == set(getColumnLocations(5)))

    lst = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
    assert (set(lst) == set(getColumnLocations(0)))

    lst = [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]
    assert (set(lst) == set(getColumnLocations(8)))

    expected = (1, 0)
    result = getColumnLocations(0)
    assert (expected == result[1])


def testGetBoxLocations():
    lst = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    assert (set(lst) == set(getBoxLocations((3, 2))))

    lst = [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    assert (set(lst) == set(getBoxLocations((8, 8))))

    lst = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    assert (set(lst) == set(getBoxLocations((0, 0))))

    expected = 0
    result = getBoxLocations((2, 0))
    assert (expected == result[0][0])


def testEliminate():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    location = (1, 2)  # contains {2}
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2)])
    assert (2 == count)
    assert ([[{1}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 3}]] ==
            sets)

    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    location = (1, 2)  # contains {2}
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2), (2, 0)])
    assert (3 == count)
    assert ([[{1}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{3}, {2}, {1, 3}]] ==
            sets)

    sets = [[{1, 2, 3, 7}, {3, 4, 7}], [{3, 5, 7}, {7}]]
    location = (1, 1)  # contains {7}
    count = eliminate(sets, location, [(0, 0), (0, 1), (1, 0)])
    assert (3 == count)
    assert ([[{1, 2, 3}, {3, 4}], [{3, 5}, {7}]] ==
            sets)

    sets = [[{1, 2, 3, 7}, {3, 4, 7}, {1, 2, 3, 5}], [{3, 5, 7}, {7}, {8}]]
    location = (1, 2)  # contains {8}
    count = eliminate(sets, location, [(0, 0)])
    assert (0 == count)
    assert ([[{1, 2, 3, 7}, {3, 4, 7}, {1, 2, 3, 5}], [{3, 5, 7}, {7}, {8}]] ==
            sets)

    sets = [[{4, 5, 6, 8}, {8}, {2, 3, 8}], [{3, 5, 8}, {1, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8}]]
    location = (0, 1)  # contains {8}
    count = eliminate(sets, location, [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)])
    assert (5 == count)
    assert ([[{4, 5, 6}, {8}, {2, 3}], [{3, 5}, {1, 7}, {1, 2, 3, 4, 5, 6, 7}]] ==
            sets)

    sets = [[{4, 5, }], [{4}]]
    location = (1, 0)  # contains {4}
    count = eliminate(sets, location, [(0, 0)])
    assert (1 == count)
    assert ([[{5}], [{4}]] == sets)


def testIsSolved():
    array = [[{1}] * 9] * 9
    assert (all([len(array[r][c]) == 1 for r in range(0, 9)
                 for c in range(0, 9)]))
    expected = True
    actual = isSolved(array)
    assert expected == actual

    array[3][5] = {1, 2}
    assert not (all([len(array[r][c]) == 1 for r in range(0, 9)
                     for c in range(0, 9)]))

    array = [[{1}] * 9] * 9
    array[3][5] = {1, 1, 1}
    assert (all([len(array[r][c]) == 1 for r in range(0, 9)
                 for c in range(0, 9)]))

    array = [[{1}] * 36] * 36
    assert (all([len(array[r][c]) == 1 for r in range(0, 36)
                 for c in range(0, 36)]))

    array[35][35] = {1, 2, 3}
    assert not (all([len(array[r][c]) == 1 for r in range(0, 36)
                     for c in range(0, 36)]))

    array = [[{1}] * 9] * 9
    array[0][8] = {1, 1, 2}
    assert not (all([len(array[r][c]) == 1 for r in range(0, 9)
                     for c in range(0, 9)]))
    expected = False
    actual = isSolved(array)
    assert expected == actual


def testSolve():
    # Easy
    sudoku1 = [[4, 0, 0, 0, 0, 3, 0, 7, 0],
               [0, 0, 1, 0, 0, 9, 5, 0, 8],
               [0, 0, 0, 6, 0, 8, 4, 1, 3],

               [0, 1, 0, 9, 0, 0, 3, 0, 0],
               [0, 0, 0, 0, 5, 0, 0, 0, 0],
               [0, 0, 4, 0, 0, 6, 0, 8, 0],

               [7, 9, 2, 8, 0, 5, 0, 0, 0],
               [3, 0, 5, 4, 0, 0, 9, 0, 0],
               [0, 4, 0, 2, 0, 0, 8, 0, 5]]

    solved1 = [[4, 6, 8, 5, 1, 3, 2, 7, 9],
               [2, 3, 1, 7, 4, 9, 5, 6, 8],
               [5, 7, 9, 6, 2, 8, 4, 1, 3],

               [6, 1, 7, 9, 8, 2, 3, 5, 4],
               [8, 2, 3, 1, 5, 4, 7, 9, 6],
               [9, 5, 4, 3, 7, 6, 1, 8, 2],

               [7, 9, 2, 8, 3, 5, 6, 4, 1],
               [3, 8, 5, 4, 6, 1, 9, 2, 7],
               [1, 4, 6, 2, 9, 7, 8, 3, 5]]
    # Easy
    sudoku2 = [[0, 0, 0, 7, 0, 0, 6, 8, 9],
               [3, 0, 8, 0, 0, 0, 2, 0, 0],
               [0, 0, 0, 8, 1, 0, 0, 4, 0],

               [6, 0, 0, 0, 0, 0, 8, 0, 4],
               [8, 0, 0, 3, 4, 9, 0, 0, 5],
               [7, 0, 5, 0, 0, 0, 0, 0, 3],

               [0, 8, 0, 0, 7, 6, 0, 0, 0],
               [0, 0, 7, 0, 0, 0, 1, 0, 8],
               [9, 5, 1, 0, 0, 8, 0, 0, 0]]

    solved2 = [[1, 2, 4, 7, 5, 3, 6, 8, 9],
               [3, 7, 8, 9, 6, 4, 2, 5, 1],
               [5, 9, 6, 8, 1, 2, 3, 4, 7],

               [6, 3, 9, 5, 2, 7, 8, 1, 4],
               [8, 1, 2, 3, 4, 9, 7, 6, 5],
               [7, 4, 5, 6, 8, 1, 9, 2, 3],

               [4, 8, 3, 1, 7, 6, 5, 9, 2],
               [2, 6, 7, 4, 9, 5, 1, 3, 8],
               [9, 5, 1, 2, 3, 8, 4, 7, 6]]

    # Hard
    sudoku3 = [[9, 0, 0, 0, 0, 8, 0, 0, 0],
               [0, 0, 0, 0, 3, 2, 0, 0, 0],
               [6, 8, 0, 9, 0, 1, 0, 7, 0],

               [8, 0, 9, 5, 2, 0, 0, 3, 0],
               [2, 0, 0, 0, 0, 0, 0, 0, 5],
               [0, 4, 0, 0, 9, 3, 7, 0, 8],

               [0, 2, 0, 3, 0, 9, 0, 6, 4],
               [0, 0, 0, 2, 8, 0, 0, 0, 0],
               [0, 0, 0, 6, 0, 0, 0, 0, 3]]

    solved3 = [[9, 0, 0, 0, 0, 8, 0, 0, 0],
               [0, 0, 0, 0, 3, 2, 0, 0, 0],
               [6, 8, 0, 9, 0, 1, 0, 7, 2],

               [8, 0, 9, 5, 2, 0, 0, 3, 0],
               [2, 0, 0, 0, 0, 0, 0, 0, 5],
               [5, 4, 6, 1, 9, 3, 7, 2, 8],

               [0, 2, 0, 3, 0, 9, 0, 6, 4],
               [0, 0, 0, 2, 8, 0, 0, 0, 0],
               [0, 0, 0, 6, 0, 0, 0, 0, 3]]

    # easy - mulitple 2s in same row - unsolvable puzzle
    sudoku4 = [[0, 6, 8, 5, 1, 3, 2, 7, 9],
               [2, 0, 1, 7, 4, 9, 5, 6, 8],
               [5, 7, 0, 6, 2, 8, 4, 1, 3],

               [6, 1, 7, 0, 8, 2, 3, 5, 4],
               [8, 2, 3, 1, 0, 4, 7, 9, 6],
               [9, 5, 4, 3, 7, 0, 1, 8, 2],

               [2, 2, 2, 8, 3, 5, 0, 4, 1],
               [0, 0, 0, 4, 6, 1, 9, 0, 7],
               [0, 0, 0, 2, 9, 7, 8, 3, 0]]

    solved4 = [[4, 6, 8, 5, 1, 3, 2, 7, 9],
               [2, 3, 1, 7, 4, 9, 5, 6, 8],
               [5, 7, 9, 6, 2, 8, 4, 1, 3],

               [6, 1, 7, 9, 8, 2, 3, 5, 4],
               [8, 2, 3, 1, 5, 4, 7, 9, 6],
               [9, 5, 4, 3, 7, 6, 1, 8, 2],

               [7, 9, 2, 8, 3, 5, 6, 4, 1],
               [3, 8, 5, 4, 6, 1, 9, 2, 7],
               [1, 4, 6, 2, 9, 7, 8, 3, 5]]
    # Easy - two 4s in fist row
    sudoku5 = [[4, 0, 0, 0, 0, 3, 0, 7, 4],
               [0, 0, 1, 0, 0, 9, 5, 0, 8],
               [0, 0, 0, 6, 0, 8, 4, 1, 3],

               [0, 1, 0, 9, 0, 0, 3, 0, 0],
               [0, 0, 0, 0, 5, 0, 0, 0, 0],
               [0, 0, 4, 0, 0, 6, 0, 8, 0],

               [7, 9, 2, 8, 0, 5, 0, 0, 0],
               [3, 0, 5, 4, 0, 0, 9, 0, 0],
               [0, 4, 0, 2, 0, 0, 8, 0, 5]]

    solved5 = [[4, 6, 8, 5, 1, 3, 2, 7, 9],
               [2, 3, 1, 7, 4, 9, 5, 6, 8],
               [5, 7, 9, 6, 2, 8, 4, 1, 3],

               [6, 1, 7, 9, 8, 2, 3, 5, 4],
               [8, 2, 3, 1, 5, 4, 7, 9, 6],
               [9, 5, 4, 3, 7, 6, 1, 8, 2],

               [7, 9, 2, 8, 3, 5, 6, 4, 1],
               [3, 8, 5, 4, 6, 1, 9, 2, 7],
               [1, 4, 6, 2, 9, 7, 8, 3, 5]]

    tryToSolve(sudoku1, solved1)
    tryToSolve(sudoku2, solved2)
    tryToSolve(sudoku3, solved3)
    tryToSolveFail(sudoku4, solved4)
    tryToSolveFail(sudoku5, solved5)


def tryToSolve(problem, solution):
    ##        print_sudoku(problem)
    problemAsSets = convertToSets(problem)
    solve(problemAsSets)
    solved = convertToInts(problemAsSets)
    ##        print_sudoku(solution)
    maxDiff = None
    assert (solution == solved)


def tryToSolveFail(problem, solution):
    problemAsSets = convertToSets(problem)
    solve(problemAsSets)
    solved = convertToInts(problemAsSets)
    maxDiff = None
    assert (solution != solved)


def test_string_convert():
    expected = ". "
    assert (expected == string_convert(0, 0))

    expected = "1 "
    assert (expected == string_convert(1, 0))

    expected = "123456789 "
    assert (expected == string_convert(123456789, 0))

    expected = "-67 "
    assert (expected == string_convert(-67, 0))

    expected = ". "
    assert (expected == string_convert(6, 6))

    expected = "0 "
    assert (expected == string_convert(0, 6))


def test_set_convert():
    expected = {3}
    assert (expected == set_convert(3, 0))

    expected = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    assert (expected == set_convert(0, 0))

    expected = {1234}
    assert (expected == set_convert(1234, 0))

    expected = {1.0}
    assert (expected == set_convert(1.0, 0))


def test_int_convert():
    expected = 1
    assert (expected == int_convert({1}, 0))

    expected = 0
    assert (expected == int_convert({1, 2, 4}, 0))

    expected = 0
    assert (expected == int_convert({1, -1}, 0))

    expected = 0
    assert (expected == int_convert({}, 0))

    expected = 12345
    assert (expected == int_convert({12345}, 0))

    expected = 0
    assert (expected == int_convert({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, 0))


def test_generic_convert():
    s = set(range(1, 10))
    ary = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    assert ([[s, {1}, {2}], [{1}, s, {2}], [s, {1}, s]] == generic_convert(ary, set_convert))

    ary = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert ([[s, s, s], [s, s, s], [s, s, s]] == generic_convert(ary, set_convert))

    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
    assert ([[0, 3, 4], [1, 0, 2], [0, 2, 3]] == generic_convert(sets, int_convert))

    sets = [[{}]]
    assert ([[0]] == generic_convert(sets, int_convert))

    ary = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    assert ([[". ", "1 ", "2 "], ["1 ", ". ", "2 "], [". ", "1 ", ". "]] == generic_convert(ary, string_convert))


def test_print_on_third():
    expected = ""
    assert (expected == print_on_third(2, "test"))

    expected = "test"
    assert (expected == print_on_third(3, "test"))

    expected = "test"
    assert (expected == print_on_third(384, "test"))

    expected = ""
    assert (expected == print_on_third(-3.4, "test"))

    expected = ""
    assert (expected == print_on_third(0.4, "test"))
