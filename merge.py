import sys
import json

if len(sys.argv) <= 2:
    raise ValueError('meger error: two file or more are required!')

if len(sys.argv) == 4 and sys.argv[3].find('-mode=')==-1:
    raise ValueError('The last parameter must be -mode')

base = sys.argv[1]
head = sys.argv[2]

print(f'base name: {base}, head name: {head}')

with open(base, 'r', encoding='utf-8') as basefile:
    base_content = json.loads(basefile.read())

with open(head, 'r', encoding='utf-8') as headfile:
    head_content = json.loads(headfile.read())

def check_base_conflict(_dict):
    for w in base_content:
        if w == _dict:
            return w

def merge(mode='discarded'):
    for w in head_content:
        result = check_base_conflict(w)
        if result is None:
            print(f'追加项: {w}')
            base_content.append(w)
    with open(base, 'w', encoding='utf-8') as writefile:
        base_json = json.dump(base_content, writefile, sort_keys=True, indent=4, separators=(',', ':'))



def check(arg):
    for w in head_content:
        result = check_base_conflict(w)
        if result:
            print(f"存在相同的项: {result}")


def exec(*args):
    input_mode = "merge"
    if len(sys.argv) == 4:
        input_mode = sys.argv[3].split('=')[1]

    mode_func = {
        'merge': merge,
        'check': check
    }
    func = mode_func.get(input_mode, merge)
    if func:
        return func(args)

if __name__ == "__main__":
    exec()
