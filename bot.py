import requests,re,time

kurlarlistesi = {}

def getsingleinfo(link):
    tümdegerler = []
    for tümf in re.findall("<li class=.cell037.>-?[0-9]+,[0-9]+<",requests.get(link).text):
        tümdegerler.append(re.findall("-?[0-9]+,[0-9]+",tümf)[0])
    print("Stochastic : ",tümdegerler[2],tümdegerler[3],tümdegerler[4])
    print("Rsı : ",tümdegerler[5],tümdegerler[6],tümdegerler[7])
    print("CCI : ",tümdegerler[8],tümdegerler[9],tümdegerler[10])
    print("Boilinger : ",tümdegerler[12],tümdegerler[13],tümdegerler[14])

for kur in re.findall("<a href=.\S+ target=._blank.>\S+",requests.get("http://bigpara.hurriyet.com.tr/borsa/canli-borsa/").text):
    kurlarlistesi[re.findall("[A-Z]+",kur)[0]] = "http://bigpara.hurriyet.com.tr/" + kur[9:].split('"')[0] +"teknik-yorum/"

for kur in kurlarlistesi:
    print(kur,":", kurlarlistesi[kur])
    time.sleep(1)
    getsingleinfo(kurlarlistesi[kur])






