#Defiano Dhio Bimantara
#Quiz

#no1
##import re
##pola = '[@]+[a-zA-Z]+[0-9]+[_]+'
##Username = input('Masukkan Nama Email: ')
##
##if re.findall(pola, Username):
##    print('PASS')
##else:
##    print('FAILED')

#2
import re
pola = r'\w+@+[\w.-]+'
f = open ("quiz.txt")
s = f.read()
menampilkan = re.findall(pola,s)
print(menampilkan)

#3
##import re
##class PohonBiner(object):
##    def __init__(self, data):
##        self.data = data
##        self.kiri = None
##        self.kanan = None
##A = PohonBiner('A')
##B = PohonBiner('B')
##C = PohonBiner('C')
##D = PohonBiner('D')
##E = PohonBiner('E')
##F = PohonBiner('F')
##G = PohonBiner('G')
##H = PohonBiner('H')
##I = PohonBiner('I')
##
##A.kiri = B; A.kanan = C
##B.kiri = D; B.kanan = E
##C.kiri = F; C.kanan = G
##E.kiri = H
##G.kanan = I
##
##def cetakPohonLuarKiri(data):  
##    if data is not None :       
##        cetakPohonLuarKiri(data.kiri)
##        print(data.data)
##
##def cetakPohonLuarKanan(data):
##    if data.kanan is not None :
##        cetakPohonLuarKanan(data.kanan)
##        print(data.data)
##
##
##def cetakPohonLuar(data):
##    cetakPohonLuarKiri(data)
##    cetakPohonLuarKanan(data)
##
##cetakPohonLuar(A)

