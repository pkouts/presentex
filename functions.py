import re

class EnvironmentNode:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.children = []
        self.parent = []

class PresentationTree:
    def __init__(self):
        self.nodes = []
    
    # def __init__(self, file_content):
    #     envs = extract_environments(file_content)
    #     for env in envs:
    #         en_parent = EnvironmentNode(env[0], env[1])
    #         idx_parent = pt.addNode(en_parent)

    
    
    def addNode(self, env):
        self.nodes.append(env)
        return len(self.nodes)-1

    def printNodeList(self):
        for i in range(len(self.nodes)):
            print( str(i) + ": " + self.nodes[i].name )

    def printNodeChildren(self):
        for i in range(len(self.nodes)):
            print( str(i) + " --> " + str(self.nodes[i].children) )

    





def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

def extract_environments(latex_content):
    pattern = r'\\begin\{(.*?)\}(.*?)\\end\{\1\}'
    environments = re.findall(pattern, latex_content, re.DOTALL)
    return environments