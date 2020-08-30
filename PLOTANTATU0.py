#Program:   PLOTANTATU0
#Obejtivo:  Gerar Dezenas para os proximos concursos
#Data:      Nov/2018
#Input:     Ler O arquivo de resultado da Cef
#Process:   Montar e Descobrir as dezenas sorteada
#OutPut:    listar as dezenas 
#================================================================

import PLOPRM00    as rp # recebe parm
import PLOREGFMT0  as rf # formata registro
import PSYSHtml00  as ht # imprime relatorio
import PLOCMBPSQ0  as ps   # selecionar as dezenas para o proximo concurso
from   CPLOAcol import Aclista
from   CPLOAtraso import Atraso
from   CPLOSelec import Selec
import time
import os
import sys
import datetime    as dt
import numpy       as np
#import wbfDB       as wf 
from   itertools   import combinations

#_________________________________________________
def pxxmain():

    lscomb = []
    lsdados = []
    lsfibo = ['1', '2', '3', '5', '8', '13', '21']
    #lsdados = [0-sort, 1-repe, 2-nova, 3-atrz, 4-sseg, 5-acum, 6-qtreg, 7-par, 8-imp, 9-nsrt, 10-nsrtp, 11-nsrti, 12-pcsai, 13-pcnsai,
    #14-qtd, 15-gpo, 16-qtd, 17-gpo, 18-qtd, 19-gpo, 20-qtd, 21-gpo, 22-qtd, 23-gpo]
 
    lscomb = pxxgeracombfibo(lsfibo)
    lsdados = pxxgeraresu(lscomb, lsfibo)
    lsdeze = pxxescolhe(lsdados) 

#_________________________________________________
def pxxgeracombfibo(lsfibo):
    
    lscomb = []    
    wsconta = 1
    wsctger = 1
    col = 0    

    #___ Geras as combinções possiveis da fibonacci __
    for col in range(col, len(lsfibo)):
        comb = combinations(lsfibo, (7 - col))
        for cbo in comb: 
            print('Numero {} / Comb{} - {} {} '.format(wsctger, wsconta, cbo, (7 - col)))
            wsconta += 1
            wsctger += 1
            lscomb.append(cbo)
       
        wsconta = 1
    
    return lscomb 

#_________________________________________________
def pxxgeraresu(comb, lsfibo):
    """pxxgeraresu [summary]
    
    Arguments:
        comb {[list]} -- [Lista de Combinação]
        lsfibo {[list]} -- [lista de numero fibonacci]
    """

    lsaux  = []
    lsprjg = []  #lista com o jogo a ser analisado    
    lsjgfx = []    
    lsprfx = []  #lista com os jogos De/até   
    lsfaixa = []
    lsjogo = []
    lsatra = []
    lsprjg.clear()
    lsjgfx.clear() 
    lsprfx.clear()   
    lsfaixa.clear()
    lsatra.clear()
    
    LcHrInicio = time.perf_counter()
    #___ Recebe o numero do Jogoe a lista com 1 jogo ____
    lsaux = main_prepara_jogo() 
    lsjgfx = lsaux[0] 
    lsjogo = lsaux[1]  #lista jogo 

    #___ Recebe a faixa de jogo e a lista ____
    lsaux = main_prepara_faixa()
    lsprfx = lsaux[0] 
    lsresfx = lsaux[1] #lista faixa
    
    #_________________________________________________
    LcHrInicio = time.perf_counter()
    #___ lê o Jogo a ser analisado e traz toda a informação ___
    lsjgdados = ps.main_ler_resultado(lsjgfx, lsjogo)       

    #___ Formata os dados de lsjgdados em lsdados 
    #lsdados = pxximpdados(lsjgdados, lsprfx) 
    lsdados = pxxfmtcol(lsjgdados, lsprfx)

    oSelec = Selec(lsdados)    
    lsesco = oSelec.pxxescolhe()

    #oSelec = Selec(lsjgdados, lsatra)    
    #oSelec.pxxprint()

    lsprfx = lsaux[0] 
    lsresfx = lsaux[1] #lista faixa
    pxxlistfibo(comb, lsprfx,  lsresfx, lsfibo, LcHrInicio) 

    #___ ler as ombinaçôes possiveis para os numeros fibonacci ___
    lsaux = rf.pxxqtdesaiu(plsresu, lsista)

    lshmtcomb = lsaux[1]
    lstparam  = ['16', '',  lsfaixa[0], lsfaixa[1], lsista, len(plsresu)]
    lccab = "Acertos para um grupo de dezenas"
    lsobtarq = rp.pxobtarqrelat()
    ht.PxMaincomb9(lshmtcomb, lccab, LcHrInicio, lsobtarq[0], lstparam) 

#_________________________________________________   
def pxximpdados(lsjgdados, lsprfx):

    lsaux = []
   
    print('______ SORTEADA ATUAL______')
    print('Jogo: {} Data: {} DiaS: {}'.format(lsjgdados[0][0], lsjgdados[0][1], lsjgdados[0][2]))
    #lsaux = [0-sort, 1-repe, 2-nova, 3-atrz, 4-sseg, 5-acum, 6-qtreg, 7-par, 8-imp, 9-nsrt, 10-nsrtp, 11-nsrti, 12-pcsai, 13-pcnsai,
    #14-qtd, 15-gpo, 16-qtd, 17-gpo, 18-qtd, 19-gpo, 20-qtd, 21-gpo, 22-qtd, 23-gpo]
    
    oAclista = Aclista(lsjgdados[0][3])    
    lsres = oclista.pxxacerta() 
    print('  Sort  : {}'.format(lsres))
    lsaux.append(list(lsres)) 
    #
    oAclista = Aclista(lsjgdados[0][18])    
    lsres = oAclista.pxxacerta() 
    print('  Repe  : {}'.format(lsres))
    lsaux.append(list(lsres))
    #
    oAclista = Aclista(lsjgdados[0][19])    
    lsres = oAclista.pxxacerta() 
    print('  Nova  : {}'.format(lsres))
    lsaux.append(list(lsres))
      
    #_____________________________________________
    #___ Prepara para montar as atrasadas
    lsaux2 = main_prepara_faixa2(lsprfx)
    lsfaixa = lsaux2[1]  
    oAtraso = Atraso(lsfaixa) 
    lsres = oAtraso.pxxatrasada()
    print('  Atra  : {}'.format(lsres))
    #lsatra = list(lsres)
    lsaux.append(list(lsres))
   
    #___ Prepara para montar as Saidas Seguidas
    oSaiseg = Atraso(lsfaixa) 
    lsres = oSaiseg.pxxseguidas()
    print('  Seg   : {}'.format(lsres))
    #lsseg = list(lsres)
    lsaux.append(list(lsres))
      
    #___________________________________________________________
    #___ totais das colunas, FAIXA SELECIONADA_
    lsres = rf.pxselacm(lsfaixa)
    del lsres[1]
    del lsres[0]
    print('  Acum  : {}'.format(lsres))
    lsaux.append(list(lsres))
    lsaux.append(len(lsfaixa))
    print('  Qreg  : {}'.format(len(lsfaixa)))
    
    #____________________________________________________________
    oAclista = Aclista(lsjgdados[0][4])    
    lsres = oAclista.pxxacerta() 
    print('   Par  : {}'.format(lsres))
    lsaux.append(list(lsres))
    
    oAclista = Aclista(lsjgdados[0][5])    
    lsres = oAclista.pxxacerta() 
    print('   Impar: {}'.format(lsres))
    lsaux.append(list(lsres))

    oAclista = Aclista(lsjgdados[0][6])    
    lsres = oAclista.pxxacerta() 
    print('  NSrt  : {}'.format(lsres))
    lsaux.append(list(lsres))

    oAclista = Aclista(lsjgdados[0][7])    
    lsres = oAclista.pxxacerta() 
    print('   Par  : {}'.format(lsres))
    lsaux.append(list(lsres))

    oAclista = Aclista(lsjgdados[0][8])    
    lsres = oAclista.pxxacerta() 
    print('   Impar: {}'.format(lsres))     
    lsaux.append(list(lsres))

    lsres = pxxsainsai(lsaux[5], (lsaux[6]))
    lsaux.append(list(lsres[0]))
    lsaux.append(list(lsres[1]))
    print('   psai : {}'.format(lsres[0]))  
    print('   pnsai: {}'.format(lsres[1]))  
   

    print(' ')
      

    return(lsaux)

#_________________________________________
def pxxacumula(lsfaixa):

    lsslac = []  # totais das colunas, qtas vezes saiu cada dezena

    #___ acumulado para a FAIXA SELECIONADA_
    lsslac   = rf.pxselacm(lsfaixa)

    return lsslac

    print('______ POR LINHA e Dezenas ______')
    print('Linha')
    print('L1-{}: {} '.format(lsjgdados[0][22][0], lsjgdados[0][22][5]))
    print('L2-{}: {} '.format(lsjgdados[0][22][1], lsjgdados[0][22][6])) 
    print('L3-{}: {} '.format(lsjgdados[0][22][2], lsjgdados[0][22][7]))
    print('L4-{}: {} '.format(lsjgdados[0][22][3], lsjgdados[0][22][8]))
    print('L5-{}: {} '.format(lsjgdados[0][22][4], lsjgdados[0][22][9]))

#_________________________________________________
def pxxlistfibo(lscombi, lsfaixa, plsresu, lsista, LcHrInicio):
   
    #___ ler as ombinaçôes possiveis para os numeros fibonacci ___
    lscbo = list(lscombi)
    lsaux = rf.pxxqtdesaiu(plsresu, lsista)

    lshmtcomb = lsaux[1]
    lstparam  = ['16', '',  lsfaixa[0], lsfaixa[1], lsista, len(plsresu)]
    lccab = "Acertos para um grupo de dezenas"
    lsobtarq = rp.pxobtarqrelat()
    ht.PxMaincomb9(lshmtcomb, lccab, LcHrInicio, lsobtarq[0], lstparam) 

    #return(lsjgdados, plsresu)  
    a = 1

#__________________________________________________________
def  main_prepara_jogo():     

    print('   ==> Informe o JOGO a ser analisado')
    #___obtém o path do resultado    
    lsobtarq = rp.pxobtarq()       
    nlines = rp.pxobterqtjogos(lsobtarq[2])     
 
    LcCrt = False
    while LcCrt == False:
        try:
            lsjogo = rp.pxobterjogo(lsobtarq[2])          #escolhe um jogo
            if int(lsjogo) < 2:
                os.system('cls')
                print('Informe um jogo de 2 até {}'.format(nlines))
            else:
                LcCrt = True     

        except ValueError:
            print('Dado não Numerico, informe um número de 2 até {}'.format(nlines))
       
    #lsjogo = rp.pxobterjogo(lsobtarq[2])          #escolhe um jogo
    lsprfx = [lsjogo, lsjogo]
    lsResu = rf.pxlercsv(lsobtarq[2], lsprfx)   #obter os jogos da faixa 
    return([lsprfx, lsResu])

#__________________________________________________________
def  main_prepara_faixa():  

    print('   ==> Informe o DE/ATÉ a serem analisados') 
    lsobtarq = rp.pxobtarq()                        #obtém o path do resultado            
    lsprfx   = rp.pxobterjgds(lsobtarq[2])          #escolhe um DE/ATÉ 
    lsResu   = rf.pxlecsvgpsel01(lsobtarq[2], lsprfx) #obter os jogos da faixa wbf 28/06/2019
    return([lsprfx, lsResu])

#__________________________________________________________
def  main_prepara_faixa2(lsprfx):
    
    lsobtarq = rp.pxobtarq()                       #obtém o path do resultado            
    lsResu   = rf.pxlercsv(lsobtarq[2], lsprfx)    #obter os jogos da faixa 
    return([lsprfx, lsResu])

#__________________________________________________________
def pxxsainsai(lsacm, wsqt):
    wspsai = 0.0
    wspnsai = 0.0
    lspsai = []
    lspnsai = []
    
    for icol in range(0, len(lsacm)):
        wspsai  = round(lsacm[icol] / wsqt, 2)
        wspnsai = round(1 - wspsai, 2)
        lspsai.append(wspsai)
        lspnsai.append(wspnsai)
    
    return([lspsai, lspnsai])
#__________________________________________________________
def pxxfmtcol(lsjgdados, lsprfx):

    #[0-sort, 1-repe, 2-nova, 3-atrz, 4-sseg, 5-acum, 6-qtreg, 7-par, 8-imp, 9-nsrt, 10-nsrtp, 11-nsrti, 12-pcsai, 13-pcnsai,
    #14-qtd, 15-gpo, 16-qtd, 17-gpo, 18-qtd, 19-gpo, 20-qtd, 21-gpo, 22-qtd, 23-gpo]

    lstdesc = ['Sort', 'Repe', 'Nova', '', '', '', 'Par ', 'Imp ', 'NSrt', 'Par ', 'Imp ', '' ]
    lsjgsad = [lsjgdados[0][3], lsjgdados[0][18], lsjgdados[0][19], '', '', '', lsjgdados[0][4], lsjgdados[0][5], lsjgdados[0][6], lsjgdados[0][7], lsjgdados[0][8], '' ]
    lsres = []
    lsaux = []

    for icol in range(0, len(lstdesc)):             
        if icol == 3:
            #___ ATRASADAS _______
            lsaux2 = main_prepara_faixa2(lsprfx)
            lsfaixa = lsaux2[1]  
            oAtraso = Atraso(lsfaixa) 
            lsres = oAtraso.pxxatrasada()
            print('  Atra  : {}'.format(lsres))
            lsaux.append(list(lsres))

        elif icol == 4:
            #___ SEGUIDAS ___
            oSaiseg = Atraso(lsfaixa) 
            lsres = oSaiseg.pxxseguidas()
            print('  Seg   : {}'.format(lsres))
            #lsseg = list(lsres)
            lsaux.append(list(lsres))
        
        elif icol == 5:
            #___ TOTAIS DAS COLUNA, FAIXA SELECIONADA ___
            lsres = rf.pxselacm(lsfaixa)
            del lsres[1]
            del lsres[0]
            print('  Acum  : {}'.format(lsres))
            lsaux.append(list(lsres))
            lsaux.append(len(lsfaixa))
            print('  Qreg  : {}'.format(len(lsfaixa)))
        
        elif icol == 11:
            #___ % QUE SAI CADA COLUNA ___
            lsres = pxxsainsai(lsaux[5], (lsaux[6]))
            lsaux.append(list(lsres[0]))
            lsaux.append(list(lsres[1]))
            print('  psai  : {}'.format(lsres[0]))  
            print('  pnsai : {}'.format(lsres[1]))    
            #
            for wcol in range(0,5):
                lsaux.append(lsjgdados[0][22][wcol])
                lsaux.append(lsjgdados[0][22][wcol + 5])
                print('  L{}-{}: {} '.format(wcol + 1, lsjgdados[0][22][wcol], lsjgdados[0][22][wcol + 5]))
            
        else:
            oAclista = Aclista(lsjgsad[icol])    
            lsres = oAclista.pxxacerta() 
            print('  {}  : {}'.format(lstdesc[icol], lsres))
            lsaux.append(list(lsres))    
        
    return(lsaux)      

#___________________________________________
pxxmain()

    # print('______ ANTERIOR ______')
    # print('Jogo:  {} Data: {} Dsem: {}'.format(lsjgdados[0][9], lsjgdados[0][10], lsjgdados[0][11]))

    # oAclista = Aclista(lsjgdados[0][12])    
    # lsres = oAclista.pxxacerta() 
    # print('  Sort  : {}'.format(lsres))
    # #
    # oAclista = Aclista(lsjgdados[0][18])    
    # lsres = oAclista.pxxacerta() 
    # print('  Repe  : {}'.format(lsres))
    # #
    # oAclista = Aclista(lsjgdados[0][19])    
    # lsres = oAclista.pxxacerta() 
    # print('  Nova  : {}'.format(lsres))

    # oAclista = Aclista(lsjgdados[0][13])    
    # lsres = oAclista.pxxacerta() 
    # print('    Par : {}'.format(lsres))
    
    # oAclista = Aclista(lsjgdados[0][14])    
    # lsres = oAclista.pxxacerta() 
    # print('   Impar: {}'.format(lsres))

    # oAclista = Aclista(lsjgdados[0][15])    
    # lsres = oAclista.pxxacerta() 
    # print('  NSrt  : {}'.format(lsres))

    # oAclista = Aclista(lsjgdados[0][16])    
    # lsres = oAclista.pxxacerta() 
    # print('   Par  : {}'.format(lsres))

    # oAclista = Aclista(lsjgdados[0][17])    
    # lsres = oAclista.pxxacerta() 
    # print('   Impar: {}'.format(lsres))


#   dictdados ={'Sort': lsjgdados[0][3],   'Rep':lsjgdados[0][18],  'Nova': lsjgdados[0][19],
#                 'Atra': lsres,           'Par':lsjgdados[0][4],   'Impar': lsjgdados[0][5],
#                 'NSrt': lsjgdados[0][6], 'Par':lsjgdados[0][7],   'Impar': lsjgdados[0][8], 
#                 'Sort': lsjgdados[0][3], 'Rep': lsjgdados[0][18], 'Nova': lsjgdados[0][19],
#                 'Atra': lsres,           'Par':lsjgdados[0][4],   'Impar': lsjgdados[0][5],
#                 'NSrt': lsjgdados[0][6], 'Par':lsjgdados[0][7],   'Impar': lsjgdados[0][8],   
#                }

# print('  Sort  : {}'.format(lsjgdados[0][3]))
# print('  Repe  : {}'.format(lsjgdados[0][18]))
# print('  Nova  : {}'.format(lsjgdados[0][19]))
# #print('  Atra  : {}'.format(lsatra))
# print(' ')
# print('   Par  : {}'.format(lsjgdados[0][4]))
# print('   Impar: {}'.format(lsjgdados[0][5]))  
# print(' ')
# print('  NSrt :  {}'.format(lsjgdados[0][6]))
# print('   Par  : {}'.format(lsjgdados[0][7]))
# print('   Impar: {}'.format(lsjgdados[0][8]))    
# print(' ')
# print('______ ANTERIOR ______')
# print('Jogo:  {} Data: {} Dsem: {}'.format(lsjgdados[0][9], lsjgdados[0][10], lsjgdados[0][11]))
# print('  Sort  : {}'.format(lsjgdados[0][12]))
# print('  Repe  : {}'.format(lsjgdados[0][18]))
# print('  Nova  : {}'.format(lsjgdados[0][19]))
# print(' ')
# print('   Par  : {}'.format(lsjgdados[0][13]))
# print('   Impar: {}'.format(lsjgdados[0][14]))  
# print(' ') 
# print('  NSrt  : {}'.format(lsjgdados[0][15]))
# print('   Par  : {}'.format(lsjgdados[0][16]))
# print('   Impar: {}'.format(lsjgdados[0][17])) 

# print('______ POR LINHA e Dezenas ______')
# print('Linha')
# print('L1-{}: {} '.format(lsjgdados[0][22][0], lsjgdados[0][22][5]))
# print('L2-{}: {} '.format(lsjgdados[0][22][1], lsjgdados[0][22][6])) 
# print('L3-{}: {} '.format(lsjgdados[0][22][2], lsjgdados[0][22][7]))
# print('L4-{}: {} '.format(lsjgdados[0][22][3], lsjgdados[0][22][8]))
# print('L5-{}: {} '.format(lsjgdados[0][22][4], lsjgdados[0][22][9]))


#_________________________________________________
# def pxatrasada(plsresultado):
    
#     wsatr = 0 
#     lsaux = []
#     lsatr = []   
#     lsatr.clear() 

#     #--- inicializa a lsatr e monta os campos na posição
#     for col in range(0, 26):  
#         if col > 9:
#             lsatr.append('  ') 
#         else:
#             lsatr.append(' ') 
  
#     plsresultado.reverse()
#     for col in range(2, 27): 
#         wsatr = 0
#         for lsresu in plsresultado:                            
#             if lsresu[col] == '': 
#                 wsatr += 1
#                 #--- somando o atraso ---
#             else:
#                 wspos = int(lsresu[col])
#                 if wsatr > 0:
#                     lsatr[wspos] = ' ' + str(wsatr)
#                     #--- quanto está atrasada ---
#                 else:
#                     a = 1
#                     #--- em dia ----
                
#                 break  

#     del lsatr[0]
#     return(lsatr)


    # print('  Sort  : {}'.format(lsjgdados[0][12]))
    # print('  Repe  : {}'.format(lsjgdados[0][18]))
    # print('  Nova  : {}'.format(lsjgdados[0][19]))
    # print(' ')
    # print('   Par  : {}'.format(lsjgdados[0][13]))
    # print('   Impar: {}'.format(lsjgdados[0][14]))  
    # print(' ') 
    # print('  NSrt  : {}'.format(lsjgdados[0][15]))
    # print('   Par  : {}'.format(lsjgdados[0][16]))
    # print('   Impar: {}'.format(lsjgdados[0][17])) 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # lsaux  = []
    # lsprjg = []  #lista com o jogo a ser analisado    
    # lsjgfx = []    
    # lsprfx  = []  #lista com os jogos De/até   
    # lsfaixa = []
    # lsprjg.clear() 
    # lsjgfx.clear() 
    # lsprfx.clear()   
    # lsfaixa.clear()
  
    # #___ lê o Jogo a ser analisado ____    
    # LcCrt = False
    # while LcCrt == False:
    #     lsaux = main_prepara_jogo() 
    #     if int(lsaux[0][0]) < 2:
    #         os.system('cls')
    #         print('Informe um número, maior que 1')           
    #     else:
    #         LcCrt = True

    # lsjgfx = lsaux[0] 
    # lsjogo = lsaux[1]  #lista jogo 

    # #___ lê os Jogos para saber as atrasadas ____
    # lsaux  = main_prepara_faixa()
    # lsprfx = lsaux[0] 
    # lsfaixa = lsaux[1] #lista faixa
    
    # #_____________________________________________________________________
    # LcHrInicio = time.perf_counter()
    # #___ lê o Jogo a ser analisado ____
    # lsjgdados = ps.main_ler_resultado(lsjgfx, lsjogo)   

    # #___ acessa o programa PLOTGPSEL01 ___ wbf julho/2019
    # lshtmlapo = gs.pxmain(lsjgdados, lsprfx, lsfaixa)  

    # #___ lê os Jogos para saber as atrasadas ____
    # lsaux  = main_prepara_faixa2(lsprfx)
    # lsfaixa = lsaux[1] #lista faixa
