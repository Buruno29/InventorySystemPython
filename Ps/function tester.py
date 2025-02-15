def Pass():
      Typedpass = input(print('\n Enter Password:\n'))
      file_path ='C:\MNQ Project\Main\passtemp.txt'
      with open(file_path, 'r') as file:
           Passw = file.read()
      
      if Passw != Typedpass:
            exit()

Pass()

print ('afasga')