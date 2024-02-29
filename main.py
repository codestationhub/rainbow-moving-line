import json
import time
import termcolor

json_file = open("config.json")
json_data = json.load(json_file)

USE_COLOR = json_data["UseColor"]
SYMBOL_LIST = json_data["Symbols"]
SYMBOL_SWITCH = json_data["SwitchSymbols"]
SYMBOLS_LENGTH = json_data["SymbolsLength"]
LINES_AMOUNT = json_data["LinesAmount"]
DISTANCE = json_data["Distance"]
SPEED = json_data["Speed"]
COLOR_INTERVAL = json_data["ColorInterval"]
FPS = json_data["FPS"]

colors = ["red", "yellow", "green", "blue", "magenta", "cyan", "white"]
spaces = 0
sped = SPEED
color = 0
count = 0
sym = 0
count2 = 0

while True:
    line = SYMBOL_LIST[sym] * SYMBOLS_LENGTH
    count2 += 1
    if SYMBOL_SWITCH[0]:
        if count2 > SYMBOL_SWITCH[1]-1:
            sym += 1
        count2 = 0
    if sym > len(SYMBOL_LIST)-1:
        sym = 0
    current_color = colors[color % len(colors)]
    spacer = " " * spaces
    if USE_COLOR:
        print(termcolor.colored(spacer + line, current_color)*LINES_AMOUNT)
    else:
        print((spacer + line)*LINES_AMOUNT)
    if spaces > DISTANCE:
        sped = -SPEED
    if spaces < 1:
        sped = SPEED
    count += 1
    if count > COLOR_INTERVAL-1:
        count = 0
        color += 1
    if color > 6:
        color = 0
    spaces += sped
    time.sleep(1 / float(FPS))
