# def son_multiple(*sonlar):
#     kopaytma=1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma
# print(son_multiple(1,2,3,4))


def talaba_info(ism,familya,**kwargs):
    kwargs['name']=ism.title()
    kwargs['family']=familya.title()
    return kwargs

talaba1=talaba_info('hoji','jumaboev',date=2000,gender='male')
print(talaba1)

