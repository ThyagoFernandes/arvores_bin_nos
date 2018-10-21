class tree:
	raiz = None
	def inserirfilho(self,novo_elemento, pai,l):
		if(self.raiz is not None):	
			if(pai.ocupado(l)):
				#print("filho " + novo_elemento.valor+" no pai "+ pai.valor)
				pai.setfilho(novo_elemento,l)
				novo_elemento.setpai(pai)
				#print(novo_elemento.pai)
			else:
				print("ocupado tente remover primeiro\n")
		else:
			print("raiz inserida" + str(novo_elemento.valor))
			self.raiz = novo_elemento

	def remover(self,no):
		if(no is None):
			return 
		while(no.efolha() is False):
			self.remover(no.filhoesquerdo)
			self.remover(no.filhodireito)
		if(no.pai is not None):
			no.pai.removefilho(no)
		del no 
	def busca_em_ordem(self,no, valor,encontrado):
		if(no is None or encontrado is True):
			return None
		self.busca_em_ordem(no.filhoesquerdo,valor,encontrado)
		if(no.valor == valor):
			print("encontrei o no"+ str(no.valor))
			encontrado = True
			return no
		else:
			print("valor "+ str(no.valor))
		self.busca_em_ordem(no.filhodireito,valor,encontrado)
		return None

	def busca_pre_ordem(self,no, valor,encontrado):
		if(no is None or encontrado is True):
			return None
		if(no.valor == valor):
			print("encontrei o no"+ str(no.valor))
			encontrado = True
			return no
		else:
			print("valor"+ str(no.valor))
	
		self.busca_pre_ordem(no.filhoesquerdo,valor,encontrado)
		self.busca_pre_ordem(no.filhodireito,valor,encontrado)
		return None
		
	def busca_pos_ordem(self,no, valor,encontrado):
		if(no is None ):
			return None
		if(encontrado):

		self.busca_pos_ordem(no.filhoesquerdo,valor,encontrado)
		self.busca_pos_ordem(no.filhodireito,valor,encontrado)

		if(no.valor == valor):
			print("encontrei o no"+ str(no.valor))
			encontrado = True
			return no
		else:
			print("valor"+ str(no.valor))
		return None


	def __repr__(self):
		return "Test()"
	def __str__(self):
		return "arvore " + str(self.raiz.valor)


class node:
	valor = None
	pai = None
	filhoesquerdo = None
	filhodireito = None
	def __init__(self,valor):
		self.valor = valor
	
	def __del__(self):
		print("deletado "+ str(self.valor))
	
	def __repr__(self):
		s = "no " + str(self.valor)
		if(self.pai is not None):
			s += " pai "+ str(self.pai.valor)
		else:
			s += " pai  None"
		if(self.filhoesquerdo is not None):
			s += " filho esquerdo "+ str(self.filhoesquerdo.valor)
		else:
			s += " filho esquerdo  None"
		if(self.filhodireito is not None):
			s += " filho direito "+ str(self.filhodireito.valor)
		else:
			s += " filho direitoo  None"

		return s

	def setpai(self,no):
		self.pai = no

	def setfilho(self,no,l):
		if(l == "e"):
			self.filhoesquerdo = no
		if(l == "d"):
			self.filhodireito = no	
	def ocupado(self, l):
		if((l == "e" and self.filhoesquerdo is not None) or (l == "d" and self.filhodireito is not None)):
			return False
		return True
	def removefilho(self,no):
		if(no == self.filhoesquerdo):
			self.filhoesquerdo = None
		else:
			self.filhodireito = None
	
	def efolha(self):
		print(str(self.valor)+" "+str(self.filhoesquerdo is None and self.filhodireito is None ))
		if(self.filhoesquerdo is None and self.filhodireito is None):
			return True
		return False
arv= tree()
'''no = node("D")
no2 = node("A")
no3 = node("E")
no4 = node ("X")
no5 = node ("Q")
arv.inserirfilho(no,no,"e")
arv.inserirfilho(no2,no,"e")
arv.inserirfilho(no3,no,"d")
arv.inserirfilho(no4,no,"e")
arv.inserirfilho(no5,no3,"d")
arv.busca_em_ordem(no,17,False)
print("    ")
arv.busca_pre_ordem(no,17,False)
print("    ")
arv.busca_pos_ordem(no,17,False)
arv.remover(no)
'''

	
