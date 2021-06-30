# Towers-of-Hanoi
Python program for solving the Towers of Hanoi problem.
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
