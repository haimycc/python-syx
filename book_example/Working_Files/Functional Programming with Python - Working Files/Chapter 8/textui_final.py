from __future__ import print_function
import sys
from effect import Effect, Func
from effect.do import do, do_return
from effect.io import Display, Prompt
from core2 import initial_state, take, move, render
from storage import SaveGame

@do
def mainloop(state):
    while True:
        state = yield step(state)
        yield Effect(SaveGame(state=state))

def display(o):
    return Effect(Display(o))

@do
def step(state):
    yield display(render(state))
    try:
        user_input = yield Effect(Prompt('> '))
        cmd, arg = parse(user_input)
        result = dispatch(state, cmd, arg)
        yield display("Okay.")
        yield do_return(result)
    except (EOFError, KeyboardInterrupt):
        yield display("\nThanks for playing!")
        sys.exit()
    except Exception as e:
        yield display(str(e))
        yield do_return(state)

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

def startup():
    from storage import connect_db, initialize, sqlite_dispatcher
    conn = connect_db()
    state = initialize(conn)
    if state is not None:
        print("Continuing the game...")
    else:
        print("Creating new game.")
        state = initial_state
    st_dispatcher = sqlite_dispatcher(conn)
    return st_dispatcher, state

if __name__ == '__main__':
    from effect import sync_perform
    from effect.io import stdio_dispatcher
    from effect import base_dispatcher, ComposedDispatcher
    st_dispatcher, state = startup()
    dispatcher = ComposedDispatcher([stdio_dispatcher, base_dispatcher, st_dispatcher])
    main_eff = mainloop(state)
    sync_perform(dispatcher, main_eff)
