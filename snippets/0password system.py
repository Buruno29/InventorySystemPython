def Pass():
      Typedpass = input(print('\n Enter Password:\n'))
      file_path ='C:\InventorySystemPython\Ps\passtemp.txt'
      with open(file_path, 'r') as file:
           Passw = file.read()
      
      if Passw != Typedpass:
            exit()

Pass()

print ('afasga')

#I havent implemented this in the codes, but if you see it necessary, just create a txt file with what ever password you want and change file_path, then you put this function
#At the top of the codes you need.