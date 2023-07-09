import __init__
from puzzle.rules.ArrowRules import ArrowRules, Arrow
from constraint import Problem

def test_ArrowRules():
    variables = [['A', 'B', 'C']]
    arrows = [Arrow((0, 0), [(0, 1), (0, 2)])] # A = B + C
    rules = ArrowRules(arrows)
    problem = Problem()
    for row in variables:
        for variable in row:
            problem.addVariable(variable, range(0, 2))
    rules.add_constraints(problem, len(variables), len(variables[0]), variables)
    solutions = problem.getSolutions()
    assert solutions == [
        {'A': 1, 'B': 1, 'C': 0},
        {'A': 1, 'B': 0, 'C': 1},
        {'A': 0, 'B': 0, 'C': 0}
    ]
