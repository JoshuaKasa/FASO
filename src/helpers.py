import colorama
import logging
import os

from stat import filemode
from colorama import Fore, Style

colorama.init(autoreset=True) # Auto-reset colors after each print statement

class Color:
    HEADER = Fore.LIGHTMAGENTA_EX
    BLUE = Fore.BLUE
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT
    UNDERLINE = Style.BRIGHT

# Initialize logging
def setup_logging(log_file='tree.log', log_level=logging.INFO):
    logging.basicConfig(filename=log_file, level=log_level, filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    console = logging.StreamHandler()
    console.setLevel(log_level)
    formatter = logging.Formatter('%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def print_colored(text, color=Color.RESET, log=True):
    """Prints text with the specified color and optionally logs the message."""
    if log:
        logging.info(text)
    print(f"{color}{text}{Color.RESET}")

def human_readable_size(size, decimal_places=2):
    """Converts file size to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']: 
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

def get_permissions(path):
    """Retrieves the file permissions."""
    st_mode = os.stat(path).st_mode
    return filemode(st_mode)