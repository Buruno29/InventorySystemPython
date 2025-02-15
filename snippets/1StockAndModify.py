def modifyproduct():
      a = 'C:\InventorySystemPython\snippets\BcodeSample'
      b = str(input("Enter the Barcode No.:"'\n'))
      a1 = "\\"
      c = '.txt'
      address = a + a1 + b + c
      Quant = str(input("Product Quantity:"'\n'))
      name = str(input("Product name:"'\n'))
      price = float(input("Price:"'\n'))

      FinalWrite = name + '\n' + Quant + '\n' + str(price) 
      f = open (str(address), 'w')
      f.write (str(FinalWrite))
      f.close

def addstock():
      a = 'C:\InventorySystemPython\snippets\BcodeSample'
      b = str(input("Enter the Barcode No.:"'\n'))
      a1 = "\\"
      c = '.txt'
      address = a + a1 + b + c
      f = open (str(address), 'r')
      name0 = f.readline()
      quantstock = f.readline() 
      print('Quantidade atual:',quantstock)
      price0 = f.readline()
      f.close()
      Quant = str(input("Insert the Quantity to change:"'\n''(Pay in mind that you are not adding, you are changing final value)''\n'))
      name = name0
      

      FinalWrite = name + Quant + '\n' + str(price0) 
      f = open (str(address), 'w')
      f.write (str(FinalWrite))
      f.close 


def mainaddstock():
    matcher = input('===Modify Product or Add Stock===''\n''1- Modify Product | 2- Add Stock''\n')
    match matcher:
         case '1':
            modifyproduct()
            mainaddstock()
         case '2':
            addstock()
            mainaddstock()


mainaddstock()    
