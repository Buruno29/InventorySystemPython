def addprodtest():
      print('==============='"\n")
      print('=======New Product:========'"\n")
      print('Attention: Do not use the code "0" to avoid errors''\n')
      a = 'C:\C:\InventorySystemPython\snippets\BcodeSample'
      b = str(input("Enter the Barcode No.:"'\n'))
      a1 = "\\"
      c = '.txt'
      address = a + a1 + b + c
      name = input("Product Name:"'\n')
      Quant = str(input("Enter Initial Quantity:"'\n'))
  
      price = float(input("Initial Price:"'\n'))

      FinalWrite = name + '\n' + Quant + '\n' + str(price) 
      try:
         f = open (str(address), 'x')
         f = open (str(address), 'w')
         f.write (str(FinalWrite))
         f.close
      except:
         print("\n""There is a product with the same barcode""\n")
         print("Open the program again")
      print('\n\'====Product Added:====''\n')
      f = open(str(address), 'r')
      print(f.read())
      f.close()
      print('====Execution Ended====')


      

        



def mainprodadd():
 a = input('Continue?''\n''1- New Product | other- Stop Program''\n')
 match a:
      case '1':
            addprodtest()
            mainprodadd()
      case _:
            quit()

mainprodadd()