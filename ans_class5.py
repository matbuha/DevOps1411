import shutil

source = "C:/Users/UserPc/Desktop/deveops/source/NAME2.txt"
destination = "C:/Users/UserPc/Desktop/deveops/destination/NAME2.txt"
move_file = shutil.move(source, destination)
print(move_file)
