from os import system
import numpy as np


"""
just a helper function to arrange lists of the literal in alternating patterns of positive and negated

i.e. [-1, 1, -1, 1, -1, 1] or [-2, -2, 2, 2, -2, -2, 2, 2] or [-4, -4, -4, -4, 4, 4, 4, 4]

returns a list of the given literal as described above
"""
def arrange_literal(literal, position, max_position):
    multiplier = -1  # start with a negated literal
    counter = 0  # counts the number of literals added to the list
    to_return = []  # stores the
    while counter < 2 ** max_position:
        for y in range(2 ** position):
            to_return.append(literal * multiplier)
            counter += 1
        multiplier *= -1

    return to_return


"""
builds the inputs to a truth table to be used when solving this solution

returns a list containing all possible combinations of positive and negated literals using the given list of literals
"""
def build_truth_table_inputs(literals):
    to_return = []
    temp = []

    # creates the truth table
    for position, literal in enumerate(literals):
        temp.append(arrange_literal(literal, position, len(literals)))

    # apply transform to the list
    for x in range(len(temp[0])):
        to_add = []
        for y in reversed(temp):
            to_add.append(y[x])
        to_return.append(to_add)
    return to_return  # returns truth table where each sub-list contains on of every literal either positive or negated


"""
converts the problem into a sum of max terms representing following the rule that 2 stars must be in the same row or 
column and 2 stars in the same row or column must not be adjacent

!F = ∑(max terms)
"""
def get_row_column_max_terms(truth_table):
    max_terms = []

    for clause in truth_table:  # iterate over each clause in the truth table
        positives = 0  # counts the number of true literals
        adjacent = False  # boolean representing if 2 true literals are adjacent
        last = False  # boolean representing if the last literal was True

        for literal in clause:  # iterate over each literal in the clause
            if last and literal > 0:  # if this literal and the last literal are true
                adjacent = True  # then the clause contains adjacent literals
            if literal > 0:  # if the literal is true
                positives += 1  # increment true literal count by 1

            last = literal > 0  # set the last literal depending if current literal is true or false

        if positives != 2 or adjacent:  # if there are more than 2 literals or there are 2 adjacent literals
            max_terms.append(clause)  # append the clause to the max terms

    return max_terms  # return all the clauses


"""
converts the problem into a sum of max terms representing following the rule that 2 stars must be in the same sector

!F = ∑(max terms)
"""
def get_sector_max_terms(truth_table):
    max_terms = []

    for clause in truth_table:  # iterate each clause in the truth table
        positives = 0  # counts the number of true literals
        for literal in clause:  # iterate each literal in the clause
            if literal > 0:  # if a literal is true
                positives += 1  # add 1 to the number to true literals
        if positives != 2:  # if there are not 2 stars in the sector
            max_terms.append(clause)  # append this clause as a max term

    return max_terms  # return all the max terms

"""
use demorgans law to convert the max terms from a sum of products to a product of sums representing
the given sum of products

returns a product of sums representing the sum of products given
"""
def demorgans(max_terms):
    to_return = []

    for clause in max_terms:  # iterate over each clause
        to_add = []
        for literal in clause:  # iterate over each literal
            to_add.append(literal * -1)  # apply demorgan's law by inverting each literal

        to_return.append(to_add)

    return to_return  # return the new product of sums created using demorgan's laws

"""
This just converts the equation out as a string using + for or, * for and, and ! for not
"""
def product_of_sums_to_string(clauses, old_literals, new_literals=None):
    if new_literals is None:
        new_literals = old_literals
    equation = ""
    for ind, x in enumerate(clauses):
        equation += "( "
        for index, y in enumerate(x):
            if y < 0:
                equation += "!"
            equation += new_literals[old_literals.index(abs(y))] + " "
            if index != len(x) - 1:
                equation += "+ "
        equation += ") "
        if ind != len(clauses) - 1:
            equation += "* "

    return equation

"""
given the board layout and the sectors on the board, this produces a sum of products AKA conjunctive normal form 
equation representing the solution to the puzzle

see SamplePuzzles.py for data structure information on puzzles

literal representations:
-Using the format set by minisat, literals are represented as integers (+/- 1, +/- 2, +/- 3, ..., etc.)
-True literals are represented as positive and False literals are represented as negative

technique for finding equation:

!F = ∑(max terms)                   // solve the max terms of the problem to find all unsatisfying solutions
!(!F = ∑(max terms))                // invert the equation to find satisfying solutions instead
!!F = !∑(max terms)                 // distribute the inversion
F = ∏(demorgan'd max terms)         //apply demorgans law to convert sum of products to product of sums AKA conjunctive 
                                    //normal form
                                    
returns a list of clause in conjunctive normal form
"""
def build_2_not_touch_clauses(board, sectors):
    truth_table = []

    for combos in board:  # build a truth table representing all combinations of each row
        truth_table += build_truth_table_inputs(combos)

    for combos in np.array(board).T.tolist():  # build a truth table representing all combinations of each columns
        truth_table += build_truth_table_inputs(combos)

    # solve the truth tables for the set of max terms according to the row/column rules of Two Not Touch
    row_column_max_terms = get_row_column_max_terms(truth_table)

    truth_table = []

    for sector in sectors:  # build a truth table representing all combinations of each row
        truth_table += build_truth_table_inputs(sector)

    # solve the truth tables for the set of max terms according to the sector rules of Two Not Touch
    sectors_max_terms = get_sector_max_terms(truth_table)

    pos_clauses = demorgans(row_column_max_terms + sectors_max_terms)  # invert clauses and apply demorgan's

    return pos_clauses  # return clauses representing solution in conjunctive normal form


"""
Solves a two touch puzzle by encoding it in sat then using the sat solver 'minisat' to find a solution

:returns a list of places locations that a star should be placed in order to solve the puzzle
"""
def solve(puzzle):
    # construct the clauses representing the puzzle as a boolean product of sums AKA conjunctive normal form
    product_of_sums = build_2_not_touch_clauses(puzzle["board"], puzzle["sectors"])

    # write the clauses to the clauses.cnf file in the format used by the minisat solver
    with open("clauses.cnf", "w+") as f:
        f.write("p cnf {} {}\n".format(str(len(puzzle["board"][0]) * len(puzzle["board"])), str(len(product_of_sums))))
        for clause in product_of_sums:
            f.write(" ".join(map(str, clause)))
            f.write(" 0\n")

    # run minisat with the clauses.cnf file as the input parameters and output a solution to out.sat if satisfiable
    system("minisat clauses.cnf out.sat")

    # read the solution in from out.sat
    with open("out.sat", "r") as f:
        lines = f.read()

    # parse solution into a list of numbers representing the squares which a star should be placed in
    lines = lines.split("\n")
    lines = lines[1].split(" ")
    stars = []
    for x in lines:
        num = int(x)
        if num > 0:
            stars.append(num)

    # return the parsed solution
    return stars
