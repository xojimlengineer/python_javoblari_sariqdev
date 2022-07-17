# def qiymat_uzat(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=int(input(f"Talaba {ism.title()}ning bahosini kiriting"))
#         baholar[ism]=baho
#     return baholar
    
# talabalar=['nodir','asad','akbar','sunnat','abdumalik']
# baholar=qiymat_uzat(talabalar[:])
# print(baholar)
# print(talabalar)
    

# def katta_harf(matnlar):
#     matn=matnlar[:]
#     for i in range(len(matnlar)):
#         matn[i]=matn[i].title()
#     return matn
# ismlar=['anvar','sodiq','qodir','avaz']
# nomlar=katta_harf(ismlar)
# print(nomlar)

# def avto_info(company,model,color,price):
#     avtolar={
#         'kompaniya':company,
#         'modeli':model,
#         'rangi':color,
#         'narxi':price
#         }
#     return avtolar
# avtolar=[]
# while True:
#     print("Quyidagi ma'lumotlarni kiriting!!")
#     company=input("Kompaniya nomi>>")
#     model=input("Qaysi model>>")
#     color=input("Rangi qanaqa>>")
#     price=input("Narxi qancha>>")
#     avtolar.append(avto_info(company,model,color,price))
#     savol=input("Wanna something else? yes\\no")
#     if savol == 'no':
#        break

# for avto in avtolar:
    
#     print(avto)
    
  
# def oraliq(mini ,maxi):
#     sonlar=[]
#     while mini < maxi :
#         sonlar.append(mini)
#         mini+=1
        
#     return sonlar
    
# number = oraliq(1, 10)
# print(number)    
    
 
## *args    
# def unlimited(*sonlar):
#     return sum(sonlar)
#     # summa=0
#     # for son in sonlar:
#     #     summa+=son
#     # return summa

# num=unlimited(1,13,4,5,5,6)
# num2=unlimited(8,7,6,5,4,3,2,1)
# print(num)
# print(num2)    
    
    
def avto_data(kompaniya,model,**malumotlar):
    malumotlar['company']=kompaniya
    malumotlar['model']=model
    return malumotlar



data1=avto_data('BMW','BMW 3500')
data2=avto_data("Lamborghini", 'Huracan super speed', color='black',price=10000000)
print(data1)
print(data2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    