import os, re, struct, string
q = input('需要操作的文件:')
aa = [0,0,0,0]
ab = [0,0,0,0]
ac = [0,0,0,0]
ad = [0,0,0,0]
ka = [0,0,0,0]
kb = [0,0,0,0]
kc = [0,0,0,0]
kd = [0,0,0,0]
b1 = [0,0,0,0]
b2 = [0,0,0,0]
b3 = [0,0,0,0]
b4 = [0,0,0,0]
I = [0,0,0,0]
S1 = {
	'0':'52','1':'09','2':'6A','3':'D5','4':'30','5':'36','6':'A5','7':'38','8':'BF','9':'40','a':'A3','b':'9E','c':'81','d':'F3','e':'D7','f':'FB',
	'10':'7C','11':'E3','12':'39','13':'82','14':'9B','15':'2F','16':'FF','17':'87','18':'34','19':'8E','1a':'43','1b':'44','1c':'C4','1d':'DE','1e':'E9','1f':'CB',
	'20':'54','21':'7B','22':'94','23':'32','24':'A6','25':'C2','26':'23','27':'3D','28':'EE','29':'4C','2a':'95','2b':'0B','2c':'42','2d':'FA','2e':'C3','2f':'4E',
	'30':'08','31':'2E','32':'A1','33':'66','34':'28','35':'D9','36':'24','37':'B2','38':'76','39':'5B','3a':'A2','3b':'49','3c':'6D','3d':'8B','3e':'D1','3f':'25',
	'40':'72','41':'F8','42':'F6','43':'64','44':'86','45':'68','46':'98','47':'16','48':'D4','49':'A4','4a':'5C','4b':'CC','4c':'5D','4d':'65','4e':'B6','4f':'92',
	'50':'6C','51':'70','52':'48','53':'50','54':'FD','55':'ED','56':'B9','57':'DA','58':'5E','59':'15','5a':'46','5b':'57','5c':'A7','5d':'8D','5e':'9D','5f':'84',
	'60':'90','61':'D8','62':'AB','63':'00','64':'8C','65':'BC','66':'D3','67':'0A','68':'F7','69':'E4','6a':'58','6b':'05','6c':'B8','6d':'B3','6e':'45','6f':'06',
	'70':'D0','71':'2C','72':'1E','73':'8F','74':'CA','75':'3F','76':'0F','77':'02','78':'C1','79':'AF','7a':'BD','7b':'03','7c':'01','7d':'13','7e':'8A','7f':'6B',
	'80':'3A','81':'91','82':'11','83':'41','84':'4F','85':'67','86':'DC','87':'EA','88':'97','89':'F2','8a':'CF','8b':'CE','8c':'F0','8d':'B4','8e':'E6','8f':'73',
	'90':'96','91':'AC','92':'74','93':'22','94':'E7','95':'AD','96':'35','97':'85','98':'E2','99':'F9','9a':'37','9b':'E8','9c':'1C','9d':'75','9e':'DF','9f':'6E',
	'a0':'47','a1':'F1','a2':'1A','a3':'71','a4':'1D','a5':'29','a6':'C5','a7':'89','a8':'6F','a9':'B7','aa':'62','ab':'0E','ac':'AA','ad':'18','ae':'BE','af':'1B',
	'b0':'FC','b1':'56','b2':'3E','b3':'4B','b4':'C6','b5':'D2','b6':'79','b7':'20','b8':'9A','b9':'DB','ba':'C0','bb':'FE','bc':'78','bd':'CD','be':'5A','bf':'F4',
	'c0':'1F','c1':'DD','c2':'A8','c3':'33','c4':'88','c5':'07','c6':'C7','c7':'31','c8':'B1','c9':'12','ca':'10','cb':'59','cc':'27','cd':'80','ce':'EC','cf':'5F',
	'd0':'60','d1':'51','d2':'7F','d3':'A9','d4':'19','d5':'B5','d6':'4A','d7':'0D','d8':'2D','d9':'E5','da':'7A','db':'9F','dc':'93','dd':'C9','de':'9C','df':'EF',
	'e0':'A0','e1':'E0','e2':'3B','e3':'4D','e4':'AE','e5':'2A','e6':'F5','e7':'B0','e8':'C8','e9':'EB','ea':'BB','eb':'3C','ec':'83','ed':'53','ee':'99','ef':'61',
	'f0':'17','f1':'2B','f2':'04','f3':'7E','f4':'BA','f5':'77','f6':'D6','f7':'26','f8':'E1','f9':'69','fa':'14','fb':'63','fc':'55','fd':'21','fe':'0C','ff':'7D'
}
with open(q,'rb') as f:
	with open('KEY.txt','rb') as K:
		with open(q[:len(q)-8]+'R','wb') as E:
			fr = f.read()
			f.seek(0,0)
			for k in range((len(fr)//16)):
				K.seek(0,0)
				for i in range(16):
					b = ord(struct.pack('c',f.read(1)))
					if i <= 3:
						aa[i] = b 
					elif 3 < i <= 7:
						ab[i-4] = b
					elif 7 < i <=11:
						ac[i - 8] = b 
					elif i > 11:
						ad[i-12] = b
				for j in range(16):
					b = ord(K.read(1))
					if j <= 3:
						ka[j] = b
					elif 3 < j <= 7:
						kb[j-4] = b 
					elif 7 < j <=11:
						kc[j - 8] = b
					elif j > 11:
						kd[j-12] = b
				b1[0] = aa[0] ^ int('02',16)
				b2[0] = ab[0] ^ int('03',16)
				b3[0] = ac[0] ^ int('01',16)
				b4[0] = ad[0] ^ int('01',16)	
									 
				b1[1] = aa[1] ^ int('01',16)
				b2[1] = ab[1] ^ int('02',16)
				b3[1] = ac[1] ^ int('03',16)
				b4[1] = ad[1] ^ int('01',16)	
									 
				b1[2] = aa[2] ^ int('01',16)
				b2[2] = ab[2] ^ int('01',16)
				b3[2] = ac[2] ^ int('02',16)
				b4[2] = ad[2] ^ int('03',16)     
									 
				b1[3] = aa[3] ^ int('03',16)
				b2[3] = ab[3] ^ int('01',16)
				b3[3] = ac[3] ^ int('01',16)
				b4[3] = ad[3] ^ int('02',16)
				
				I = b2[0]
				J = b2[1]
				M = b2[2]
				L = b2[3]
				
				b2[0] = L
				b2[1] = I
				b2[2] = J
				b2[3] = M
				
				I = b3[0]
				J = b3[1]
				M = b3[2]
				L = b3[3]
				
				b3[0] = M
				b3[1] = L
				b3[2] = I
				b3[3] = J
				
				I = b4[0]
				J = b4[1]
				M = b4[2]
				L = b4[3]
				
				b4[0] = J
				b4[1] = M
				b4[2] = L
				b4[3] = I	
				
				for i in range(16):
					if i <= 3:
						aa[i] = b1[i]^ka[i]
					elif 3 < i <= 7:
						ab[i-4] = b2[i-4]^kb[i-4]
					elif 7 < i <=11:
						ac[i-8] = b3[i-8]^kc[i-8]
					elif i > 11:
						ad[i-12] = b4[i-12]^kd[i-12]
				for i in range(4):
					E.write(struct.pack('B',aa[i]))
				for i in range(4):
					E.write(struct.pack('B',ab[i]))
				for i in range(4):
					E.write(struct.pack('B',ac[i]))
				for i in range(4):
					E.write(struct.pack('B',ad[i]))	
with open(q[:len(q)-8]+'R','rb') as E:
	fr = E.read()
	fr = str.rstrip(str(fr))
with open(q[len(q)-8:]+'R','w') as E:
	E.write(fr)
with open(q[len(q)-8:]+'R','r') as f:
	with open(q+'\'','w') as fm:
		k = -1
		a = fm.readlines()
		for i in a:
			k = k + 1
			if k/7 - k//7 == 0:
				j = i; b = 1
			elif b == 1:
				f.write(i+j); b = 0
			else:
				f.write(i)
		if b == 1:
			f.write(j); b = 0
with open(q+'\'','r') as fm:
	with open(q[len(q)-8:],'w') as f:
		a = f.readlines()
		j = ''; l = ''; k = -1; b = 0
		for i in a:
			k = k + 1
			if k/2 - k//2 == 0:
				j = i; b = 1
			else:
				fm.write(i+j); b = 0
		if b == 1:
			fm.write(j); b = 0
