    #archivo = input('ingrese el arhivo: ')
# archivo = input('ingrese el arhivo: ')
# texto = open(archivo,"r",encoding="utf-8") 
# text = texto.read()
# def simple_tokenizer(text):
#     text = text.lower()
#     text = text.split()

#     return text
# lista_word = simple_tokenizer(text)

text = "NEW VAR rotate = 3 NEW MACRO foo (c , p ) { drop( c ) ; letgo ( p ) ; walk( rotat e ) ; }"
text= text.lower()
text= text.split()
lista_word = text
size = len(lista_word)
dicc_publico = {}
dicc_privado = {}  
verificacion = 0 
list_rango = str(list(range(1,100))) 
posiciones = ["x","y","v"]
list_posicion = ['right','left','front','back'] 
list_cardinales =['north','south','west','east'] 
list_commansTurn = ['left','right',' back']  
lista_comandos = ['jump','walk','turntothe','turntomy','drop','grab','letgo','nop','pick','pop','move','saveexe']

def RevisionCompletitud(list, index, qc, corchete):
    comprobar = list[index]
    if qc < -1 or corchete < -1:
        return -1000
    elif qc == 0 and corchete ==1 :
        return 0
    else:
        if comprobar== '(':
            RevisionCompletitud(list, index+1, qc+1, corchete)
        elif comprobar == ')':
            RevisionCompletitud(list, index+1, qc-1, corchete)
        elif comprobar != '(' and comprobar != ')' and comprobar != '{' and comprobar != '}':
            RevisionCompletitud(list, index+1, qc, corchete)

        elif comprobar== '{':
            RevisionCompletitud(list, index+1, qc, corchete+1)
        elif comprobar == '}' and corchete>1:
            RevisionCompletitud(list, index+1, qc, corchete-1)
        

        elif comprobar == '}' and qc==1:
            RevisionCompletitud(list, index, qc, corchete-1)

for a in range(0,size):
    word = lista_word[a]
    if word == 'new':
        var_mac = lista_word[a+1]
        if var_mac == 'var':
               
            b = a+2
            c = a+3
            d = a+4
            variable = lista_word[b]
            valor = lista_word[c]
            igual = lista_word[d]
            dicc_publico[variable] = valor
    
        if var_mac == 'macro':
            b = a+2
            c = a+3
            lista = []
            variable = lista_word[b]
            indesado = lista_word.index(')', c)
            for aa in range(c+1,indesado):
                if lista_word[aa] != ',':
                    lista.append(lista_word[aa])
            dicc_privado[variable]=lista
            llavedefuncion = indesado+1
            if lista_word[llavedefuncion] == '{':
                indesadofuncion = lista_word.index('}',llavedefuncion)
                coordenada_complititud = RevisionCompletitud(lista_word, llavedefuncion+1, 0, 1)
                print(coordenada_complititud)
                if coordenada_complititud == -1000:
                    verificacion+1
        
    if word == 'jump': 
                    b = a+1 
                    indesado = lista_word.index(')',b)  
                    for aa in range(b+1,indesado): 
                        if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and (lista_word[aa+2] in list_rango or lista_word[aa+2] in posiciones):  
                            verificacion+0
                        else:
                            verificacion+1
    if word == 'move': 
                    b = a+1 
                    indesado = lista_word.index(')',b) 
                    for aa in range(b+1,indesado): 
                        if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                            verificacion+0
                        elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_posicion: 
                            verificacion+0
                        elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_cardinales: 
                            verificacion+0
                        else:
                            verificacion+1
    if word == 'skip': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                                verificacion+0
                            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_posicion: 
                                verificacion+0
                            elif (lista_word[aa] in list_rango or lista_word[aa] in posiciones) and lista_word[aa+1] == ',' and lista_word[aa+2] in list_cardinales: 
                                verificacion+0
                            else:
                                verificacion+1
    if word == 'turn': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_commansTurn): 
                                verificacion+0
                            else:
                                verificacion+1
    if word =='face': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_cardinales):
                                verificacion+0
                            else:
                                verificacion+1
    if word == 'put': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                                verificacion+0
                            else:
                                verificacion+1
    if word == 'pick': 
                        b = a+1 
                        indesado = lista_word.index(')',b) 
                        for aa in range(b+1,indesado): 
                            if (lista_word[aa] in list_rango or lista_word[aa] in posiciones) : 
                                verificacion+0
                            else:
                                verificacion+1

    if word == 'null':    
                        b = a+1 
                        c = a+2
                        if b == '(' and c == ')': 
                            verificacion+0
                        else:
                            verificacion+1            
    if word == 'facing': 
                        b = a+1 
                        indensado = lista_word.index(')',b) 
                        for aa in range(b+1,indensado): 
                            if lista_word[aa] in list_cardinales: 
                                verificacion+0
                            else:
                                verificacion+1

    if  word == 'not': 
                        b = a+1 
                        condicion = lista_word[b] 
                        if condicion == 'can' or condicion == 'facing': 
                            verificacion+0
                        else:
                            verificacion+1
if verificacion > 1:
    print('False')
  
    
        

            
        


