from random import randint

def dead_state(width=0, height=0):

    state = []

    for i in range(height):
        state.append([])
        for j in range(width):
            state[i].append(0)

    return state
        
    

def random_state(width=0, height=0):

    state = [] 

    for i in range(height):
        row = [ randint(0,1) for i in range(width) ]
        state.append(row)

    return state

def render(state):
    divider = ''.join(['-'] * (len(state[0])*2 + 2 ))

    print(divider)

    for row in state:
        line = [ '# ' if cell==1 else '  ' for cell in row ]
        print('|', end='')
        print(''.join(line), end='|\n') 

    print(divider)
