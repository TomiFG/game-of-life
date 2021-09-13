from random import randint
import time

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
    

def count_neighbors(state, x, y):
    count = 0

    for i in range(y-1, y+2):
        # ignore cells outside the board
        if i<0 or i>=len(state): continue

        for j in range(x-1, x+2):
            # ignore cells outside the board
            if j<0 or j>=len(state[0]): continue
            # ignore the cell of which we're counting it's neighbors
            if i==y and j==x: continue
            
            count += state[i][j]
    
    return count  
            
    
def next_state(init_state):

    new_state = dead_state(len(init_state[0]), len(init_state))

    for y in range(len(init_state)): 
        for x in range(len(init_state[0])):

            count = count_neighbors(init_state, x, y)

            if init_state[y][x] == 1:
                if count==2 or count==3:
                    new_state[y][x] = 1
                continue
            
            if count==3:
                new_state[y][x] = 1

    return new_state

def main(width=50, height=50, fps=5):
    state = random_state(width, height) 
    
    sleep_time = 1 / fps

    while True:
        render(state)
        state = next_state(state)
        time.sleep(sleep_time)

if __name__ == '__main__':
    main()
