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
""")

"""
files = ("dict.txt", "pkmn.txt", "beemovie.txt", "chinesechar.txt", "abc.txt")

if int(txt) > 0 and int(txt) <= 5:
	txtfile = files[int(txt) + 1]
else:
	raise You

f = open(txtfile, "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1)
"""
