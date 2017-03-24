import os
def rename_files():
	# get file names from a folder
    file_list = os.listdir(r"/Users/yuepan/GitHub/udacity-python/examples/prank")
    print(file_list)

    # get current working directory
    saved_path = os.getcwd();
    print("Current Working Directory is " + saved_path)

    os.chdir(r"/Users/yuepan/GitHub/udacity-python/examples/prank")

    # for each file, remae file name
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    print(file_list)

    # change the path back to its original working directory
    os.chdir(saved_path)
    

rename_files()
