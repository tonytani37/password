import os

def get_file_sizes(directory):
    file_sizes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_sizes[file_path] = os.path.getsize(file_path)
    return file_sizes

def compare_directories(dir1, dir2):
    sizes1 = get_file_sizes(dir1)
    sizes2 = get_file_sizes(dir2)
    
    different_sizes = []
    
    for file in sizes1:
        relative_path = os.path.relpath(file, dir1)
        file_in_dir2 = os.path.join(dir2, relative_path)
        
        if file_in_dir2 in sizes2:
            if sizes1[file] != sizes2[file_in_dir2]:
                different_sizes.append((relative_path, sizes1[file], sizes2[file_in_dir2]))
        else:
            different_sizes.append((relative_path, sizes1[file], 'Not Found'))
    
    for file in sizes2:
        relative_path = os.path.relpath(file, dir2)
        file_in_dir1 = os.path.join(dir1, relative_path)
        
        if file_in_dir1 not in sizes1:
            different_sizes.append((relative_path, 'Not Found', sizes2[file]))
    
    return different_sizes

def save_differences_to_file(differences, filename):
    with open(filename, 'w') as file:
        for diff in differences:
            file.write(f"File: {diff[0]}, Size in dir1: {diff[1]}, Size in dir2: {diff[2]}\n")

dir1 = '/Volumes/Data/Photo'
dir2 = '/Volumes/Data1/Photo'
output_file = 'differences.txt'

differences = compare_directories(dir1, dir2)
save_differences_to_file(differences, output_file)
print(f"Differences saved to {output_file}")


# import os

# def get_file_sizes(directory):
#     file_sizes = {}
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             file_sizes[file_path] = os.path.getsize(file_path)
#     return file_sizes

# def compare_directories(dir1, dir2):
#     sizes1 = get_file_sizes(dir1)
#     sizes2 = get_file_sizes(dir2)
    
#     different_sizes = []
    
#     for file in sizes1:
#         relative_path = os.path.relpath(file, dir1)
#         file_in_dir2 = os.path.join(dir2, relative_path)
        
#         if file_in_dir2 in sizes2:
#             if sizes1[file] != sizes2[file_in_dir2]:
#                 different_sizes.append((relative_path, sizes1[file], sizes2[file_in_dir2]))
#         else:
#             different_sizes.append((relative_path, sizes1[file], 'Not Found'))
    
#     for file in sizes2:
#         relative_path = os.path.relpath(file, dir2)
#         file_in_dir1 = os.path.join(dir1, relative_path)
        
#         if file_in_dir1 not in sizes1:
#             different_sizes.append((relative_path, 'Not Found', sizes2[file]))
    
#     return different_sizes

# dir1 = '/Volumes/Data/Photo'
# dir2 = '/Volumes/Data1/Photo'

# differences = compare_directories(dir1, dir2)
# # for diff in differences:
# #     print(f"File: {diff[0]}, Size in dir1: {diff[1]}, Size in dir2: {diff[2]}")


