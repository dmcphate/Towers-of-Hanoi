# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:35:28 2021

@author: Dustin McPhate

    This function solves the Tower of Hanoi problem for 3 towers
    and 'num_discs' discs.  This function creates a list whose 
    elements are the state of the towers after each move.  For example, 
    the following list would be generated for 3 discs (spacing added only
    for readability):
    [ [[2, 1, 0], [],     []         ], 
      [[2, 1],    [],     [0]        ], 
      [[2],       [1],    [0]        ], 
      [[2],       [1, 0], []         ], 
      [[],        [1, 0], [2]        ], 
      [[0],       [1],    [2]        ], 
      [[0],       [],     [2, 1]     ], 
      [[],        [],     [2, 1, 0]] ]
      
    initial_state    - The list of towers containing the discs in their 
                       initial state.
    solution         - The list that shall contain the list of states 
                       moving from the initial_state to the final state
                       upon completion of this function.
    num_towers       - The number of towers in each state.  You may assume
                       this is always 3.
    num_discs        - The number of discs.
    start_tower_idx  - The index of the tower containing all of the discs
                       in the initial state.
    target_tower_idx - The index of the tower that shall contain all of 
                       the discs in the final state.
"""

def init_tower_discs(towers, num_towers, num_discs, start_tower_idx):
    """
    Initializes the variable tower to contain 'num_towers' towers, with
    'num_discs' appropriately ordered on the first tower according to the
    rules of Tower of Hanoi.
    """
    towers.clear()
    for c in range(num_towers):
        towers.append([])
    for d in reversed(range(num_discs)):
        towers[start_tower_idx].append(d)


def HT(x,y,source,aux,target):
    if source == None:
        source = initial_state[0]
    if target == None:
        target = initial_state[x - 1]
    if aux == None:
        for i in range(x):
            if i != start_tower_idx and i != target_tower_idx :
                aux = initial_state[i]    
    if y > 0:
        HT(x,y-1,source, target, aux)        
        disk = source.pop()
        target.append(disk)
        solution.append([initial_state[0][:],initial_state[1][:],initial_state[2][:]])    
        HT(x,y-1,aux, source, target)
    pass

def hanoi(initial_state, solution, num_towers, num_discs, start_tower_idx, target_tower_idx):
        solution.append([initial_state[0][:],initial_state[1][:],initial_state[2][:]])  
        HT(num_towers, num_discs, initial_state[start_tower_idx], None, initial_state[target_tower_idx])
        pass


num_discs = 5
num_towers = 3
start_tower_idx = 0
target_tower_idx = num_towers - 1
initial_state = []

init_tower_discs(initial_state, num_towers, num_discs, start_tower_idx)

solution = []

hanoi(initial_state, solution, num_towers, num_discs, start_tower_idx, target_tower_idx)
print(solution)  