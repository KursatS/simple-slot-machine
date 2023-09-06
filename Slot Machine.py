#Rastgele sonuçlar için RANDOM kütüphanesi
import random

#Slot simgeleri ve olasılıkları
values = ["BAR","BAR","BAR","BAR","2XBAR","2XBAR","2XBAR","3XBAR","3XBAR","DIAMOND","CHERRY","7","JACKPOT"]

def slot_machine():
    print("Slot Makinesine Hoşgeldiniz\n-----")
    money = 10000

#Slot'u sürekli hale getiren while loop'u
    slot_loop = True
    while slot_loop:
        print("Bakiyeniz : {}$".format(money))
#Kullanıcıdan komut alma
        user_cmd = str(input("Çevirmek için enter tuşuna basınız.\nÇıkmak için c yazınız.\n"))
#Girilen değere göre farklı aksiyon
        if user_cmd.lower() == "c":
            print("Slot Makinesinden çıkış yaptınız. Tekrar bekleriz.")
            break
        elif user_cmd == "":
            if money >= 500:
                value1 = random.choice(values)
                value2 = random.choice(values)
                value3 = random.choice(values)

                print("{} {} {}".format(value1,value2,value3))
#Bazı simgeler için farklı kazanç
                if value1 == value2 == value3:
                    print("Tebrikler kazandınız.")
                    if value1 == "7":
                        money += 3500
                    elif value1 == "JACKPOT":
                        money += 10000
                    elif value1 == "DIAMOND":
                        money += 2500
                    elif value1 == "2XBAR":
                        money += 1000
                    elif value1 == "3XBAR":
                        money += 1500
                    else:
                        money += 500
                else:
                    money -= 500
                    print("Kaybettiniz!")
            else:
                print("Bakiyeniz yetersiz.")
        else:
            print("Yanlış girdi!!")

slot_machine()