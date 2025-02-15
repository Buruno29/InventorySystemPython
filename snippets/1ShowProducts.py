# Import Module 
import os 
  
# Folder Path 
path = "C:\InventorySystemPython\snippets\BcodeSample"
  
# Change the directory 
os.chdir(path) 
  
# Read text File 
  
print('====All Products:====''\n')  
print('(The barcodes of the products for consultation are in the file names before the ".txt" and after the "BcodeSample")\n')
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