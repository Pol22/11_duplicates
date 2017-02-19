import os
import sys


file_dict = {}
return_list = []


def get_duplicate_files(path):
    content = os.scandir(path)
    for item in content:
        if item.is_dir():
            get_duplicate_files(item.path)
        else:
            file_size = item.stat().st_size
            size_list = file_dict.setdefault(item.name, {}).keys()
            if len(size_list):
                if file_size in size_list:
                    return_list.append(item.path+" | " +
                                       file_dict[item.name][file_size])
            else:
                file_dict[item.name][file_size] = item.path
    return return_list


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Input path to second argument")
        exit()
    path = sys.argv[1]

    if not os.path.isdir(path):
        print("Incorrect path")
        exit()

    path_to_files = get_duplicate_files(path)

    print("Deleted duplicate files:")
    if not len(path_to_files):
        print("None")
    for path in path_to_files:
        # os.unlink(path)
        print(path)
