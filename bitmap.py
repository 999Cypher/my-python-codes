import sys
import time

bitmap = """
  __  __
 |  \\/  | ___  _ __  _   _ 
 | |\\/| |/ _ \\| '_ \\| | | |
 | |  | | (_) | | | | |_| |
 |_|  |_|\\___/|_| |_|\\__,_|
"""

print('Bitmap by your G Johntee')
print('Enter the message to display with the bitmap:')
message = input('> ')
if message == '':
    sys.exit()

# Colors for the message
colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']

# loop over each line in the bitmap:
for line in bitmap.splitlines():
    # loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # print an empty space since there is an space in the bitmap:
            print(' ', end='')
        else:
            # print a character from the message with random color:
            color = colors[i % len(colors)]
            print(color + message[i % len(message)], end='')
            # Add a little delay for an animated effect
            time.sleep(0.02)
    print()  # prints a new line
