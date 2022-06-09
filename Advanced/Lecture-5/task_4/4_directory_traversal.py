from genericpath import isdir
from os import listdir
from os.path import join


def printing(result):
    for k, v in result.items():
        with open('./report.txt', 'a') as f:
            f.write(f".{k} \n")
            [f.write(f"- - - {x} \n") for x in v]


def directory_traversal(path, files_by_ext):
    for el in listdir(path):
        if isdir(join(path, el)):
            directory_traversal(join(path, el), files_by_ext)
        else:
            extension = el.split('.')[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(el)


result = {}
directory_traversal('./', result)
result = dict(sorted(result.items(), key=lambda x: x[0].lower()))
printing(result)
