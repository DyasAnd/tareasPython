String nombre = ""
int edad 
String email = " "

print "ingresa tu nombre"
nombre = input()
print " ingresa tu edad"
edad = input()
print " cual es tu correo electronico"
email = input()


print " mi nombre es "+"\033[1;33m", {nombre}
print "  tengo  "+"\033[;36m",{edad}+"  años  "
print " y se enviara un correo electronico a la siguiente direcion "+"chr(27)+"[1;33m", {email}

