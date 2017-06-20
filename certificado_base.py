# -*- coding: utf-8 -*-
import commands


subj_cuit = "1212121"
subj_cn = "121212"
subj_o = "121212"

def obtener_certificado():
    print "Se Obtiene el certificado"
    res = commands.getstatusoutput('openssl smime --help')
    if res[0] == 0:
        print res[1]
    else:
        print "Error: " + str(res[0])
        print "Descripción: " + res[1]

obtener_certificado()