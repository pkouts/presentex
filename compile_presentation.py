#!/bin/python3

from functions import *

import re

# class EnvironmentNode:
#     def __init__(self, name, content):
#         self.name = name
#         self.content = content
#         self.children = []

# def read_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             return content
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")
#     except IOError:
#         print(f"Error reading file '{file_path}'.")

# def extract_environments(latex_content):
#     pattern = r'\\begin\{(.*?)\}(.*?)\\end\{\1\}'
#     environments = re.findall(pattern, latex_content, re.DOTALL)
#     return environments

# def build_environment_tree(environments):
#     root = EnvironmentNode("document", "")  # Root node representing the document
#     stack = [root]
#     for env_name, env_content in environments:
#         current_node = EnvironmentNode(env_name, env_content)
#         parent_node = stack[-1]
#         parent_node.children.append(current_node)
#         stack.append(current_node)
#         if env_name == 'document':
#             stack = [root]
#     return root

# def build_environment_tree_aux(file_content, parent_node_id):
#     current_node = EnvironmentNode(env_name, env_content)

#     return 

# def build_environment_tree(file_content):
#     root = EnvironmentNode("document", "")  # Root node representing the document
#     stack = [root]
#     envs = extract_environments(file_content)
#     for env_name, env_content in envs:
#         current_node = EnvironmentNode(env_name, env_content)
#         stack.append(current_node)
        

#     return root

# def print_environment_tree(node, indentation=""):
#     print(f"{indentation}Environment: {node.name}")
#     print(f"{indentation}Content:\n{node.content}\n")
#     for child in node.children:
#         print_environment_tree(child, indentation + "  ")



# def compile_presentation(file_content):
#     environments = extract_environments(file_content)
#     root_node = build_environment_tree(environments)
#     print_environment_tree(root_node)
#     return

# Example usage
file_path = './examples/example.ptex'  # Replace with the actual file path
file_content = read_file(file_path)
# if file_content:
#     print(file_content)
envs = extract_environments(file_content)

pt = PresentationTree()

iii = 0
for env in envs:
    print(env[0]+":\n")
    print(env[1])
    en_parent = EnvironmentNode(env[0], env[1])
    idx_parent = pt.addNode(en_parent)

    print(str(iii))
    iii = iii + 1

    envs_child = extract_environments(env[1])
    cnt = 0
    idx_child = [None] * (len(envs_child))
    for child in envs_child:
        print(child[0]+":\n")
        print(child[1])
        en_child = EnvironmentNode(child[0], child[1])
        en_child.parent = idx_parent
        idx_child[cnt] = pt.addNode(en_child)
        cnt = cnt + 1

    pt.nodes[idx_parent].children = idx_child





pt.printNodeList()
pt.printNodeChildren()