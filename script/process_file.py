# -*- coding: utf-8 -*-

PATH = '../content/Eo - Zamenhof, L.L_ - Fundamenta Krestomatio.md'

def del_empty_line(file_lists):
    pass

def del_gabage_line(file_lists):
    pass

def get_file_lists(path):
    with open(path) as f:
        res = f.readlines()
    return res

def deal_diacritic_slipped(file_list):
    pass


def write_file(file_list):
    pass

def main():
    file_lists = get_file_lists(PATH)
    res = write_file(del_empty_line(del_gabage_line(deal_diacritic_slipped(file_list))))
    return res

if __name__ == '__main__':
    main()

