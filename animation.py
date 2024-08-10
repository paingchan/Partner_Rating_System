import time
import sys
import pyfiglet
from colorama import Fore, Style, init

def color(color_name):
    """Return the corresponding color based on the color name."""
    colors = {
        'cyan': Fore.CYAN,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'red': Fore.RED,
        'blue': Fore.BLUE,
        'white': Fore.WHITE
    }
    return colors.get(color_name.lower(), Fore.WHITE)

#init(autoreset=True)
def welcome_page(text, color_name='cyan'):
    """Display a welcome page with big ASCII text in the specified color."""
    chosen_color = color(color_name)  # Get the color from the color_name
    figlet = pyfiglet.Figlet(font='slant')  # Choose a font, e.g., 'slant'
    big_text = figlet.renderText(text)
    print(chosen_color + big_text + Style.RESET_ALL)


def animated_loading(text="Checking", color=Fore.CYAN):
    print(color + text, end="")
    sys.stdout.flush()  # Ensures that the text is displayed immediately
    for _ in range(3):  # Loop to add 3 dots
        time.sleep(0.5)  # Pause for 0.5 seconds
        print(color + ".", end="")  # Add color to the dots
        sys.stdout.flush()  # Ensures that the dot is displayed immediately
    print(Style.RESET_ALL)  # Reset to default after the animation
