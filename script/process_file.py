# -*- coding: utf-8 -*-

PATH = '../content/Eo - Zamenhof, L.L_ - Fundamenta Krestomatio.md'



def del_garbage_line(lines):
    def is_garbage(line):
        if (len(line)==1 and line[0]=='\n'):
            return True
        return line.rstrip('\n').isdigit()
    return list(filter(lambda x:not is_garbage(x),lines))

def get_lines(path):
    with open(path) as f:
        res = f.readlines()
    return res

def split_para(lines):
    def is_para_start(line,former_line):
        start_mark = line.lstrip()[0]
        end_mark = former_line.lstrip()[-1]
        return end_mark == '.' and (start_mark.isupper() or start_mark == 'ˆ')

    new_lines=[]
    res = ''
    for i in range(len(lines)):
        res+=lines[i]
        if i <len(lines)-1 and is_para_start(lines[i+1],lines[i]):
            new_lines.append(res)
            res=''
    return new_lines

def deal_diacritic_slipped(lines):
    pass


def write_file(lines):
    pass

def main():
    lines = get_lines(PATH)
    res = write_file(del_garbage_line(deal_diacritic_slipped(file_list)))
    return res

if __name__ == '__main__':
    main()

