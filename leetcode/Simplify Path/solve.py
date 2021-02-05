import re

class Directory:

    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = {}

    def get_parent(self):
        if self.parent == None: # root
            return self
        return self.parent

    def get_next_dir(self, directory_name):
        if directory_name == '.':
            return self
        if directory_name == '..':
            return self.get_parent()
        
        if directory_name in self.children:
            return self.children[directory_name]
        
        new_directory = Directory(directory_name, self)
        self.children[directory_name] = new_directory
        return new_directory

    def get_canonical_path(self):
        if self.parent == None:
            return ""
        return self.get_parent().get_canonical_path() + '/' + f"{self.name}"

class Solution:
    selected_dir = None
    root = None

    def clean(self, path):
        return re.sub(r'/+', '/', path)

    def simplifyPath(self, path: str) -> str:
        path = self.clean(path)[1:]

        if path.endswith("/"):
            path = path[:-1]
        
        tokens = path.split('/')
        
        self.selected_dir = self.root = Directory("", None)

        for token in tokens:
            self.selected_dir = self.selected_dir.get_next_dir(token)
        
        if self.selected_dir.parent == None:
            return '/'

        return self.selected_dir.get_canonical_path()
