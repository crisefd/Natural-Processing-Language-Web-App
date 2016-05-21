import os

phrase = 'El cielo esta hermoso el dia de hoy'

f = os.popen("echo '{0}' | analyze --fcorf analyze -f myconfig.cfg".format(phrase))
output  = f.read()
print output
