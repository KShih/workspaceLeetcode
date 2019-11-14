"""
Given a grid with w as width, h as height.
Each cell of the grid represents a potential building lot and we will be adding "n" buildings inside this grid.
The goal is for the furthest of all lots to be as near as possible to a building.
Given an input n, which is the number of buildings to be placed in the lot,
determine the building placement to minimize the distance of the most distant empty lot is from the building.

https://stackoverflow.com/questions/52562585/maximal-value-among-shortest-distances-in-a-matrix
https://ideone.com/ix1nh8

"""

def find_loc(w, h, n):
