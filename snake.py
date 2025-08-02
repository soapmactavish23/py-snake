import curses
from asyncio import timeout


def game_loop(window):
    # Setup inicial
    curses.curs_set(0)
    personagem = [10, 15]

    while True:
        draw_screen(window)
        draw_actor(actor=personagem, window=window)
        direction = get_new_direction(window=window, timeout=1000)
        if direction is not None:
            move_actor(actor=personagem, direction=direction)
        if actor_hit_border(actor=personagem, window=window):
            return


def draw_screen(window):
    window.clear()
    window.border(0)


def draw_actor(actor, window):
    window.addch(actor[0], actor[1], curses.ACS_DIAMOND)


def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        return direction
    return None


def move_actor(actor, direction):
    match direction:
        case curses.KEY_UP:
            actor[0] -= 1
        case curses.KEY_LEFT:
            actor[1] -= 1
        case curses.KEY_DOWN:
            actor[0] += 1
        case curses.KEY_RIGHT:
            actor[1] += 1
        case _:
            pass


def actor_hit_border(actor, window):
    height, width = window.getmaxyx()
    if (actor[0] <= 0) or (actor[0] >= height - 1):
        return True
    if (actor[1] <= 0) or (actor[1] >= width - 1):
        return True
    window.addch(actor[0], actor[1], curses.ACS_DIAMOND)
    return False


if __name__ == '__main__':
    curses.wrapper(game_loop)
    print('Perdeu!')
