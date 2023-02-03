import sys
def read_inside(txt):
    print(txt, file=sys.stderr)
    with open(txt) as f:
        contents = f.read()
    
    print(contents, file=sys.stderr)
    return contents

def split_five(string):
    string = [(string[i:i+5]) for i in range(0, len(string), 5)]
    string = " ".join(string)
    return string