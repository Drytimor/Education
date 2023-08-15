from os import listdir, path
def search_file(name: str, path_file=r"/Users/andrejoveskov/PycharmProjects", res_search=[]):
    for i in listdir(path_file):
        if i == name:
            res_search.append(path_file + "//" + i)
        if path.isdir(path_file + "//" + i):
            search_file(name, path_file + "//" + i)
    for elem in res_search:
        return elem
search_file("")


