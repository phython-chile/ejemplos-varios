from twill.commands import *

# Comandos
# go, show, find, notfind, echo, code, back, reload, agent, follow

# Va una URL
go('http://falconsolutions.cl/wp-login.php?')

# Muestra a una URL
# show()

# Buscar
# find("body")

# Muestra el formulario
showforms()

fv("1", "user_login", "mfalcon@falconsolutions.cl")
fv("1", "user_pass", "xuba24741")

submit()

show()
