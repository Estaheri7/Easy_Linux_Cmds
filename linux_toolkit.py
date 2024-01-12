import argparse
import datetime
import sys
import os
import shutil

class LinuxCommands:
    # setting argument parser
    def __init__(self):
        self.parser = self.setup_parser()
        self.args = self.parser.parse_args()

    # setting arguments
    def setup_parser(self):
        parser = argparse.ArgumentParser(description="Linux simple commands")
        parser.add_argument("--ls", action="store_true", help="shows the files in selected path")
        parser.add_argument("--cd", type=str, help="change directory")
        parser.add_argument("--mkdir", type=str, help="make directory")
        parser.add_argument("--rmdir", type=str, help="removes directory if it's empty")
        parser.add_argument("--rm", type=str, help="removes file")
        parser.add_argument("--rm-r", type=str, help="removes directory")
        parser.add_argument("--cp", type=str, nargs=2, help="copy and paste")
        parser.add_argument("--mv", type=str, nargs=2, help="move the file to selected path")
        parser.add_argument("--find", type=str, nargs=2, help="search the file/directory")
        parser.add_argument("--cat", type=str, help="show the content of file")
        parser.add_argument("--word-f", type=str, nargs=2, help="finds a pattern in file")
        parser.add_argument("--search-w", type=str, nargs=2, help="search a file with words")
        parser.add_argument("--show-log", action="store_true", help="logs each command")
        return parser

    # writes in log command file
    def log_command(self, line):
        with open("command.log", "a") as log_file:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d")
            log_file.write(f"{current_time}: {line}\n")

    # shows the log commands
    def log_show(self):
        with open("command.log", "r") as log_file:
            return log_file.read()

    # gets a path and gives files and folders that are in the path
    def ls(self, path):
        file = os.listdir(path)
        for f in file:
            fod_path = os.path.join(path, f)
            if not os.path.isfile(fod_path):
                print(f"**{f}**", end=", ") # making special view for directories (like linux)
            else:
                print(f, end=", ")
    
    # changes directory to selected path
    def cd(self, path):
        try:
            os.chdir(path)
            print(f"Changed directory to {path}")
            return path
        except FileNotFoundError:
            return "Directory not found"
        except PermissionError:
            return "Permission denied"

    # makes directory by its name
    def mkdir(self, directory):
        try:
            os.makedirs(directory)
            print(f"Directory created successfully!")
        except FileExistsError:
            print("Directory already exists")

    # removes directory by its name if it's empty
    def rmdir(self, name):
        try:
            os.rmdir(name)
            print("Directory deleted successfully!")
        except NotADirectoryError:
            print("You have to select directory")
        except FileNotFoundError:
            print("Directory not found")
        except OSError as e: 
            print(e) # handling OS errors like (Directory is not empty)

    # removes a file
    def rm(self, file):
        try:
            os.remove(file)
            return "File deleted successfully!"
        except IsADirectoryError:
            return "It's a directory"
        except FileNotFoundError:
            return "File not found"

    # removes directory and all included files and directories in it
    def rm_r(self, directory):
        if os.path.isdir(directory):
            for path, directories, files in os.walk(directory):
                for f in files:
                    f_path = os.path.join(path, f)
                    os.remove(f_path)
                for d in directories:
                    d_path = os.path.join(path, d)
                    self.rm_r(d_path)
            os.rmdir(directory)
            return "Selected directory removed!"
        elif os.path.isfile(directory):
            os.remove(directory)
            return "Selected file removed!"
        else:
            return "File or Directory not found" # Trying to handle FileNotFoundError

    # copies a file from source to destination
    def cp(self, source, destination):
        try:
            file_name = os.path.basename(source)
            cp_file = os.path.join(destination, file_name)
            if os.path.isfile(source):
                shutil.copy(source, cp_file) # using shutil.copy to copy a file
                print("File copied!")
            else:
                shutil.copytree(source, cp_file) # using shutil.copytree to copy directory and it's files
                print("Folder copied!")
        except FileNotFoundError:
            print("File or Directory not found")
        except FileExistsError:
            print("File exists already") # handle shutil exceptions
        except shutil.Error as e:
            print(e)

    # moves (cuts) a file from source to destination
    def mv(self, source, destination):
        try:
            file_name = os.path.basename(source)
            cp_file = os.path.join(destination, file_name)
            if os.path.isfile(source):
                shutil.move(source, cp_file) # using shutil.move to move file
                print("File moved!")
            else:
                shutil.move(source, cp_file)
                print("Folder moved!")
        except FileNotFoundError:
            print("File or Directory not found")
        except FileExistsError:
            print("File exists already")
        except shutil.Error as e: # handle shutil exceptions
            print(e)

    # finds all files in the given path by the given pattern
    def find(self, path, pattern):
        try:
            for p, directories, files in os.walk(path):
                for f in files:
                    if f == pattern:
                        f_path = os.path.join(p, f)
                        print(f_path)
                for d in directories:
                    if d == pattern:
                        d_path = os.path.join(p, d)
                        print(d_path)
        except FileNotFoundError:
            print("File not found")
        except PermissionError:
            print("Perimission denied")

    # returns data of a file
    def cat(self, file):
        try:
            with open(file, "r") as file:
                data = file.read()
        except FileNotFoundError:
            return "File not found"
        except IsADirectoryError:
            return "It's a Directory"
        return data

    # finds words in the given file and showing the line (little grep)
    def word_find(self, f_path, pattern):
        count = 0
        try:
            with open(f_path, "r") as file:
                for n_line, line in enumerate(file, start=1):
                    if pattern in line:
                        print(f"Found {pattern} in line {n_line}!")
                        count += 1
                if count == 0:
                    print("Found nothing")
        except FileNotFoundError:
            print("File not found")
        except IsADirectoryError:
            print("It's a Directory")

    # searchs files by a word that given as pattern
    def search_by_word(self, path, pattern):
        files_with_pattern = []
        for p, d, files in os.walk(path):
            for file in files:
                file_path = os.path.join(p, file)
                try:
                    with open(file_path, "r") as p_file:
                        content = p_file.read()
                        if pattern in content:
                            files_with_pattern.append(file_path)
                except UnicodeDecodeError:
                    continue # trying to skip unreadable files ( encoding issue )

        return files_with_pattern

    def execute_command(self):
        #handle command logs
        if not self.args.show_log:
            command_line = " ".join(sys.argv)
            self.log_command(command_line)
        # adding functions that are related to change directory
        if self.args.cd:
            path = self.args.cd
            current_path = self.cd(path)
            if current_path != "Directory not found":
                if self.args.ls:
                    self.ls(current_path)
                elif self.args.mkdir:
                    name = self.args.mkdir
                    self.mkdir(os.path.join(current_path, name))
                elif self.args.rmdir:
                    name = self.args.rmdir
                    self.rmdir(name)
                elif self.args.rm:
                    name = self.args.rm
                    result = self.rm(name)
                    print(result)
                elif self.args.rm_r:
                    name = self.args.rm_r
                    result = self.rm_r(name)
                    print(result)
                elif self.args.cat:
                    name = self.args.cat
                    data = self.cat(name)
                    print(data)
            else:
                print(current_path)
        # using without cd function
        elif self.args.ls:
            self.ls(".")
        elif self.args.mkdir:
            name = self.args.mkdir
            self.mkdir(name)
        elif self.args.rmdir:
            name = self.args.rmdir
            self.rmdir(name)
        elif self.args.rm:
            file = self.args.rm
            result = self.rm(file)
            print(result)
        elif self.args.rm_r:
            f_d = self.args.rm_r
            result = self.rm_r(f_d)
            print(result)
        elif self.args.cat:
            path = self.args.cat
            data = self.cat(path)
            print(data)
        # other functions that are getting their own path
        elif self.args.cp:
            path = self.args.cp
            self.cp(path[0], path[1])
        elif self.args.mv:
            path = self.args.mv
            self.mv(path[0], path[1])
        elif self.args.find:
            path = self.args.find
            self.find(path[0], path[1])
        elif self.args.show_log:
            logs = self.log_show()
            print(logs)
        elif self.args.word_f:
            path = self.args.word_f
            self.word_find(path[0], path[1])
        elif self.args.search_w:
            path = self.args.search_w
            files = self.search_by_word(path[0], path[1])
            for f in files:
                print(f)
        else:
            self.parser.print_help()

if __name__ == "__main__":
    linux_commands = LinuxCommands()
    linux_commands.execute_command()
