import os
import sys


def generate_tree(indent=''):
    dir_path = input("Enter file path:")
    """Recursively generates a tree structure for a given directory."""
    contents = os.listdir(dir_path)
    files = []
    dirs = []
    for item in contents:
        if os.path.isfile(os.path.join(dir_path, item)):
            files.append(item)
        else:
            dirs.append(item)

    files.sort()
    dirs.sort()

    for file in files:
        print(f"{indent}├── {file}")
    for idx, dir in enumerate(dirs):
        if idx == len(dirs) - 1:
            print(f"{indent}└── {dir}")
            generate_deeper_tree(os.path.join(dir_path, dir), f"{indent}    ")
        else:
            print(f"{indent}├── {dir}")
            generate_deeper_tree(os.path.join(dir_path, dir), f"{indent}│   ")


def generate_deeper_tree(dir_path, indent=''):
    contents = os.listdir(dir_path)
    files = []
    dirs = []
    for item in contents:
        if os.path.isfile(os.path.join(dir_path, item)):
            files.append(item)
        else:
            dirs.append(item)

    files.sort()
    dirs.sort()

    for file in files:
        print(f"{indent}├── {file}")
    for idx, dir in enumerate(dirs):
        if idx == len(dirs) - 1:
            print(f"{indent}└── {dir}")
            generate_deeper_tree(os.path.join(dir_path, dir), f"{indent}    ")
        else:
            print(f"{indent}├── {dir}")
            generate_deeper_tree(os.path.join(dir_path, dir), f"{indent}│   ")


if __name__ == '__main__':
    generate_tree()
