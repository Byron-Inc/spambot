import pyautogui, time
time.sleep(5)

txt = input("""
Which would you like to spam:
------------------------------------------
| 1 | English words (423378 lines)       |
| 2 | Pokemons (898 lines)               |
| 3 | Bee Movie Script (1363 lines)      |
| 4 | Chinese characters (9900 lines)    |
| 5 | Alphabet (26 lines)                |
------------------------------------------
> """)

method = input("""
Which way would you like to send messages?
------------------------------------------
| 1 | Tab + Shift (Forum)                |
| 2 | Enter (Social media)               |
------------------------------------------
> """)

cooldown = int(input("How long is the cooldown between post?\n> "))

def send(txt)
    pyautogui.typewrite(txt)
    if method == 1:
        pyautogui.press("tab", "shiftright")
    elif method == 2:
        pyautogui.press("enter")

files = ("dict.txt", "pkmn.txt", "beemovie.txt", "chinesechar.txt", "abc.txt")

if int(txt) > 0 and int(txt) <= 5:
	txtfile = files[int(txt) - 1]
else:
	print("File doesn't exist.")


f = open(txtfile, "r")
for word in f:
    send(word)
    time.sleep(cooldown)
