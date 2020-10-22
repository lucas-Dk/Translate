# Criando um tradutor de textos
# Necessário a biblioteca translate
# Necessário a biblioteca tqdm


# Importações
try:
	import os
	import sys
	import time
	from translate import Translator
	from tqdm import tqdm
except:
	print("\033[1;31mERROR: Você não tem os requisitos :( !")
	print("Por favor, leia o \033[4mREADME.md\033[m \033[1;31maqui do arquivo")
	print("E tente novamente!\033[m")
else:
	print("\033[1;31mCarregando tradutor...\033[m")
	for loading in tqdm(range(1, 100 + 1)):
		time.sleep(0.1)
	print("\033[1;32mTradutor carregado e pronto para uso!\033[m")
	time.sleep(1)
	os.system("clear")

	while True:
		print("""\033[94m
 _                              _          _         
| |_   _ _   __ _   _ _    ___ | |  __ _  | |_   ___ 
|  _| | '_| / _` | | ' \  (_-< | | / _` | |  _| / -_)
 \__| |_|   \__,_| |_||_| /__/ |_| \__,_|  \__| \___|
                      
                      V 1.0
\033[m\033[1m
OBS: Nome da linguagem precisa estar em inglês!

exemplo:

traduzir de \033[33mPortuguese\033[m \033[1mpara\033[m \033[1;36mEnglish\033[m
\033[m""")
		print("==" * 26 + '\n')
		try:
			frase = input("Digite sua frase: ").lower()
			de = str(input("Traduzir de: ")).capitalize()
			para = str(input("Para: ")).capitalize()
		except KeyboardInterrupt:
			print("\nSaindo...")
			time.sleep(1)
			sys.exit()
		else:
			traduzir = Translator(from_lang=de,to_lang=para)
			traducao = traduzir.translate(frase)
			print("Traduzindo...")
			time.sleep(0.6)
			print("\nSua frase: {}".format(frase))
			print("Tradução: {}".format(traducao))
			print()
			again = str(input("Traduzir mais alguma coisa Y/N: ")).upper()
			while again.strip() not in "Y" and again.strip() not in "N":
				print("ERROR: Digite uma opção válida para prosseguir...")
				again = str(input("Traduzir mais alguma coisa Y/N: ")).upper()
			if again == "S":
				pass
			elif again == "N":
				print("Saindo...")
				time.sleep(1)
				sys.exit()
finally:
	print() # Espaço apenas1

# Fim do script
