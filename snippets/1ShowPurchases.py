# Import Module 
import os 
  
# Folder Path 
path = "C:\InventorySystemPython\snippets\Purchase"
  
# Change the directory 
os.chdir(path) 
  
# Read text File 
  
print('====All Purchases:====''\n')  
print('\n')
def read_text_file(file_path): 
    with open(file_path, 'r') as f: 
        print(f.read()) 
  
  
# iterate through all file 
for file in os.listdir(): 
    # Check whether file is in text format or not 
    if file.endswith(".txt"): 
        file_path = f"{path}\{file}"
        print(file_path)
  
        # call read text file function 
        read_text_file(file_path)