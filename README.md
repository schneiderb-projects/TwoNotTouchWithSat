# TwoNotTouchWithSat
Touch Two Not is a puzzle where you have an NxN grid and various zones of adjacent cells are walled off as well. The intent of the game is to fill in stars in grid such that,

- No two stars can be adjacent to each other in any directions including diagonally
- Every row contains exactly 2 stars
- Every column contains exactly 2 stars
- Every zone contains only 2 stars


Importance of this Solution Approach:
  The goal is to figure out a solution, if any, for a given puzzle grid.

  The idea of a solution is to represent this game as SAT solver problem and use standard SAT solvers to solve it. The advantage of taking this approach is that our problem can be reduced into a satisfiability problem (SAT). Instead of building a solution finder for our problem ourselves, we are able to make use of standard SAT solvers to identify a solution for our problem, if any. There are standard SAT solvers available to find if a given problem contains any solution that satisfies the rules and representations of that problem. SAT solvers can also tell you if there are no solutions to that SAT problem. 

The rules of the game and given zones for a particular board will be represented in propositional logic in a conjunctive normal form (CNF). Then this CNF will be fed to the SAT solver, which should present us with a solution, or tell us if there are no solutions.
