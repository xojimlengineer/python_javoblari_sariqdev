# def toliq_ism_yasa(name,sname):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{name.title()} {sname.title()}"
#     return toliq_ism
# talaba1=toliq_ism_yasa('olim','oyqorli')
# talaba2=toliq_ism_yasa('hakim', 'suyun')
# print(f"{talaba1} va {talaba2}lar kontraktni vaqtida to'lamagan")
# print(f"{talaba1}ning kontrakt summasi davlat tomonidan to'liq to'lab beriladi")!


# def darsga_kelmagan(ism,familya,otasini_ismi=''):
#     """Darsga kelmaganlarni royxatini tuzuvchi funksiya"""
#     if otasini_ismi:
#         darsda_yoq=f"{ism} {familya} {otasini_ismi}"
#     else:
#         darsda_yoq=f"{ism} {familya}"
#     return darsda_yoq.title()
# talaba1=darsga_kelmagan('nozim','abduvohidov')   
# talaba2=darsga_kelmagan('xosila', 'rahimova','nurullaevna')

# print(f"Darsga kelmagan talabalar:{talaba1} {talaba2}")


# def salom_ber():
#     """Bu funksiya salom beruvchi funksiya hisoblanadi"""
#     print("Assalom alaykum")

# salom_ber()
# print(salom_ber.__doc__)

# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tyil)



# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
# toliq_ism('olim','hakimov')


# def yosh_hisobla(name,birth_date):
#     """Yosh hisoblaydigan funksiya"""
#     print(f"{name.title()} {2022-birth_date} yoshda")
# yosh_hisobla('asil', 2000)     
    
# def son_kub(son):
#     """Sonni kvadrati,kubini hisoblaydigan dastur"""
#     print(son**2,son**3)
# enterson=int(input("Sonni kiritng"))
# son_kub(enterson)
# def juft_toq(son):
#     """Sonni juft yoki toqligini aniqlovchi dastur"""
#     if son%2==0:
#         print("juft son")
#     else:
#         print("toq son")
# sonkirit=int(input("Sonni kiriting"))
# juft_toq(sonkirit)

# def max_hisobla(son1,son2):
#     """Maximumni hisoblaymiz"""
#     if son1 != son2 :
#         print(max(son1,son2))
#     else:
#         print("Bu sonlar o'zaro teng")
        
# kirit1=int(input("son1 kirit\n>>"))
# kirit2=int(input("son2 kirit\n>>"))  
# max_hisobla(kirit1, kirit2)      


# def solishtir(son1,son2):
#     """Ikki sonni solishtiruvchi funksiya"""
#     if son1>son2:
#         print(son1)
#     elif son2==son1:
#         print("Bu sonlar o'zaro teng")
#     else:
#         print(son2)

# kirit1=int(input("Son1 ni kiriting"))
# kirit2=int(input("son2 ni kiriting"))
# solishtir(kirit1, kirit2)


# def bolinish_alomatlari(son):
#     for m in range(1,11):
#         if son%m == 0:
#             print(f"{son}  {m}ga bo'linadi")
#         else:
#             print(f"{son} {m}ga bo'linmaydi")
# kiritson=int(input("son\n>>"))
# bolinish_alomatlari(kiritson)


# def toliq_ism_yasa(name,sname):
#     """ismni ekranga chiqaradigan dastur"""
#     toliq_ism=f"{name} {sname}"
#     return toliq_ism.title()
# talaba1=toliq_ism_yasa('hasan', 'husanov')
# talaba2=toliq_ism_yasa('tolqin', 'jabborov')
# print(talaba1)
# print(talaba2)
    

# def ixtiyoriy_funksiya(name,sname,fname=''):
#     """Ixtiyoriy parametr qabul qiladigan"""
#     if fname:
#         toliq_ism=f"{name} {sname} {fname}"
#     else:
#         toliq_ism=f"{name}  {sname}"
#     return toliq_ism.title()
# talaba=ixtiyoriy_funksiya('baxti', 'eshonqulov')
# talaba1=ixtiyoriy_funksiya('samar','badriddinov','xofizovich')
# print(f"Kontrakdan qarzi borlar:{talaba} va   {talaba1}")

# def avto_info(company,model,color,price=None):
#     """Bu funksiya foydalanuvchiga return yordamida qiymat qaytaradi"""
#     avto={'kompaniya':company,
#           'modeli':model,
#           'rangi':color,
#           'narxi':price
#         }
#     return avto
# car1=avto_info('GM', 'malibu', 'qora', 15000)
# car2=avto_info("BMW", "BMW GL 6100", 'green', )
# cars=[car1,car2]
# print("Onlayn bozordagi moshinalar")
# for car in cars:
#     if car['narxi']:
#         narx=car['narxi']
#     else:
#         narx='nomalum'
#     print(f"{car['modeli']}   {car['rangi']} :{car['narxi']}")    


#def oraliq(mini,maxi,pace=''):
#     sonlar=[]
#     while mini<maxi:
#         sonlar.append(mini)
#         if pace:
#             mini+=pace
#         else:
#             mini+=1
        
#     return sonlar
# print(oraliq(12,90,11,)) 
# print(oraliq(1, 10,2))
## qadam_royxati




    
    
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
    
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# for avto in avtolar:
#     print(avto)



# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# print("Saytimiz uchun mashinalar ro'yxatini shakllantiramiz")
# avtolar=[]
# while True:
#     print("Quyidagi ma'lumotlarnimkiriting")
#     kompaniya=input("Kompaniya")
#     model=input("modeli")
#     rangi=input("rangi")
#     korobka=input("korobka")
#     yili=input("yili")
#     narhi=input("narhi")
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     savol=input("Anything else yes\\no")

#     if savol =='no':
#         break
    
# for car in avtolar:
#     print(car)

# def full_info(ism,familya,t_yil,t_joy,tel_raqam,e_manzil):
#     info={
#         'ismi':ism,
#         'familya':familya,
#         't_yil':t_yil,
#         't_joy':t_joy,
#         'tel_raqam':tel_raqam,
#         'e_manzil':e_manzil            
#         }
#     return info

# print("Barcha ma'lumotlarni oladigan dastur")
# data =[]
# while True:
#     print("Ma'lumotlartni kiriting")
#     ism=input("Ismingiz nima?")
#     familya=input("Familyangiz")
#     t_yil=input("Tug'ilgan yilingiz")
#     t_joy=input("Tug'ilgan joyingiz")
#     tel_raqam=input("Telefon raqamingiz")
#     e_manzil=input("elektron manzilingiz")
#     data.append(full_info(ism,familya,t_yil,t_joy,tel_raqam,e_manzil))
#     javob=input("WAnna else yes\\no")
#     if javob == 'no':
#         break
    

# for malumot in data:
#     print(malumot)
    
    
# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")  
    
    
# def katta(x,y,z):
#      maximum = max(x,y)
#      maxi=max(y,maximum)
#      return maxi
# qiymat=katta(1, 3, -2)
# print(qiymat)
  
    
# def aylana(radius,pi=3.14):
#        circle ={
#         'radius':radius,
#         'diametr':2*radius,
#         'perimetr':2*radius*pi,
#         'yuzi':2*pi*(radius**2)
#         }
#        return circle
# ayla=aylana(5)
# print(ayla)
    




# def tub(mini,maxi):
#     tub_sonlar=[]
#     while mini==maxi :
#         if (mini % 2 != 0 and mini ):
#             print(mini)
#             tub_sonlar.append(mini)
#             mini+=1
            
#         else :
#             continue
#         return tub_sonlar
    
# qiymat=tub(1,18)
# print(qiymat)
        
    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










































































































