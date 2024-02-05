def saludo(name, nikname):
    print("Bienvenid@ " + name + ", su usuario en GitHub es " + nikname)

name = input("Ingrese su nombre: ")
nikname = input("Ingrese su nombre de usuario en GitHub: ")
saludo(name, nikname)
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
for mes in meses:
    print(mes.uppercase())
