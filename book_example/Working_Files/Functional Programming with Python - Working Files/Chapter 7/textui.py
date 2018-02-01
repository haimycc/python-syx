from __future__ import print_function
import sys
from core2 import initial_state, take, move, render

def mainloop(state):
    while True:
        state = step(state)

def step(state):
    print(render(state))
    try:
        cmd, arg = parse(raw_input("> "))
        result = dispatch(state, cmd, arg)
        print("Okay.")
        return result
    except (EOFError, KeyboardInterrupt):
        print("\nThanks for playing!")
        sys.exit()
    except Exception as e:
        print(e)
        return state

def parse(line):
    parts = line.split(' ', 1)
    if len(parts) != 2 or parts[0] not in ('take', 'move'):
        raise Exception("Expected: `take <item>` or `move <direction>`")
    return parts

def dispatch(state, cmd, arg):
    handler = {'take': take, 'move': move}[cmd]
    result = handler(state, arg)
    if result is None:
        raise Exception("Invalid argument!")
    else:
        return result

if __name__ == '__main__':
    mainloop(initial_state)
