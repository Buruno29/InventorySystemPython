import os
def CompressAndDestroy():
  a = 'EndereçoDaPasta'
  i = 0
  dir_path = r'C:\InventorySystemPython\snippets\Purchase'
  count = 0
  print("Saving and Deleting...""\n")
  path = "C:\InventorySystemPython\snippets\Purchase"
  
# Change the directory 
  os.chdir(path) 
#adaptar código abaixo para Ler tudo, salvar em Listas e nos próximos códigos acessaremos essas listas
  ListPurchase = []
  print('====All Purchases:====''\n')  
  print('\n')
  def read_text_file(file_path): 
      with open(file_path, 'r+') as f:  
          a = f.read()
          ListPurchase.append(a)


  for file in os.listdir(): 
    # Check whether file is in text format or not 
    if file.endswith(".txt"): 
        file_path = f"{path}\{file}"
        print(file_path)
  
        # call read text file function 
        read_text_file(file_path)
       
  b = 0
  c = len(ListPurchase)

  def Escreverarq():
        try:
           fnamen = input('Document Name:''\n')
           fnamen2 = 'C:\InventorySystemPython\snippets\PurchaseCluster' + '\\' + fnamen + '.txt'
           f = open(str(fnamen2), 'x') 
           f = open(str(fnamen2), 'a') 
           for x in ListPurchase:
              f.write(str(x))
              f.write('\n''=========''\n')
        except: 
          print("Possible error with document name"'\n')
          Escreverarq()            
  Escreverarq()

         

def delete_files_in_directory(directory_path):
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files in the Purchase folder were successively deleted and compressed in the PurchaseCluster."'\n')
   except OSError:
     print("Error occured on Deleting the files."'\n')


directory_path = 'C:\InventorySystemPython\snippets\Purchase'
CompressAndDestroy()
delete_files_in_directory(directory_path) 
      




