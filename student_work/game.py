# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon
# To make this work, you may have to type this into the terminal --> pip install curses




import curses
import random
# collectable_x = random.randint(1,9)
# collectable_y = random.randint(8,10)

# collectable_xx = random.randint(1,9)
# collectable_yy = random.randint(5,6)


# random_integer = random.randint(1,9)
# random_integer = int(random_integer)


cieling = 3
game_data = {
    'width': 10,
    'height': 15,
    'player': {"x": 5, "y": 13, "score": 0, "energy": 10, "max_energy": 10},
    'floor': [
        {"x": 1, "y": 14},
        {"x": 2, "y": 14},
        {"x": 3, "y": 14},
        {"x": 4, "y": 14},
        {"x": 5, "y": 14},
        {"x": 6, "y": 14},
        {"x": 7, "y": 14},
        {"x": 8, "y": 14},
        {"x": 9, "y": 14},
        {"x": 10, "y": 14},
    ],
    # 'clouds': [
    #     {"x": 1, "y": 1},
    #     {"x": 2, "y": 1},
    #     {"x": 3, "y": 1},
    #     {"x": 4, "y": 1},
    #     {"x": 5, "y": 1},
    #     {"x": 6, "y": 1},
    #     {"x": 7, "y": 1},
    #     {"x": 8, "y": 1},
    #     {"x": 9, "y": 1},
    #     {"x": 10, "y": 1},
    # ],
    'collectibles': [
        {"x": 4, "y": 10, "collected": False},
        {"x": 5, "y": 6, "collected": False},
        {"x": 5, "y": 13, "collected": False},
    ],
    'obstacles': [

        {"x": 4, "y": 11},
        {"x": 5, "y": 7},
    ],

    # ASCII icons
    'clouds': "\U0001F327",
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
    for x in range(24):
    # .addstr(y, x, string)
        stdscr.addstr(2, x, "\U0001F327")
def randomization_of_platforms():
    # (game_data['collectibles']['x']) = random.randint(1,9)
    # (game_data['collectibles']['y']) = random.randint(1,9)
    for collectible in game_data['collectibles']:
        collectible['x'] = random.randint(1,9)
        collectible['y'] = random.randint(1,9)
    for obstacle in game_data['obstacles']:
        obstacle['x'] = random.randint(1,9)
        obstacle['y'] = random.randint(1,9)
def reset_level():
    if (game_data['player']['y']) <= 3:
        (game_data['player']['y']) = 13
        (game_data['player']['x']) = 5
        randomization_of_platforms()
def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

    if key == "w" and y > 0:
        if (game_data['player']['x']) == 4 and (game_data['player'])['y'] == 10 or (game_data['player']['x']) == 5 and (game_data['player'])['y'] == 6 or (game_data['player']['x']) == 5 and (game_data['player'])['y'] == 13:
            new_y -= 5
        if (game_data['player'])['y'] <= 3:
            reset_level()
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
    if (game_data['player']['x']) == 4 and (game_data['player'])['y'] == 10:
        (game_data['player']['score']) += 1
    if (game_data['player']['x']) == 5 and (game_data['player'])['y'] == 6:
        (game_data['player']['score']) += 1

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
