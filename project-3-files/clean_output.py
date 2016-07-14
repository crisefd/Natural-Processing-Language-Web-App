import sys
import os

def clean_output():
	dir_path = os.getcwd()
	# print "=> ", sys.argv
	# Salida etiquetada del CRF
	crf_output_file = open(dir_path + "/crf_outputs/" + sys.argv[1], "r")
	lines = crf_output_file.readlines()
	#Archivo Transformado
	crf_cleaned_file = open(dir_path + "/crf_outputs/" + sys.argv[2], "w")
	for line in lines:
		arrayLine = line.replace("\n","").split("\t")
		txt = ""
		for i in range(len(arrayLine)):
			txt += arrayLine[i]+" "
		txt = txt[:len(txt)-1]+"\n"
		crf_cleaned_file.write(txt)
	crf_cleaned_file.close()
	crf_output_file.close()


if __name__ == "__main__":
    clean_output()
