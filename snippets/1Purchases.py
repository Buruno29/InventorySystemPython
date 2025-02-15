def purchasetest():
      ListPurchase1 = []
      ListPurchase2 = []
      Sum = 0.0
      b2 = 0
      b = 1
      Discount = 0
      print('====Purchase System by [SheepGaming]====')
      try:
             while b != b2:
                'a'
                a = 'f\snippets\BcodeSample'
                b = str(input("Enter the Barcode No.:"'\n'))
                if b == '0':
                    print("\n===Insertion Finished==="'\n')
                    break
                a1 = "\\"
                c = '.txt'
                address = a + a1 + b + c 
                f = open (str(address), 'r')
                name = f.readline()
                no = f.readline()
                price = f.readline()
                #print(':::',name, no, price)
                price3 = price
                print('Nome:''\n', name, '\n', 'preço: ', price, '\n')
                ListPurchase1.append(name)
                ListPurchase2.append(price)
                Sum = Sum + float(price)
                f.close()
                no2 = int(no)
                no2 -= 1
                
                Finalwrite = name + str(no2) + '\n' + str(price3)
                f = open (str(address), 'w')
                f.write(str(Finalwrite))


      except:
             print("\n===Insertion Finished==="'\n')
      Discount = float(input("Discount (press '0' and Enter if none):"'\n'))     
      Sum = Sum - Discount
      
      import os

      dir_path = r'C:\InventorySystemPython\snippets\Purchase'
      count = 0
# Iterate directory
      for path in os.listdir(dir_path):
# check if current path is a file
          if os.path.isfile(os.path.join(dir_path, path)):
              count += 1

      i = 0
      try:
           address2 = 'C:\InventorySystemPython\snippets\Purchase'+'\\'+'purchase' + str(count) + '.txt'
           f = open (str(address2), 'x')
           f = open (str(address2), 'a')
      except:
           try:
               address2 = 'C:\InventorySystemPython\snippets\Purchase'+'\\'+'purchase' + str(count) + '(1)' + '.txt'
               f = open (str(address2), 'x')
               f = open (str(address2), 'a')
           except:
               try: 
                   count += 1
                   address2 = 'C:\InventorySystemPython\snippets\Purchase'+'\\'+'purchase' + str(count) + '(1)'+ '.txt'
                   f = open (str(address2), 'x')
                   f = open (str(address2), 'a') 
               except: 
                    count += count
                    address2 = 'C:\InventorySystemPython\snippets\Purchase'+'\\'+'purchase' + str(count) + '(1)'+ '.txt'
                    f = open (str(address2), 'x')
                    f = open (str(address2), 'a') 
            
      awfg = '\n'

      while i < len(ListPurchase1):
          
          print(ListPurchase1[i])
          name2 = ListPurchase1[i]
          awfg1 = awfg + str(name2)
          f.write(str(awfg1))
          print(ListPurchase2[i])
          price2 = ListPurchase2[i]
          awfg2 = awfg + 'Price: ' + str(price2) + "\n"
          f.write(str(awfg2))

          i += 1
      writen = "Total:"+"  ",str(Sum)
      writen2 = "Discount:"+"  ",str(Discount)
      f.write('\n')
      f.write(str(writen))  
      f.write('\n')
      f.write(str(writen2))          
      print("Total:""\n", Sum) 
      print("\n""Document Address:""\n", address2)
      f.close()
      printin = input('\n Do you want to Print?:'"\n 1- For 'yes' | Other- New Purchase""\n""Close the program if you want to finish"'\n')
      if printin == '1':
           
        os.startfile(address2, "print")
      else:
        purchasetest()




   


purchasetest()    