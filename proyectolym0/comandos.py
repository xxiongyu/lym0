archivo = input('ingrese el arhivo: ')
texto = open(archivo,"r",encoding="utf-8") 
text = texto.read()
# text = "NEW VAR rotate = 3 NEW MACRO foo ( c , p ) { drop ( c ) ; letgo ( p ) ; walk ( rotat e ) ; }"
text= text.lower()
text= text.split()
lista_word = text
print(lista_word)
size = len(lista_word)
dicc_publico = {}
dicc_privado = {}  
verificacion = 0 
list_rango = str(list(range(1,100))) 
posiciones = ["x","y","v"]
list_posicion = ['right','left','front','back'] 
list_cardinales =['north','south','west','east'] 
list_commansTurn = ['left','right',' back']  
lista_comandos = ['jump','walk','turntothe','turntomy','drop','grab','letgo','nop','pick','pop','moves','safeexe']
lista_condi = ['isfacing','isblocked','zero','not']
lista_estruc=['if','do','repeat']




def RevisionCompletitud(list, index, qc, corchete):
    comprobar = list[index]
    if qc < -1 or corchete < -1:
        return -1000

    else:
        if comprobar== '(':
            return RevisionCompletitud(list, index+1, qc+1, corchete)
        if comprobar == ')':
            return RevisionCompletitud(list, index+1, qc-1, corchete)
        if comprobar != '(' and comprobar != ')' and comprobar != '{' and comprobar != '}':
            return RevisionCompletitud(list, index+1, qc, corchete)

        if comprobar== '{':
            return RevisionCompletitud(list, index+1, qc, corchete+1)
        if comprobar == '}' and corchete>1:
            return RevisionCompletitud(list, index+1, qc, corchete-1)
        

        if comprobar == '}' and corchete==1:
            return index
        


def RevisionDefinicion (lista,a)->int  :
        global verificacion    
        if lista[a] == 'new':
            tipo = lista[a+1]
            if tipo == 'var':
                b = a+2
                c = a+3
                d = a+4
                variable = lista_word[b]
                valor = lista_word[d]
                igual = lista_word[c]
                if igual == '=' and esEntero(valor):
                    dicc_publico[variable] = valor
                    return a+5
                else:
                    return a+size

            if tipo=="macro":
                b = a+2
                c = a+3
                listaParam = []
                variable = lista[b]
                indensado = lista.index(')', c)
                for j in range(c+1,indensado):
                    if lista_word[j] != ',':
                        listaParam.append(lista_word[j])
                dicc_privado[variable]=listaParam
                llavedefuncion = indensado+1
                if lista[llavedefuncion] == '{':
                    coordenada_complititud = RevisionCompletitud(lista_word, llavedefuncion+1, 0, 1)
                    if coordenada_complititud == -1000:
                        verificacion+1    
                        return a+size
                    else:
                           for vericidad in range(llavedefuncion, coordenada_complititud):
                                    if lista_word[vericidad] :
                                        RevisionComando(lista_word,vericidad)
                                    if lista_word[aa] in lista_condi:
                                        RevisionCondicion(lista_word,vericidad)
                                    if lista_word[aa] in lista_estruc:
                                        RevisionEstructuraControl(lista_word,vericidad)
                                    if lista_word[aa] == 'new':
                                        RevisionDefinicion(lista_word,vericidad)

                           return a+coordenada_complititud
                    

                             
def esEntero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def RevisionComando(lista,a)->int:
        global verificacion

        if lista[a] == 'jump': 
                    b = a+1 
                    indesado = lista.index(')',b)  
                    for aa in range(b+1,indesado): 
                        if (lista[aa] in dicc_publico):  
                            verificacion+0
                            return aa+3
                        else:
                            verificacion+1
                            return a+size
        if lista[a] == 'moves': 
                    b = a+1 
                    indesado = lista.index(')',b) 
                    add=b+1
                    for aa in range(b+1,indesado): 
                        if (lista[aa] in list_rango or lista[aa] in posiciones) : 
                            verificacion+0
                            add+=(aa+1)
                        elif (lista[aa] in list_rango or lista[aa] in posiciones) and lista[aa+1] == ',' and lista[aa+2] in list_posicion: 
                            verificacion+0
                            add+=(aa+3)
                        elif (lista[aa] in list_rango or lista[aa] in posiciones) and lista[aa+1] == ',' and lista[aa+2] in list_cardinales: 
                            verificacion+0
                            add+=(aa+3)
                        else:
                            verificacion+1
                            return a+size
                    return add 
           
        if lista[a] == 'turntomy': 
                        b = a+1 
                        indesado = lista.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista[aa] in posiciones): 
                                verificacion+0
                                return aa+1
                            else:
                                verificacion+1
                                return a+size
        if lista[a] == 'turntothe': 
                        b = a+1 
                        indesado = lista.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista[aa] in list_cardinales): 
                                verificacion+0
                                return aa+1
                            else:
                                verificacion+1
                                return a+size                    
        if lista[a] == 'pick': 
                        b = a+1 
                        indesado = lista.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista[aa] in dicc_publico) : 
                                verificacion+0
                                return aa+1
                            else:
                                verificacion+1
                                return a+size

            
        if lista[a] == 'walk':
                        b = a+1
                        indensado=lista.index(')',b)
                        for j in range(b+1,indensado):
                                if (lista[j] in dicc_publico):
                                      verificacion+0
                                      return j+1
                                else:   
                                      verificacion+1
                                      return a+size

        if lista[a] == 'drop':
                        b = a+1
                        indensado=lista.index(')',b)
                        for j in range(b+1,indensado):
                                if (lista[j] in dicc_publico):
                                      verificacion+0
                                      return j+1
                                else:   
                                      verificacion+1 
                                      return a+size

        if lista[a] == 'grab':
                        b = a+1
                        indensado=lista.index(')',b)
                        for j in range(b+1,indensado):
                                if (lista[j] in dicc_publico):
                                      verificacion+0
                                      return j+1
                                else:   
                                      verificacion+1   
                                      return a+size

        if lista[a] == 'letgo':
                        b = a+1
                        indensado=lista.index(')',b)
                        for j in range(b+1,indensado):
                                if (lista[j] in dicc_publico):
                                      verificacion+0
                                      return j+1
                                else:   
                                      verificacion+1
                                      return a+size
                                    
        if lista[a] == 'pop':
                        b = a+1
                        indensado=lista.index(')',b)
                        for j in range(b+1,indensado):
                                if (lista[j] in dicc_publico):
                                      verificacion+0
                                      return j+1
                                else:   
                                      verificacion+1 
                                      return a+size

        if lista[a] == 'nop':
                        b = a+1
                        if lista[b]!= ')' or lista[b]!= '(' or not(lista[b] in dicc_publico):
                                verificacion+0
                                return b+1
                        else:
                                verificacion+1
                                return a+size

        if lista[a] == 'safeexe':
                        b = a+1
                        indensado=lista.index(')',b)
                        for j in range(b+1,indensado):
                                if (lista_word[j] in lista_comandos):
                                      RevisionComando(lista[j:],j)
                                else:   
                                      verificacion+1 
                                      return a+size
                                
        if lista[a] in dicc_privado:
               return a+1+(dicc_privado[lista[a]].size())                        
        else:
               return a

def RevisionCondicion(lista,a)->int:
        global verificacion
        if lista[a] == 'isfacing?': 
                        b = a+1 
                        indensado = lista[a].index(')',b) 
                        for aa in range(b+1,indensado): 
                            if lista[aa] in list_cardinales: 
                                verificacion+0
                                return aa+1
                            else:
                                verificacion+1
                                return a+size

        if lista[a] == 'isblocked?':
                        b = a+1   
                        indensado= lista.index(')',b) 
                        for j in range(b+1,indensado):
                            if lista[j] in posiciones:
                                    verificacion+0
                                    return j+1
                            else:
                                    verificacion+1
                                    return a+size

        if lista[a] == 'zero?':
                        b = a+1
                        indensado=lista.index(')',b)
                        for j in range(b+1,indensado):
                                if lista[j] in dicc_privado:
                                        verificacion+0
                                        return j+1
                                else:
                                        verificacion+1   
                                        return a+size

        if  lista[a] == 'not': 
                        b = a+1 
                        condicion = lista[b] 
                        if condicion == 'isfacing?' or condicion == 'isblocked?' or condicion == 'zero?': 
                            verificacion+0
                            return b+1
                        else:
                            verificacion+1   
                            return a+size
        else:
               return a
        
def RevisionEstructuraControl (lista,a)->int:
        global verificacion
        if lista[a] == 'if':
                b = a+1
                condicion= RevisionCondicion(lista[b:],b)
                if not (condicion>size) and (condicion!=b) and lista[condicion]=="then":
                     #aplicar revision completitud
                    if_index = lista_word.index('{', a)
                    coordenadaCompletitud = RevisionCompletitud(lista_word, if_index+1,0,1)
                    then=RevisionComando(lista[condicion:],condicion)
                    if not (then>size) and (condicion!=b) and lista[then]=="else":
                        RevisionComando(lista[then],then)
                    
                    elif coordenadaCompletitud == -1000:
                           verificacion+1
                           return a+size
                    
                    elif coordenadaCompletitud != -1000:
                           for vericidad in range(if_index, coordenadaCompletitud):
                                    if lista_word[vericidad] :
                                        RevisionComando(lista_word,vericidad)
                                    if lista_word[aa] in lista_condi:
                                        RevisionCondicion(lista_word,vericidad)
                                    if lista_word[aa] in lista_estruc:
                                        RevisionEstructuraControl(lista_word,vericidad)
                                    if lista_word[aa] == 'new':
                                        RevisionDefinicion(lista_word,vericidad)
                    
                    else:
                           verificacion+1
                           return a+size

                else:
                       verificacion+1
                       return a+size

        if lista[a]== "do":
                b=a+1
                condicion= RevisionCondicion(lista[b:],b)
                if not (condicion>size) and (condicion!=b) :
                       RevisionComando(lista[condicion],condicion)
                else:
                       verificacion+1
                       return a+size
        if lista[a]=="repeat":
                b=a+1
                if (b in dicc_publico) and (lista[b+1]=="times"):
                      RevisionComando(lista[b+1],b+1)
                else:
                       verificacion+1
                       return a+size
        else:
               return a
aa = 0   
while ( aa < size) and (verificacion == 0):
    
    if lista_word[aa] == "exec" :
           aa=RevisionComando(lista_word,aa)
    if lista_word[aa] in lista_condi:
           aa=RevisionCondicion(lista_word,aa)
    if lista_word[aa] in lista_estruc and "exec":
           aa=RevisionEstructuraControl(lista_word,aa)
    if lista_word[aa] == 'new':
           aa=RevisionDefinicion(lista_word,aa)
                                                   

if verificacion > 1:
    print('esta mal')

elif verificacion == 0:
    print('esta bien')

#
#archivo = input('ingrese el arhivo: ')
# texto = open(archivo,"r",encoding="utf-8") 
# text = texto.read()
# def simple_tokenizer(text):
#     text = text.lower()
#     text = text.split()

#     return text
# lista_word = simple_tokenizer(text)
  
    
 

            
        


