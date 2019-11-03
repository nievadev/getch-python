import termios, sys, tty

def getch():
    file_descriptor = sys.stdin.fileno()

    terminal_settings = termios.tcgetattr(file_descriptor)

    tty.setraw(file_descriptor) # Setting raw mode

    character = sys.stdin.read(6)

    termios.tcsetattr(file_descriptor, termios.TCSADRAIN, actual_settings) # Reset terminal to normal state

    return character

ch = getch()
print(ch)
