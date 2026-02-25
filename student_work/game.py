# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon
# To make this work, you may have to type this into the terminal --> pip install curses
import curses
import random
collectable_x = random.randint(1,9)
collectable_y = random.randint(7,10)
game_data = {
    'width': 10,
    'height': 15,
    'player': {"x": 5, "y": 13, "score": 0, "energy": 10, "max_energy": 10},
    # 'eagle_pos': {"x": 9, "y": 14},
    'collectibles': [
        {"x": collectable_x, "y": collectable_y, "collected": False},
    ],
    'obstacles': [

        {"x": collectable_x, "y": collectable_y+1},
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

    # ASCII icons
    'turtle': "\U0001F422",
    # 'eagle_icon': "\U0001F985",
    'obstacle': "\U0001F533",
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
            # Eagle
            # elif x == game_data['eagle_pos']['x'] and y == game_data['eagle_pos']['y']:
            #     row += game_data['eagle_icon']
            # Obstacles
            elif any(o['x'] == x and o['y'] == y for o in game_data['obstacles']):
                row += game_data['obstacle']
            # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['leaf']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)
