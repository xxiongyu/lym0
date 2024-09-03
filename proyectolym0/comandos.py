#archivo = input('ingrese el arhivo: ')
archivo = input('ingrese el arhivo: ')
texto = open(archivo,"r",encoding="utf-8") 
text = texto.read()
def simple_tokenizer(text):
    text = text.split()
    text = text.lower()
    return text
lista_word = simple_tokenizer(text)
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

def RevisionCompletitud(list, index, qc, Findex):
    if qc < -1:
        return -1000
    elif qc == 0:
        return Findex
    else:
        if list[index]== '(':
            RevisionCompletitud(list, index+1, qc+1, Findex)
        elif list[index] == 'defun':
            RevisionCompletitud(list, index+1, -10, Findex)
        elif list[index] == ')' and qc>1:
            RevisionCompletitud(list, index+1, qc-1, Findex)
        elif list[index] != '(' and list[index] != ')':
            RevisionCompletitud(list, index+1, qc, Findex)
        
        else:
            RevisionCompletitud(list, index, qc-1, index)

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
            if lista_word[llavedefuncion] == '{}':
                indesadofuncion = lista_word.index('}',llavedefuncion)
                coordenada_complititud = RevisionCompletitud(lista_word, llavedefuncion, 1, 0)
                v_publico = dicc_publico.keys()
                v_privado = dicc_privado.get(variable)
                if coordenada_complititud == -1000:
                    print('False')
        
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
    
        

            
        


