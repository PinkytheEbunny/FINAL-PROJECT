# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon
# To make this work, you may have to type this into the terminal --> pip install curses
import curses
import random
collectable_x = random.randint(1,9)
collectable_y = random.randint(8,10)

collectable_xx = random.randint(1,9)
collectable_yy = random.randint(5,6)

collectable_xxx = 5
collectable_yyy = 13
cieling = 2
game_data = {
    'width': 10,
    'height': 15,
    'player': {"x": 5, "y": 13, "score": 0, "energy": 10, "max_energy": 10},
    'floor': [
        {"x": 1, "y": 14, 'state': 'solid'},
        {"x": 2, "y": 14, 'state': 'solid'},
        {"x": 3, "y": 14, 'state': 'solid'},
        {"x": 4, "y": 14, 'state': 'solid'},
        {"x": 5, "y": 14, 'state': 'solid'},
        {"x": 6, "y": 14, 'state': 'solid'},
        {"x": 7, "y": 14, 'state': 'solid'},
        {"x": 8, "y": 14, 'state': 'solid'},
        {"x": 9, "y": 14, 'state': 'solid'},
        {"x": 10, "y": 14, 'state': 'solid'}
    ],
    'collectibles': [
        {"x": collectable_x, "y": collectable_y, "collected": False},
        {"x": collectable_xx, "y": collectable_yy, "collected": False},
        {"x": collectable_xxx, "y": collectable_yyy, "collected": False},
    ],
    'obstacles': [

        {"x": collectable_x, "y": collectable_y+1},
        {"x": collectable_xx, "y": collectable_yy+1},
    ],

    # ASCII icons
    'turtle': "\U0001F419",
    'state': "\U0001F533",
    'solid': "\U0001F533",
    'obstacle': "\U0001F533",
    'Lava': "\U0001F7E7",
    'leaf': "\U0001FA99",
    'empty': "  "
}

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['turtle']
            # Obstacles
            elif any(o['x'] == x and o['y'] == y for o in game_data['obstacles']):
                row += game_data['obstacle']
            # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['leaf']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.addstr(game_data['height'] + 1, 0,
                  f"COINS COLLECTED: {game_data['player']['score']}",
                  curses.color_pair(1))
    stdscr.refresh()

def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

    if key == "w" and y > 0:
        if (game_data['player']['x']) == collectable_x and (game_data['player'])['y'] == collectable_y or (game_data['player']['x']) == collectable_xx and (game_data['player'])['y'] == collectable_yy or (game_data['player']['x']) == collectable_xxx and (game_data['player'])['y'] == collectable_yyy:
            new_y -= 6
    elif key == "s" and y < game_data['height'] - 1:
        new_y += 1
    elif key == "a" and x > 0:
        new_x -= 1
        new_y += 1
    elif key == "d" and x < game_data['width'] - 1:
        new_x += 1
        new_y += 1
    else:
        return  # Invalid key or move off board

    # Check for obstacles
    if any(o['x'] == new_x and o['y'] == new_y for o in game_data['obstacles']):
        return

    # Update position and increment score
    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y
    if (game_data['player']['x']) == collectable_x and (game_data['player'])['y'] == collectable_y:
        (game_data['player']['score']) += 1
    if (game_data['player']['x']) == collectable_xx and (game_data['player'])['y'] == collectable_yy:
        (game_data['player']['score']) += 1
    if (game_data['player']['y']) <= cieling:
        (game_data['player']['y']) = 13
        (game_data['obstacles']['x']) = random.randint(1,9)
        (game_data['obstacles']['y']) = random.randint(1,9)



def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break

            move_player(key)
            draw_board(stdscr)

curses.wrapper(main)
