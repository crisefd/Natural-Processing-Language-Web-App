def transformarSalida():
	#Salida etiquetada del CRF
	archivo=open("input-p", "r")
	lineas=archivo.readlines()
	#Archivo Transformado
	salida=open("salida.txt", "w")
	for linea in lineas:
		arrayLinea=linea.replace("\n","").split("\t")
		cadena=""
		for i in range(len(arrayLinea)):
			cadena+=arrayLinea[i]+" "
		
		cadena=cadena[:len(cadena)-1]+"\n"
		salida.write(cadena)
	salida.close()
	archivo.close()
transformarSalida()
