def removeprodtest():
      import os
      a = 'C:\InventorySystemPython\snippets\BcodeSample'
      b = str(input("Enter the Barcode No. :"'\n'))
      a1 = "\\"
      c = '.txt'
      address = a + a1 + b + c
      os.remove(address)




def mainprodadd2():
 a = input('Continue?''\n''1- Remove Product | other- Stop Program ''\n')
 match a:
      case '1':
            removeprodtest()
            mainprodadd2()
      case _:
            quit()

mainprodadd2()

