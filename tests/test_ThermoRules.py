import __init__
from puzzle.rules.ThermoRules import ThermoRules
from constraint import Problem

def test_ThermoRules():
    variables = [['A', 'B', 'C']]
    thermos = [[(0, 0), (0, 1), (0, 2)]] # A < B < C
    rules = ThermoRules(thermos)
    problem = Problem()
    for row in variables:
        for variable in row:
            problem.addVariable(variable, range(0, 3))
    rules.add_constraints(problem, len(variables), len(variables[0]), variables)
    solutions = problem.getSolutions()
    assert solutions == [{'A': 0, 'B': 1, 'C': 2}]
