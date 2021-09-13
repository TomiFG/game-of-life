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
    # counts the number of 'live cells' around a given one
    count = 0    

    if x==0:
        if y==0:
            count = state[y][x+1] + state[y+1][x] + state[y+1][x+1]
            return count
        if y==len(state)-1:
            count = state[y-1][x] + state[y-1][x+1] + state[y][x+1]
            return count

        count += state[y-1][x] + state[y-1][x+1]
        count += state[y][x+1]
        count += state[y+1][x] + state[y+1][x+1]
        return count

    if x==len(state[0])-1:
        if y==0:
            count = state[y][x-1] + state[y+1][x-1] + state[y+1][x]
            return count
        if y==len(state)-1:
            count = state[y-1][x-1] + state[y-1][x] + state[y][x-1]
            return count

        count += state[y-1][x-1] + state[y-1][x]
        count += state[y][x-1]
        count += state[y+1][x-1] + state[y+1][x]
        return count

    if y==0:
        count += state[y][x-1] + state[y][x+1]
        count += state[y+1][x-1] + state[y+1][x] + state[y+1][x+1]
        return count
    
    if y==len(state)-1:
        count += state[y-1][x-1] + state[y-1][x] + state[y-1][x+1]
        count += state[y][x-1] + state[y][x+1]
        return count
    
    count += state[y-1][x-1] + state[y-1][x] + state[y-1][x+1]
    count += state[y][x-1] + state[y][x+1]
    count += state[y+1][x-1] + state[y+1][x] + state[y+1][x+1]
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

def main(width=20, height=20, fps=5):
    state = random_state(width, height) 
    
    sleep_time = 1 / fps

    while True:
        render(state)
        state = next_state(state)
        time.sleep(sleep_time)

if __name__ == '__main__':
    main()
