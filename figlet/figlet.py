import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
f = figlet.getFonts()

if len(sys.argv) == 1:
    text = input('input: ')
    randfont = random.choice(f)
    figlet.setFont(font=randfont)
    print(figlet.renderText(text))

elif len(sys.argv) == 3 and sys.argv[2] in f and sys.argv[1] in ['-f', '--font']:
    text = input('input: ')
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")

