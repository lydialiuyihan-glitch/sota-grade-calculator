import time
import shutil

# ─────────────────────────────────────────────
# HOUSEWIFE — Tate McRae
# aesthetic terminal lyrics
# ─────────────────────────────────────────────

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

PINK = "\033[38;2;255;153;204m"
PURPLE = "\033[38;2;200;160;255m"
BLUE = "\033[38;2;160;210;255m"
WHITE = "\033[38;2;245;245;245m"

lyrics = [
    "Go into my garden, pick the money off the tree",
    "I don't pay for nothing, baby, people pay me",
    "And you right beside me's just the icing on the dream",
    "I don't need you, I want you, and that's my favorite thing",
    "",
    "Go into my garden, pick the money off the tree",
    "I don't date nobody, baby, people date me",
    "And you right beside me's just the icing on the dream",
    "I don't need you, I want you, and that's my favorite thing",
    "",
    "[ CHORUS ]",
    "",
    "I just wanna make a lot of money, be my own housewife",
    "You, you, you, y-you could be the one I'm calling honey",
    "Be my sex on the side",
    "You, you, you, you",
    "Acres of open stars, headlights of precious cars, life imitating art",
    "I, I, I, I, I just wanna make a lot of money, be my own housewife",
    "Be my, be my"
]


def centre(text):
    width = shutil.get_terminal_size().columns
    return text.center(width)


def type_line(text, colour=WHITE, speed=0.025):
    spaces = max(
        0,
        (shutil.get_terminal_size().columns - len(text)) // 2
    )

    print(" " * spaces + colour, end="", flush=True)

    for character in text:
        print(character, end="", flush=True)
        time.sleep(speed)

    print(RESET)


# Title
print("\n" * 2)
print(PINK + BOLD + centre("♡  H O U S E W I F E  ♡") + RESET)
print(PURPLE + DIM + centre("TATE McRAE") + RESET)
print(PURPLE + centre("─" * 45) + RESET)

time.sleep(1)

# Lyrics
colours = [PINK, PURPLE, BLUE]

colour_index = 0

for line in lyrics:

    if line == "":
        print()
        time.sleep(0.4)

    elif line == "[ CHORUS ]":
        print()
        print(PINK + BOLD + centre("✦  C H O R U S  ✦") + RESET)
        print()
        time.sleep(0.8)

    else:
        type_line(
            line,
            colours[colour_index % len(colours)]
        )

        colour_index += 1
        time.sleep(0.35)

# Ending
print()
print(PURPLE + centre("─" * 45) + RESET)
print(PINK + centre("♡ be my own housewife ♡") + RESET)
print()
