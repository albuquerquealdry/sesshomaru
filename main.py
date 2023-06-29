from src import command
import sys

def main():
    if sys.argv[1] == "-c":
        c = command.CustomCommads()
        c.callCommand(f"{sys.argv[2]}")

if __name__ == '__main__':
    main()