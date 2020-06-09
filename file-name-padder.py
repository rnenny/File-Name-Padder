import os

try:
    os.chdir('C:/Users/rnenninger/Documents/! SDS/SDS Sheets') # changes working directory to the following
    print("Directory Changed")
    print(os.getcwd())  # prints current working directory

except OSError:
    print("Cannot change current working directory")

def main():
    for file in os.listdir():
        file_name, file_extension = os.path.splitext(file) # Splits the file extension and file name and assigns them to a variable
        file_name = file_name.zfill(4) # Pads filename with 0s to make a 4 digit name
        new_name = file_name + file_extension # Combines padded filename and file extension to a single string
        os.rename(file, new_name) # renames the file

main()