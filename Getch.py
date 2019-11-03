import termios, sys, tty

def getch(chars = 1):
    file_descriptor = sys.stdin.fileno()

    terminal_settings = termios.tcgetattr(file_descriptor)

    tty.setraw(file_descriptor) # Setting raw mode

    character = sys.stdin.read(chars)

    termios.tcsetattr(file_descriptor, termios.TCSADRAIN, terminal_settings) # Reset terminal to normal state

    return character
