import sys
def read_inside(txt):
    print(txt, file=sys.stderr)
    with open(txt) as f:
        contents = f.read()
    
    print("babi", file=sys.stderr)
    
    print(contents, file=sys.stderr)
    return contents