import creopyson
import subprocess
import time
import pprint

pathStart="C:\Program Files\PTC\Creo 9.0.3.0\Parametric\\bin\parametric.bat"

c = creopyson.Client()

c.connect()

c.creo_set_creo_version(9)

if not c.is_creo_running():
    subprocess.Popen(pathStart)
    while not c.is_creo_running():
        time.sleep(5)
        print("Jeszcze nie gotowe")

print("Gotowe")

enter=input("Naciśnij Enter aby kontynuować")

c.creo_cd("C:\\Users\\CAD\Desktop\\Krzysztof Malinowski\\Lab4")

c.file_open("zlozenie1.asm")


print("Parametry")

for x in range(len(c.parameter_list())):
    print(c.parameter_list()[x])
    if type(c.parameter_list()[x]['value']) is float:
        c.parameter_set( c.parameter_list()[x]['name'], value = 300)

print("Po zmianie")

for x in range(len(c.parameter_list())):
    print(c.parameter_list()[x])

c.file_get_transform(csys="ASM_DEF_CSYS")

c.file_assemble("model4.prt",package_assembly="true")

c.file_get_transform(csys="ACS0")

c.file_assemble("model5.prt",package_assembly="true")

print("Współrzędne układu ASC0: ",c.file_get_transform(csys="ACS0"))

c.file_rename("Ma_Kr.asm", onlysession="true")

c.file_save()

c.drawing_create("a3_drawing", display="true", activate="true", new_window="true")