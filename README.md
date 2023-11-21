# Linux Simple Commands

A collection of simple Linux commands implemented in Python, providing basic functionalities to perform common file and directory operations through the command line interface.

## Description

The Linux Simple Commands project aims to simplify and streamline common tasks performed in a Linux environment. It offers a set of command line options that allow users to interact with files and directories efficiently.

## Features

- List of files and directories in a selected path.
- Change the current working directory.
- Create new directories.
- Remove empty directories.
- Delete files.
- Remove directories and their contents recursively.
- Copy files or directories to a specified destination.
- Move files or directories to a specified destination.
- Search for files or directories by name.
- Display the content of a file.
- Find occurrences of a word pattern in a file.
- Search files with a specified word pattern in a directory (including subdirectories).
- Log executed commands and view command history.

## Usage

Run the linux_toolkit.py script using Python with the desired arguments:

```bash
python linux_toolkit.py --ls 
python linux_toolkit.py --cd "AddressOfDirectory"
python linux_toolkit.py --mkdir "DirectoryName"
python linux_toolkit.py --rmdir "DirectoryName"
python linux_toolkit.py --rm "FileName"
python linux_toolkit.py --rm-r "FolderOrFileName"
python linux_toolkit.py --cat "FileName"
python linux_toolkit.py --cd "AddressOfDirectory" --ls
python linux_toolkit.py --cd "AddressOfDirectory" --mkdir "DirectoryName"
python linux_toolkit.py --cd "AddressOfDirectory" --rmdir "DirectoryName"
python linux_toolkit.py --cd "AddressOfDirectory" --rm "FileName"
python linux_toolkit.py --cd "AddressOfDirectory" --rm-r "FolderOrFileName"
python linux_toolkit.py --cd "AddressOfDirectory" --cat "FileName"
python linux_toolkit.py --cp "Source" "Destination"
python linux_toolkit.py --mv "Source" "Destination"
python linux_toolkit.py --find "Path" "Pattern"
python linux_toolkit.py --word-f "FilePath" "Pattern"
python linux_toolkit.py --search-w "Path" "Pattern"
python linux_toolkit.py --show-log
```

### Arguments

- `--ls`: shows the files in selected path (can be used with `--cd`).
- `--cd`: Changes directory to selected path.
- `--mkdir`: Creates folder (can be used with `--cd`).
- `--rmdir`: Deletes directory if it's empty (can be used with `--cd`).
- `--rm`: Removes a file (can be used with `--cd`).
- `--rm-r`: Removes directory and their contents (can be used with `--cd`)
- `--cat`: Displays the content of a file (can be used with `--cd`).
- `--cp`: Copies and pastes a file or directory from source path to destination path.
- `--mv`: Moves a file or directory from source path to destination path.
- `--find`: searchs for files or directories by name.
- `--word-f`: Find occurrences of a word pattern in a file.
- `--search-w`: Search files with a specified word pattern in a directory.
- `--show-log`: view command history.

## logs

Logs of the executed commands are stored in `command.log`, with each entry timestamped.

### Prerequisites

- Python 3.x installed on your system


