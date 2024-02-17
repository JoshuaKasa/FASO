import argparse
import os
import logging

from helpers import print_colored, Color, setup_logging, human_readable_size, get_permissions

def tree(directory, prefix='', depth_limit=None, depth=0, extension_filter=None, color=False, permissions=False, human_readable=False):
    """Generates the directory tree."""
    if depth_limit is not None and depth > depth_limit: # Check if the depth limit has been reached
        return # If the depth limit has been reached, we can end the recursion

    # Attempt to list the directory entries
    try:
        entries = os.listdir(directory) # Using the os.listdir function to list the directory entries
    except PermissionError: # Handle the PermissionError exception
        # Print a message indicating that the directory cannot be accessed
        msg = prefix + '└── [Permission Denied]'
        print_colored(msg, Color.RED)
        return # End the recursion

    # If the directory is empty, we can end the recursion
    if not entries:
        return

    files = [] # List of fiels
    directories = [] # List of directories
    
    # Iterate over the directory entries
    for entry in entries:
        path = os.path.join(directory, entry) # Getting the full directory entry path
        # Checking if the entry is a directory, if it is, we add it to the directories list, otherwise, we add it to the files list
        if os.path.isdir(path):
            directories.append(entry)
        elif extension_filter is None or entry.endswith(extension_filter): # Check for extension filter if it's not None
            files.append(entry)

    items = directories + files # Concatenating the directories and files lists

    # Iterate over the items
    for i, item in enumerate(items): # We need `enumerate` to keep track of both the index and the item
        path = os.path.join(directory, item) # Getting the full path of the item
        is_last = i == len(items) - 1 # Check if the item is the last one in the list
        connector = '└── ' if is_last else '├── ' # Set the connector based on whether the item is the last one or not

        # If the permissions flag is set, we retrieve the permissions of the item
        if permissions:
            perms = get_permissions(path)
            item_str = f"{perms} {item}"
        else:
            item_str = item

        # We also need to check whether the human_readable flag is set and the item is a file
        if human_readable and os.path.isfile(path):
            size = os.path.getsize(path) # Get the size of the file
            item_str += f" ({human_readable_size(size)})" # Append the human-readable size to the item string

        # Using colorama to colorize the output
        if color:
            item_color = Color.BLUE if os.path.isdir(path) else Color.GREEN
            print_colored(prefix + connector + item_str, item_color, log=False)
        else:
            print_colored(prefix + connector + item_str, Color.RESET, log=False)

        # If the item is a directory, we need to call the tree function recursively
        if os.path.isdir(path):
            extension = '    ' if is_last else '│   ' # Set the extension based on whether the item is the last one or not
            next_prefix = prefix + extension # Set the next prefix
            # Recursively call the tree function with the next directory
            tree(path, prefix=next_prefix, depth_limit=depth_limit, depth=depth+1, extension_filter=extension_filter, color=color, permissions=permissions, human_readable=human_readable)

def faso():
    """Entry point of the script."""
    parser = argparse.ArgumentParser(description='Generate a directory tree in ASCII format.')
    parser.add_argument('directory', type=str, help='The directory path to generate the tree for.')
    parser.add_argument('--extension', '-e', type=str, help='Filter files by extension.')
    parser.add_argument('--depth', '-d', type=int, help='Limit the depth of the tree traversal.')
    parser.add_argument('--color', action='store_true', help='Enable colorized output.')
    parser.add_argument('--permissions', action='store_true', help='Show file/directory permissions.')
    parser.add_argument('--human-readable', '-hr', action='store_true', help='Show file sizes in a human-readable format.')
    parser.add_argument('--log', '-l', type=str, help='Log file path (default: tree.log).')
    parser.add_argument('--log-level', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO', help='Set the logging level (default: INFO).')
    args = parser.parse_args()

    setup_logging(log_file=args.log if args.log else 'tree.log', log_level=getattr(logging, args.log_level))

    if not os.path.isdir(args.directory):
        print_colored(f"Error: '{args.directory}' is not a valid directory.", Color.RED)
        return

    tree(args.directory, depth_limit=args.depth, extension_filter=args.extension, color=args.color, permissions=args.permissions, human_readable=args.human_readable)
    
if __name__ == '__main__':
    faso()