import termios, sys, tty

def getch(chars):
    file_descriptor = sys.stdin.fileno()

    terminal_settings = termios.tcgetattr(file_descriptor)

    tty.setraw(file_descriptor) # Setting raw mode

    character = sys.stdin.read(chars)

    termios.tcsetattr(file_descriptor, termios.TCSADRAIN, terminal_settings) # Reset terminal to normal state

    return character

ch = getch(10)
print(ch)
