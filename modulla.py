# import math as mt
import random as rn
# x=int(input('son x\n'))
# y=int(input('son y \n'))
# print(mt.pow(x, y))


# ismlar=['hasan','husan','tom','jenifer','john']
# rn.shuffle(ismlar)
# print(ismlar)


# uzunlik = lambda r,pi:2*pi*r
# pi=3.14
# print(uzunlik(pi,10))

# def daraja(n):
#     return lambda x:x**n
# kvadrat=daraja(2)
# kub=daraja(3)
# print(kvadrat(12))
# print(kub(5))

# from talaba_data_mod import son_multiple as sm
 
# sonlar=list(range(10))
# kopaytmalar= list(map(sm,sonlar))
# print(kopaytmalar)


# from talaba_data_mod import kopaytma as kp
# sonlar=list(range(10))
# son=list(map(kp, sonlar))
# print(son)



# def daraja2(z):
#     return z*z
# sonlar=list(range(5))
# print(list(map(daraja2,sonlar)))

# a=[1,2,3]
# b=[4,5,6]
# a_plus_b=list(map(lambda x,y:x+y, a,b))
# print(a_plus_b)


# # sonlar=list(r.sample(range(1000), 10))
# # print(sonlar)

# def juft(m):
#     return m%2==0

# sonlar=list(r.sample(range(1000), 10))
# # juft_sonlar=list(filter(juft,sonlar))
# # print(juft_sonlar)

# print(list(filter(lambda x:x % 2==0,sonlar)))

# mevalar=['asal','anor','banan','gilos','uzum','qovun','tut']
# harf='a'
# meva_b=list(filter(lambda meva:meva.startswith(harf), mevalar))
# print(meva_b)

# kichik=list(filter(lambda fruit:len(fruit)>=5, mevalar))
# print(kichik)


# import math
# uzunlik=lambda pi,r:2*pi*r
# print(uzunlik(math.pi,10)) 


# def daraja(n):
#     return lambda x:x**n
# kvadrat=daraja(2)
# kub=daraja(3)
# print(kub(30))


# from math import sqrt
# sonlar=list(range(10))
# ildizlar=[]
# for son in sonlar:
#     ildizlar.append(sqrt(son))
    
# print(ildizlar)

# ildiz=list(map(sqrt, sonlar))
# print(ildiz)

# sonlar=list(range(10))
#  def daraja1(x):
#      return x*x

# print(list(map(lambda x:x*x, sonlar)))


# a = [4, 5, 6]
# b = [7, 8, 9]
# print(list(map(lambda x,y:x+y,a,b)))


# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(), ismlar)))
# import random as r
# numbers=list(r.sample(range(100), 10))

# def juft(x):
#     return x%2==0
# juft_sonlar=list(filter(lambda x:x%2==0,numbers))
# print(numbers)
# print(juft_sonlar)


# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
# harf='o'
# mevalar_o = list ( filter ( lambda meva : meva.startswith(harf), mevalar ) ) 
# print(mevalar_o)



class laptop:
    def _init_(self,model,ram,hdd,ssd,gpu):
        self.model=model
        self.ram=ram
        self.hdd=hdd
        self.ssd=ssd
        self.gpu=gpu
        
        
    def info(self):
        inf=f"{self.model}, ram:{self.ram}, hdd:{self.hdd},ssd:{self.ssd}, gpu:{self.gpu}"
        return inf
        
macbook = laptop("mac" ,"8GB" "512GB","256 GB","M1") 
       





































 






























































