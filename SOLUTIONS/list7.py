#create a list of 5 value with filename and extension.replace with ".c" with ".py" and print new list.
def replace_c_with_py(filenames):
    updated_filenames = []
    for filename in filenames:
        if filename.endswith(".c"):
            updated_filenames.append(filename[:-2] + "py")
        else:
            updated_filenames.append(filename)
    return updated_filenames
filenames = ["program.c", "stdio.c", "sample.c", "a.py", "math.py", "hpp.py"]
updated_filenames = replace_c_with_py(filenames)
print(updated_filenames)
