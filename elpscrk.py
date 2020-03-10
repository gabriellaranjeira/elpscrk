#!/usr/bin/env python

import argparse
import sys
import os

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OK = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
wordInicio = []
outputFile = ""
words = 0
total = 0

def printar():
	print OKBLUE+"""
 _______  ___      _______  _______  _______  ______    ___   _ 
|       ||   |    |       ||       ||       ||    _ |  |   | | |
|    ___||   |    |    _  ||  _____||       ||   | ||  |   |_| |
|   |___ |   |    |   |_| || |_____ |       ||   |_||_ |      _|
|    ___||   |___ |    ___||_____  ||      _||    __  ||     |_ 
|   |___ |       ||   |     _____| ||     |_ |   |  | ||    _  |
|_______||_______||___|    |_______||_______||___|  |_||___| |_|

                    ________________________
		    |                      |
                    |  CODED BY: BUNNYDARK |
                    |     VERSION: 0.1     |
                    |______________________|
	"""+END

def fim():
	global OK
	global words
	global BOLD
	print OK+BOLD+"[+] Wordlist gerada com sucesso!\nPalavras geradas: {}".format(str(words))

def porcentagem(percent):
	global WARNING
	por = WARNING+"[!] {}%\n".format(str(percent))
	print por	

def geraOutput(wlFinal):
	global outputFile
	output = open(outputFile, "w")
	output.write(wlFinal)
	output.close()
	fim()

def finaliza(wl):
	finalWord = ""
	for lista in wl:
		for word in lista:
			finalWord = finalWord + word + "\n"
	geraOutput(finalWord)

def gerarWord1():
	global wordInicio
	global words
	global WARNING
	newWord = []
	for x in wordInicio:
		for y in wordInicio:
			newWord.append(x+y)
			newWord.append(y+x)
			words = words + 2
	porcentagem(25)
	return newWord

def gerarWord2():
	global wordInicio
	global words
	global WARNING
	newWord = []
	for x in wordInicio:
		for y in wordInicio:
			newWord.append(x+"_"+y)
			newWord.append(y+"_"+x)
			words = words + 2

	porcentagem(50)
	return newWord

def gerarWord3():
	global words
	global wordInicio
	newWord = []
	for x in wordInicio:
		newWord.append("123"+x)
		newWord.append(x+"123")
		words = words + 2
	
	porcentagem(75)
	return newWord

def gerarWord4():
	global words
	global wordInicio
	newWord = []
	for x in wordInicio:
		for y in wordInicio:
			for z in wordInicio:
				newWord.append(x+y+z)
				newWord.append(x+z+y)
				newWord.append(y+z+x)
				newWord.append(y+x+z)
				newWord.append(z+y+x)
				newWord.append(z+x+y)
				newWord.append(x+"_"+y+"_"+z)
				newWord.append(x+"_"+z+"_"+y)
				newWord.append(y+"_"+z+"_"+x)
				newWord.append(y+"_"+x+"_"+z)
				newWord.append(z+"_"+y+"_"+x)
				newWord.append(z+"_"+x+"_"+y)
				words = words + 12
	porcentagem(100)
	return newWord

def wordlist():
	wordFinal = []
	wordFinal.append(gerarWord1())	
	wordFinal.append(gerarWord2())
	wordFinal.append(gerarWord3())
	wordFinal.append(gerarWord4())
	finaliza(wordFinal)

def main():
	global wordInicio
	global outputFile
	global FAIL
	global BOLD
	printar()
	parser = argparse.ArgumentParser(description="FERRAMENTA HACKING PARA CRIACAO DE WORDLISTS")
	parser.add_argument('-list', action = 'store', dest = 'lst', help = 'Arquivo ou conjunto de palavras para criar a worldlist')
	parser.add_argument('-output', action = 'store', dest = 'output', help = 'Arquivo final onde serao colocadas a wordlist')
	arg = parser.parse_args()
	if(arg.lst == None):
		print FAIL+BOLD+"\n\n[X] Erro ao colocar parametros: use elpscrk -list 'LISTA' -output OUTPUT_FILE"
		sys.exit(0)
	elif(arg.output == None):
		print FAIL+BOLD+"\n\n[X] Erro ao colocar parametros: use elpscrk -list 'LISTA' -output OUTPUT_FILE"
		sys.exit(0)
	else:
		if(os.path.isfile(arg.output)):
			print FAIL+BOLD+"[X] Arquivo de output ja existente!"
			sys.exit(0)
		else:
			outputFile = arg.output
			if(os.path.isfile(arg.lst)):
				wordInicio = open(arg.lst, "r").read().split("\n")
			else:
				wordInicio = arg.lst.split(",")
			wordlist()
		

main()