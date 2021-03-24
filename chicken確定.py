import random

class chicken():
    def __init__(self,name,age,weight):
        self.age = age
        self.weight = weight
        self.name = name
    def toPrint(self):
        print("名字 :",self.name,"，現在",self.age,"個月，體重",self.weight,"公克")




w = random.randint(40,60) #決定體重(g)
a = 0
m = 1000 #錢
water = 5 #身體水分
eF = 5 #飼料
eW = 5 #水
s = random.randint(0,1)
if s==0:
    s=("母雞")
else:
    s=("公雞")

print("規則 : 歡迎來到電子雞的世界，請小心照顧，不然黃語柔會傷心。")
print("目標 : 和雞一起成為大富翁 ! 賺到 3000 元即過關。")
print("提示 : 輸入 y 表示確認，n 表示不要")
print("-")
print("恭喜玩家獲得一隻",s," ! 從今天開始你必須負責將牠養大，請用心照顧喔 ! ")
name = str(input("現在來幫他取個名字吧 : "))
sC = chicken(name,a,w) #初始設定
print("-")
sC.toPrint()
print("錢包 :",m,"元")
Ins = str(input("請問要保保險嗎 ? (費用 250 元)"))

  
if Ins == "y" :
    print("購買成功 !")
    m = 750
    print("-")
    while m < 3000 :
        print("錢包 :",m,"元")
        print("飼料 :",eF,"份 ，水 :",eW,"份")
        print("功能 : (1)餵食  (2)喝水  (3)進行才藝表演  (4)購買飼料(一包25元)  (5)購買水(一瓶25元)")
        f = int(input("請選擇功能 :"))
        if f == 1 : 
            print("--")
            if eF > 0:
                addW = random.randint(80,100)
                w += addW
                water -= 0.5
                a += 1
                eF -= 1
                C = chicken(name,a,w)
                print("餵食成功 !")
                print("-")
                C.toPrint()
            else :
                print("飼料不足!請去購買!")
                print("-")
                C.toPrint()                
        if f == 2 :
            print("--")
            if eW > 0:
                addW = random.randint(40,50)
                w += addW
                water += 1
                a += 1
                eW -= 1
                C = chicken(name,a,w)
                print("餵水成功 !")
                print("-")
                C.toPrint()
            else :
                print("水不足!請去購買!")
                print("-")
                C.toPrint()
        if f == 3 :
            print("--")
            if a >= 10 :
                show = random.randint(1,4)
                addW = random.randint(30,50)
                w -= addW
                water -= 0.5
                a += 1
                C = chicken(name,a,w)
                if show == 1 :
                    m += 100
                    print("今天表演狀況較差，沒賺到太多錢，真可惜。但還是恭喜賺進 100 元。")
                if show == 2 :
                    m += 200
                    print("今天表現不錯喔 ! 雞看起來真可愛。賺進 200 元。")
                if show == 3 :
                    m += 200
                    print("今天表現不錯喔 ! 雞看起來真可愛。賺進 200 元。")
                if show == 4 :
                    m += 300
                    print("哇 ! 今天的表演太精采了吧 ! marvelous ! 恭喜賺到 300 元 !")
                print("-")
                C.toPrint()
            else:
                print("請勿壓榨童雞!")
        if f == 4 : 
            print("--")
            mF = int(input("請問需要購買幾包飼料?"))    
            eF = eF + mF
            m = m - mF*25
        if f == 5 : 
            print("--")
            mW = int(input("請問需要購買幾瓶水?"))    
            eW = eW + mW
            m = m - mW*25
        if water <= 1 :
            print("---")
            print("你的電子雞因缺水而死亡了，QQ")
            print("---")
            ans = int(input("請問保險要(1)換雞復活還是(2)換現金 750 元 (請輸入1或2)(需再花費 250 元) :"))
            m -= 250
            if ans == 1 :
                water += 4
                print("恭喜你的雞復活了 ! 請小心不要讓牠再死了喔 !")
                print("--")
                C.toPrint()
            if ans == 2 :
                m += 750
                print("-")
                print("恭喜你換得 750 元 ~")
                print("--")
                if m >= 3000 :
                    break
                else :
                    print("-")
                    print("太可惜了，你還不是位稱職的養雞大富翁。")
                    break
            
        if a >= 20 :
            if w <= 800 :
                print("---")
                print("你的雞太瘦了，工作太累沒進食，現在餓死了。")
                print("---")
                ans1 = int(input("請問保險要(1)換雞復活還是(2)換現金 750 元(請輸入1或2)(需再花費 250 元) :"))
                m -= 250
                if ans1 == 1 :
                    w = w + 250
                    print("恭喜你的雞復活了 ! 請小心不要讓牠再死了喔 !")
                    print("--")
                    C = chicken(name,a,w)
                    C.toPrint()
                if ans1 == 2 :
                    m += 750
                    print("-")
                    print("恭喜你換得 750 元 ~")
                    print("--")
                    if m >= 3000 :
                        break
                    else :
                        print("-")
                        print("太可惜了，你還不是位稱職的養雞大富翁。")
                        break
                
                        
if Ins == "n" :
    print("未購買保險喔 !")
    m = 1000
    print("-")
    while m < 3000 :
        print("錢包 :",m,"元")
        print("飼料 :",eF,"份 ，水 :",eW,"份")
        print("功能 : (1)餵食  (2)喝水  (3)進行才藝表演  (4)購買飼料(一包25元)  (5)購買水(一瓶25元)  (6)購買保險 500 元")
        f = int(input("請選擇功能 :"))
        if f == 1 : 
            print("--")
            if eF > 0:
                addW = random.randint(80,100)
                w += addW
                water -= 0.5
                a += 1
                eF -= 1
                C = chicken(name,a,w)
                print("餵食成功 !")
                print("-")
                C.toPrint()
            else :
                print("飼料不足!請去購買!")
                print("-")
                C.toPrint()                
        if f == 2 :
            print("--")
            if eW > 0:
                addW = random.randint(40,50)
                w += addW
                water += 1
                a += 1
                eW -= 1
                C = chicken(name,a,w)
                print("餵水成功 !")
                print("-")
                C.toPrint()
            else :
                print("水不足!請去購買!")
                print("-")
                C.toPrint()
        if f == 3 :
            print("--")
            if a >= 10 :
                show = random.randint(1,4)
                addW = random.randint(30,50)
                w -= addW
                water -= 0.5
                a += 1
                C = chicken(name,a,w)
                if show == 1 :
                    m += 100
                    print("今天表演狀況較差，沒賺到太多錢，真可惜。但還是恭喜賺進 100 元。")
                if show == 2 :
                    m += 200
                    print("今天表現不錯喔 ! 雞看起來真可愛。賺進 200 元。")
                if show == 3 :
                    m += 200
                    print("今天表現不錯喔 ! 雞看起來真可愛。賺進 200 元。")
                if show == 4 :
                    m += 300
                    print("哇 ! 今天的表演太精采了吧 ! marvelous ! 恭喜賺到 300 元 !")
                print("-")
                C.toPrint()
        if f == 4 : 
            print("--")
            mF = int(input("請問需要購買幾包飼料?"))    
            eF = eF + mF
            m = m - mF*25
        if f == 5 : 
            print("--")
            mW = int(input("請問需要購買幾瓶水?"))    
            eW = eW + mW
            m = m - mW*25
        if f == 6 :
            m -= 500
            print("--")
            print("保險購買成功 !")
            print("-")
            while m < 3000 :
                print("錢包 :",m,"元")
                print("飼料 :",eF,"份 ，水 :",eW,"份")
                print("功能 : (1)餵食  (2)喝水  (3)進行才藝表演  (4)購買飼料(一包25元)  (5)購買水(一瓶25元)")
                f = int(input("請選擇功能 :"))
                if f == 1 : 
                    print("--")
                    if eF > 0:
                        addW = random.randint(80,100)
                        w += addW
                        water -= 0.5
                        a += 1
                        eF -= 1
                        C = chicken(name,a,w)
                        print("餵食成功 !")
                        print("-")
                        C.toPrint()
                    else :
                        print("飼料不足!請去購買!")
                        print("-")
                        C.toPrint()                
                if f == 2 :
                    print("--")
                    if eW > 0:
                        addW = random.randint(40,50)
                        w += addW
                        water += 1
                        a += 1
                        eW -= 1
                        C = chicken(name,a,w)
                        print("餵水成功 !")
                        print("-")
                        C.toPrint()
                    else :
                        print("水不足!請去購買!")
                        print("-")
                        C.toPrint()
                if f == 3 :
                    print("--")
                    if a >= 10 :
                        show = random.randint(1,4)
                        addW = random.randint(30,50)
                        w -= addW
                        water -= 0.5
                        a += 1
                        C = chicken(name,a,w)
                        if show == 1 :
                            m += 100
                            print("今天表演狀況較差，沒賺到太多錢，真可惜。但還是恭喜賺進 50 元。")
                        if show == 2 :
                            m += 200
                            print("今天表現不錯喔 ! 雞看起來真可愛。賺進 100 元。")
                        if show == 3 :
                            m += 200
                            print("今天表現不錯喔 ! 雞看起來真可愛。賺進 100 元。")
                        if show == 4 :
                            m += 300
                            print("哇 ! 今天的表演太精采了吧 ! marvelous ! 恭喜賺到 200 元 !")
                        print("-")
                        C.toPrint()
                    else:
                        print("請勿壓榨童雞!")
                if f == 4 : 
                    print("--")
                    mF = int(input("請問需要購買幾包飼料?"))    
                    eF = eF + mF
                    m = m - mF*25
                if f == 5 : 
                    print("--")
                    mW = int(input("請問需要購買幾瓶水?"))    
                    eW = eW + mW
                    m = m - mW*25
                if water <= 1 :
                    print("---")
                    print("你的電子雞因缺水而死亡了，QQ")
                    print("---")
                    ans = int(input("請問保險要(1)換雞復活還是(2)換現金 750 元 (請輸入1或2)(需再花費 250 元) :"))
                    m -= 250
                    if ans == 1 :
                        water += 4
                        print("-")
                        print("恭喜你的雞復活了 ! 請小心不要讓牠再死了喔 !")
                        print("--")
                        C.toPrint()
                    if ans == 2 :
                        m += 750
                        print("-")
                        print("恭喜你換得 750 元 ~")
                        print("--")
                        if m >= 3000 :                                
                            break
                        else :
                            print("-")
                            print("太可惜了，你還不是位稱職的養雞大富翁。")
                            break
                if a >= 20 :
                    if w <= 800 :
                        print("---")
                        print("你的雞太瘦了，工作太累沒進食，現在餓死了。")
                        print("---")
                        ans1 = int(input("請問保險要(1)換雞復活還是(2)換現金 750 元(請輸入1或2)(需再花費 250 元) :"))
                        m -= 250
                        if ans1 == 1 :
                            w = w + 250
                            print("-")
                            print("恭喜你的雞復活了 ! 請小心不要讓牠再死了喔 !")
                            print("--")
                            C = chicken(name,a,w)
                            C.toPrint()
                        if ans1 == 2 :
                            m += 750
                            print("-")
                            print("恭喜你換得 750 元 ~")
                            print("--")
                            if m >= 3000 :                                    
                                break
                            else :
                                print("-")
                                print("太可惜了，你還不是位稱職的養雞大富翁。")
                                break
        if water <= 1 :
            print("---")
            print("你的電子雞因缺水而死亡了，QQ")
            print("太可惜了，你還不是位稱職的養雞大富翁。")
            break
        if a >= 20 :
            if w <= 800 :
                print("---")
                print("你的雞太瘦了，工作太累沒進食，現在餓死了。")
                print("太可惜了，你還不是位稱職的養雞大富翁。")
                break        
print("錢包 :",m,"元")
if m >= 3000 :
    print("恭喜你 ! 你是一位真正的大富翁 ! ")
print("-------------------遊戲結束-------------------")



        

        
    
    



