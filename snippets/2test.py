def purchasetest2():
      ListPurchase1 = []
      ListPurchase2 = []
      Sum = 0.0
      b2 = 0
      b = 1
      Discount = 0
      print('====Sistema de Compra by [SheepGaming]====')
      while b != b2:
                'a'
                a = 'C:\MNQ Project\snippets\BcodeSample'
                b = str(input("Insert Barcode:"'\n'))
                if b == '0':
                    print("\n===Finalizado==="'\n')
                    break
                a1 = "\\"
                c = '.txt'
                address = a + a1 + b + c 
                f = open (str(address), 'r')
                name = f.readline()
                no = f.readline()
                price = f.readline()
                print(':::',name, no, price)
                price3 = price
                print('Name and Price:''\n', name, '\n', 'price: ', price, '\n')
                ListPurchase1.append(name)
                ListPurchase2.append(price)
                Sum = Sum + float(price)
                f.close()
                no2 = int(no)
                no2 -= 1
                
                Finalwrite = name + str(no2) + '\n' + str(price3)
                f = open (str(address), 'w')
                f.write(str(Finalwrite))
            
purchasetest2()
