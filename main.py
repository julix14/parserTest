import xml.dom.minidom
from os import listdir
from os.path import isfile, isdir, join
import re

def select_files_from_folder():
    path = './'
    files = listdir(path)
    for file in files:
        if not (file.endswith(".x83") or file.endswith(".X83")):
            files.remove(file)
            
    print(str(files))
    return files

def format_xml(file):
    dom = xml.dom.minidom.parse(file)
    return dom.toprettyxml()


def parse_93(content):
    result = {}
    stack = [result]

    for line in content.split("\n"):
        line = line.strip()
        if not line:
            continue

        if line.startswith("#begin["):
            key = line[7:-1]
            new_dict = {}
            stack[-1][key] = new_dict
            print(key)
            stack.append(new_dict)
        
        elif line.startswith("#end["):
            stack.pop()
        
        elif line.startswith("["):
            print('Stack = ', stack)

            match = re.match(r"\[(\w+)\](.+)\[end\]", line)
            if match:
                key = match.group(1)
                value = match.group(2)
                stack[-1][key] = value
                
        
    return result




def main():
    with open("PA23-0011178_GAEB.P93", encoding= 'unicode_escape') as f:
        content = f.read()
        final_result = parse_93(content) 
        print('-----------------')
        print()
        print('-----------------')
    
        
        
if __name__ == "__main__":
    main()