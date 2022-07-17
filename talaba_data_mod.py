def son_multiple(*sonlar):
    kopaytma=1
    for son in sonlar:
        kopaytma*=son
    return kopaytma


def talaba_info(ism,familya,**kwargs):
    kwargs['name']=ism.title()
    kwargs['family']=familya.title()
    return kwargs

def kopaytma(n):
    kopayt= n*2
    return kopayt
