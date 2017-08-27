import os
def criaMatriz(matriz):
    for i in range(0,len(matriz)):
        if i%2==0:
            for c in range(0,11):
                if c==3 or c==7:
                    matriz[i][c]='|'
                #switch(i)
                elif i==0:
                    if c==1:
                        matriz[i][c]='1'
                    elif c==5:
                        matriz[i][c]='2'
                    elif c==9:
                        matriz[i][c]='3'
                    else:
                        matriz[i][c]=' '
                elif i==2:
                    if c==1:
                        matriz[i][c]='4'
                    elif c==5:
                        matriz[i][c]='5'
                    elif c==9:
                        matriz[i][c]='6'
                    else:
                        matriz[i][c]=' '
                elif i==4:
                    if c==1:
                        matriz[i][c]='7'
                    elif c==5:
                        matriz[i][c]='8'
                    elif c==9:
                        matriz[i][c]='9'
                    else:
                        matriz[i][c]=' '
        if i%2==1:
            for c in range(0,11):
                if c==3 or c==7:
                    matriz[i][c]='+'
                else:
                    matriz[i][c]='-'
    return None
def printMatriz(matriz):
    for i in range(0,len(matriz)):
        for c in range(0,11):
            print(matriz[i][c],end="")
        if i!=4:
            print("\n")
    return None
def check_winner(matriz):
    #3 horizontais
    if matriz[0][1]==matriz[0][5] and matriz[0][1]==matriz[0][9]:
        return 1
    if matriz[2][1]==matriz[2][5] and matriz[2][1]==matriz[2][9]:
        return 1
    if matriz[4][1]==matriz[4][5] and matriz[4][1]==matriz[4][9]:
        return 1
    #3 verticais
    if matriz[0][1]==matriz[2][1] and matriz[0][1]==matriz[4][1]:
        return 1
    if matriz[0][5]==matriz[2][5] and matriz[0][5]==matriz[4][5]:
        return 1
    if matriz[0][9]==matriz[2][9] and matriz[0][9]==matriz[4][9]:
        return 1
    #2 diagonais
    if matriz[0][1]==matriz[2][5] and matriz[0][1]==matriz[4][9]:
        return 1
    if matriz[0][9]==matriz[2][5] and matriz[0][9]==matriz[4][1]:
        return 1
    return 0
def print_result(matriz,e,count):
    if e==0:
        os.system(''+['clear', 'cls'][(os.name)=='nt'])
        print('\nJogo do Welho:\n\n')
        print("Jogada: "+str(count)+"\n\n")
        printMatriz(matriz)
        print('\n\nO jogo terminou empatado.\n')
    if e==1:
        os.system(''+['clear', 'cls'][(os.name)=='nt'])
        print('\nJogo do Welho:\n\n')
        print("Jogada: "+str(count)+"\n\n")
        printMatriz(matriz)
        print('\n\nO vencedor foi X na jogada '+str(count)+'.\n')
    if e==2:
        os.system(''+['clear', 'cls'][(os.name)=='nt'])
        print('\nJogo do Welho:\n\n')
        print("Jogada: "+str(count)+"\n\n")
        printMatriz(matriz)
        print('\n\nO vencedor foi O na jogada '+str(count)+'.\n')
    return None
def computer_move(log_mymove,matriz,count):
    mymove=0
    mymove=check_win(log_mymove,matriz,mymove)
    if mymove==0:
        mymove=check_block(log_mymove,matriz,mymove)
    if mymove==0:
        mymove=default_move(log_mymove,matriz,mymove,count)
    return mymove
def check_block(log_mymove,matriz,mymove):
    a1=a2=a3=a4=a5=a6=a7=a8=a9=0
    for i in range(0,5):
        if log_mymove[i]==1:
            a1=1
        if log_mymove[i]==2:
            a2=1
        if log_mymove[i]==3:
            a3=1
        if log_mymove[i]==4:
            a4=1
        if log_mymove[i]==5:
            a5=1
        if log_mymove[i]==6:
            a6=1
        if log_mymove[i]==7:
            a7=1
        if log_mymove[i]==8:
            a8=1
        if log_mymove[i]==9:
            a9=1
    if a1==0:
        if (matriz[0][5]==matriz[0][9] and matriz[0][5]=='X') and matriz[0][1]=='1':
            mymove=1
        if (matriz[2][1]==matriz[4][1] and matriz[2][1]=='X') and matriz[0][1]=='1':
            mymove=1
        if (matriz[2][5]==matriz[4][9] and matriz[2][5]=='X') and matriz[0][1]=='1':
            mymove=1
    if a2==0:
        if (matriz[0][1]==matriz[0][9] and matriz[0][1]=='X') and matriz[0][5]=='2':
            mymove=2
        if (matriz[2][5]==matriz[4][5] and matriz[2][5]=='X') and matriz[0][5]=='2':
            mymove=2
    if a3==0:
        if (matriz[0][1]==matriz[0][5] and matriz[0][1]=='X') and matriz[0][9]=='3':
            mymove=3
        if (matriz[2][9]==matriz[4][9] and matriz[2][9]=='X') and matriz[0][9]=='3':
            mymove=3
        if (matriz[2][5]==matriz[4][9] and matriz[2][5]=='X') and matriz[0][9]=='3':
            mymove=3
    if a4==0:
        if (matriz[2][5]==matriz[2][9] and matriz[2][5]=='X') and matriz[2][1]=='4':
            mymove=4
        if (matriz[0][1]==matriz[4][1] and matriz[0][1]=='X') and matriz[2][1]=='4':
            mymove=4
    if a5==0:
        if (matriz[0][9]==matriz[4][1] and matriz[0][9]=='X') and matriz[2][5]=='5':
            mymove=5
        if (matriz[2][1]==matriz[2][9] and matriz[2][1]=='X') and matriz[2][5]=='5':
            mymove=5
        if (matriz[0][5]==matriz[4][5] and matriz[0][5]=='X') and matriz[2][5]=='5':
            mymove=5
        if (matriz[0][1]==matriz[4][9] and matriz[0][1]=='X') and matriz[2][5]=='5':
            mymove=5
    if a6==0:
        if (matriz[2][1]==matriz[2][5] and matriz[2][1]=='X') and matriz[2][9]=='6':
            mymove=6
        if (matriz[0][9]==matriz[4][9] and matriz[0][9]=='X') and matriz[2][9]=='6':
            mymove=6
    if a7==0:
        if (matriz[0][9]==matriz[2][5] and matriz[0][9]=='X') and matriz[4][1]=='7':
            mymove=7
        if (matriz[4][5]==matriz[4][9] and matriz[4][5]=='X') and matriz[4][1]=='7':
            mymove=7
        if (matriz[0][1]==matriz[2][1] and matriz[0][1]=='X') and matriz[4][1]=='7':
            mymove=7
    if a8==0:
        if (matriz[4][1]==matriz[4][9] and matriz[4][1]=='X') and matriz[4][5]=='8':
            mymove=8
        if (matriz[0][5]==matriz[2][5] and matriz[0][5]=='X') and matriz[4][5]=='8':
            mymove=8
    if a9==0:
        if (matriz[4][1]==matriz[4][5] and matriz[4][1]=='X') and matriz[4][9]=='9':
            mymove=9
        if (matriz[0][9]==matriz[2][9] and matriz[0][9]=='X') and matriz[4][9]=='9':
            mymove=9
        if (matriz[0][1]==matriz[2][5] and matriz[0][1]=='X') and matriz[4][9]=='9':
            mymove=9
    return mymove
def check_win(log_mymove,matriz,mymove):
    a1=a2=a3=a4=a5=a6=a7=a8=a9=0
    for i in range(0,5):
        if log_mymove[i]==1:
            a1=1
        if log_mymove[i]==2:
            a2=1
        if log_mymove[i]==3:
            a3=1
        if log_mymove[i]==4:
            a4=1
        if log_mymove[i]==5:
            a5=1
        if log_mymove[i]==6:
            a6=1
        if log_mymove[i]==7:
            a7=1
        if log_mymove[i]==8:
            a8=1
        if log_mymove[i]==9:
            a9=1
    if a1==0:
        if (matriz[0][5]==matriz[0][9] and matriz[0][5]=='O') and matriz[0][1]=='1':
            mymove=1
        if (matriz[2][1]==matriz[4][1] and matriz[2][1]=='O') and matriz[0][1]=='1':
            mymove=1
        if (matriz[2][5]==matriz[4][9] and matriz[2][5]=='O') and matriz[0][1]=='1':
            mymove=1
    if a2==0:
        if (matriz[0][1]==matriz[0][9] and matriz[0][1]=='O') and matriz[0][5]=='2':
            mymove=2
        if (matriz[2][5]==matriz[4][5] and matriz[2][5]=='O') and matriz[0][5]=='2':
            mymove=2
    if a3==0:
        if (matriz[0][1]==matriz[0][5] and matriz[0][1]=='O') and matriz[0][9]=='3':
            mymove=3
        if (matriz[2][9]==matriz[4][9] and matriz[2][9]=='O') and matriz[0][9]=='3':
            mymove=3
        if (matriz[2][5]==matriz[4][1] and matriz[2][5]=='O') and matriz[0][9]=='3':
            mymove=3
    if a4==0:
        if (matriz[2][5]==matriz[2][9] and matriz[2][5]=='O') and matriz[2][1]=='4':
            mymove=4
        if (matriz[0][1]==matriz[4][1] and matriz[0][1]=='O') and matriz[2][1]=='4':
            mymove=4
    if a5==0:
        if (matriz[0][9]==matriz[4][1] and matriz[0][9]=='O') and matriz[2][5]=='5':
            mymove=5
        if (matriz[2][1]==matriz[2][9] and matriz[2][1]=='O') and matriz[2][5]=='5':
            mymove=5
        if (matriz[0][5]==matriz[4][5] and matriz[0][5]=='O') and matriz[2][5]=='5':
            mymove=5
        if (matriz[0][1]==matriz[4][9] and matriz[0][1]=='O') and matriz[2][5]=='5':
            mymove=5
    if a6==0:
        if (matriz[2][1]==matriz[2][5] and matriz[2][1]=='O') and matriz[2][9]=='6':
            mymove=6
        if (matriz[0][9]==matriz[4][9] and matriz[0][9]=='O') and matriz[2][9]=='6':
            mymove=6
    if a7==0:
        if (matriz[0][9]==matriz[2][5] and matriz[0][9]=='O') and matriz[4][1]=='7':
            mymove=7
        if (matriz[4][5]==matriz[4][9] and matriz[4][5]=='O') and matriz[4][1]=='7':
            mymove=7
        if (matriz[0][1]==matriz[2][1] and matriz[0][1]=='O') and matriz[4][1]=='7':
            mymove=7
    if a8==0:
        if (matriz[4][1]==matriz[4][9] and matriz[4][1]=='O') and matriz[4][5]=='8':
            mymove=8
        if (matriz[0][5]==matriz[2][5] and matriz[0][5]=='O') and matriz[4][5]=='8':
            mymove=8
    if a9==0:
        if (matriz[4][1]==matriz[4][5] and matriz[4][1]=='O') and matriz[4][9]=='9':
            mymove=9
        if (matriz[0][9]==matriz[2][9] and matriz[0][9]=='O') and matriz[4][9]=='9':
            mymove=9
        if (matriz[0][1]==matriz[2][5] and matriz[0][1]=='O') and matriz[4][9]=='9':
            mymove=9
    return mymove
def default_move(log_mymove,matriz,mymove,count):
    #começando em canto lateral
    if count==1 and (matriz[0][1]=='X' or matriz[0][9]=='X'or matriz[4][1]=='X'or matriz[4][9]=='X'):
        mymove=5
    if count==3 and((matriz[0][1]=='X'or matriz[0][9]=='X'or matriz[4][1]=='X'or matriz[4][9]=='X')and(matriz[2][5]=='O')):
        if matriz[0][5]=='2' and matriz[4][5]=='8':
            mymove=2
        else:
            mymove=6
    #começando em canto central
    if(count==1)and(matriz[0][5]=='X'):
        mymove=1
    if(count==1)and(matriz[2][9]=='X'):
        mymove=3
    if(count==1)and(matriz[2][1]=='X'):
        mymove=1
    if(count==1)and(matriz[4][5]=='X'):
        mymove=7
    
    if(count==3)and((matriz[0][5]=='X'and matriz[4][5]=='X')or(matriz[2][1]=='X'and matriz[2][9]=='X')):
        mymove=5
    if count==3 and matriz[2][5]=='5':
        mymove=5
    
    if(count==5) and (matriz[0][1]=='O') and (matriz[4][1]=='7'):
        mymove=3
    if(count==5) and (matriz[0][9]=='O') and (matriz[4][9]=='9'):
        mymove=1
    if(count==5) and (matriz[4][1]=='O') and (matriz[0][1]=='1'):
        mymove=3
    
    if(count==3)and(mymove==0)and(matriz[0][5]=='X' or matriz[2][9]=='X' or matriz[2][1]=='X' or matriz[4][5]=='X') and (matriz[0][5]=='2' and matriz[4][5]=='8'):
        mymove=2
    if((count==3) and (mymove==0) and (matriz[0][5]=='X' or matriz[2][9]=='X' or matriz[2][1]=='X' or matriz[4][5]=='X') and (matriz[2][1]=='4' and matriz[2][9]=='6')):
        mymove=4
    if((count==3) and (mymove==0) and (((matriz[0][5]=='X' or matriz[4][5]=='X') and (matriz[2][1]=='X' or matriz[2][9]=='X')) or ((matriz[2][1]=='X' or matriz[2][9]=='X') and (matriz[0][5]=='X' or matriz[4][5]=='X'))) and (matriz[2][5]=='O')): 
        mymove=1
    #começando no centro
    if count==1 and matriz[2][5]=='X':
        mymove=3
    #default
    if(count==3):
        if check_block(log_mymove,matriz,mymove)!=0:
            if check_win(log_mymove,matriz,mymove)!=0:
                mymove=check_win(log_mymove,matriz,mymove)
            else: 
                mymove=check_block(log_mymove,matriz,mymove)
        if mymove==0:
            if matriz[0][1]=='1':
                mymove=1
        if mymove==0:
            if matriz[0][5]=='2':
                mymove=2
        if mymove==0:
            if matriz[0][9]=='3':
                mymove=3
        if mymove==0:
            if matriz[2][1]=='4': 
                mymove=4
        if mymove==0:
            if matriz[2][5]=='5': 
                mymove=5
        if mymove==0:
            if matriz[2][9]=='6': 
                mymove=6
        if mymove==0:
            if matriz[4][1]=='7': 
                mymove=7
        if mymove==0:
            if matriz[4][5]=='8': 
                mymove=8
        if mymove==0:
            if matriz[4][9]=='9': 
                mymove=9
    if (count==5) and ((matriz[0][5]=='X' or matriz[0][9]=='X') and (matriz[2][1]=='X' or matriz[4][1]=='X')):
        mymove=1
    if (count==5) and ((matriz[0][1]=='X' or matriz[0][5]=='X') and (matriz[2][9]=='X' or matriz[4][9]=='X')):
        mymove=3
    if (count==5) and ((matriz[4][5]=='X' or matriz[4][9]=='X') and (matriz[0][1]=='X' or matriz[2][1]=='X')):
        mymove=7
    if (count==5) and ((matriz[4][1]=='X' or matriz[4][5]=='X') and (matriz[0][9]=='X' or matriz[2][9]=='X')):
        mymove=9
    if(count==5):
        if check_block(log_mymove,matriz,mymove)!=0:
            if check_win(log_mymove,matriz,mymove)!=0:
                mymove=check_win(log_mymove,matriz,mymove)
            else: 
                mymove=check_block(log_mymove,matriz,mymove)
        if mymove==0:
            if matriz[0][1]=='1':
                mymove=1
        if mymove==0:
            if matriz[0][5]=='2':
                mymove=2
        if mymove==0:
            if matriz[0][9]=='3':
                mymove=3
        if mymove==0:
            if matriz[2][1]=='4': 
                mymove=4
        if mymove==0:
            if matriz[2][5]=='5': 
                mymove=5
        if mymove==0:
            if matriz[2][9]=='6': 
                mymove=6
        if mymove==0:
            if matriz[4][1]=='7': 
                mymove=7
        if mymove==0:
            if matriz[4][5]=='8': 
                mymove=8
        if mymove==0:
            if matriz[4][9]=='9': 
                mymove=9
    if count==7:
        if check_block(log_mymove,matriz,mymove)!=0:
            if check_win(log_mymove,matriz,mymove)!=0:
                mymove=check_win(log_mymove,matriz,mymove)
            else: 
                mymove=check_block(log_mymove,matriz,mymove)
        if mymove==0:
            if matriz[0][1]=='1':
                mymove=1
        if mymove==0:
            if matriz[0][5]=='2':
                mymove=2
        if mymove==0:
            if matriz[0][9]=='3':
                mymove=3
        if mymove==0:
            if matriz[2][1]=='4': 
                mymove=4
        if mymove==0:
            if matriz[2][5]=='5': 
                mymove=5
        if mymove==0:
            if matriz[2][9]=='6': 
                mymove=6
        if mymove==0:
            if matriz[4][1]=='7': 
                mymove=7
        if mymove==0:
            if matriz[4][5]=='8': 
                mymove=8
        if mymove==0:
            if matriz[4][9]=='9': 
                mymove=9
    return mymove    
while(True):
    l0=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    l1=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    l2=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    l3=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    l4=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    matriz=[l0,l1,l2,l3,l4]
    count=0
    e=0
    log_mymove=['','','','','',]
    criaMatriz(matriz)
    menu=int(input("\nJogar contra IA(1)/Player(2)? "))
    if menu==2:
        while(count<10):
            item=''
            os.system(''+['clear', 'cls'][(os.name)=='nt'])
            print('\nJogo do Welho:\n\n')
            print("Jogada: "+str(count)+"\n\n")
            printMatriz(matriz)
            e=check_winner(matriz)
            if e!=0 and count%2==0:
                e+=1
            if e>0:
                break
            if count%2==0:
                item=input("  X - > ")
                if item!='1' and item!='2' and item!='3' and item!='4' and item!='5' and item!='6' and item!='7' and item!='8' and item!='9':
                    continue
                #switch(item)
                if item=='1':
                    if matriz[0][1]!='X' and matriz[0][1]!='O':
                        matriz[0][1]='X'
                    else:
                        continue
                if item=='2':
                    if matriz[0][5]!='X' and matriz[0][5]!='O':
                        matriz[0][5]='X'
                    else:
                        continue
                if item=='3':
                    if matriz[0][9]!='X' and matriz[0][9]!='O':
                        matriz[0][9]='X'
                    else:
                        continue
                if item=='4':
                    if matriz[2][1]!='X' and matriz[2][1]!='O':
                        matriz[2][1]='X'
                    else:
                        continue
                if item=='5':
                    if matriz[2][5]!='X' and matriz[2][5]!='O':
                        matriz[2][5]='X'
                    else:
                        continue
                if item=='6':
                    if matriz[2][9]!='X' and matriz[2][9]!='O':
                        matriz[2][9]='X'
                    else:
                        continue
                if item=='7':
                    if matriz[4][1]!='X' and matriz[4][1]!='O':
                        matriz[4][1]='X'
                    else:
                        continue
                if item=='8':
                    if matriz[4][5]!='X' and matriz[4][5]!='O':
                        matriz[4][5]='X'
                    else:
                        continue
                if item=='9':
                    if matriz[4][9]!='X' and matriz[4][9]!='O':
                        matriz[4][9]='X'
                    else:
                        continue
                    
            if count%2==1:
                item=input("  O - > ")
                if item!='1' and item!='2' and item!='3' and item!='4' and item!='5' and item!='6' and item!='7' and item!='8' and item!='9':
                    continue
                #switch(item)
                if item=='1':
                    if matriz[0][1]!='X' and matriz[0][1]!='O':
                        matriz[0][1]='O'
                    else:
                        continue
                if item=='2':
                    if matriz[0][5]!='X' and matriz[0][5]!='O':
                        matriz[0][5]='O'
                    else:
                        continue
                if item=='3':
                    if matriz[0][9]!='X' and matriz[0][9]!='O':
                        matriz[0][9]='O'
                    else:
                        continue
                if item=='4':
                    if matriz[2][1]!='X' and matriz[2][1]!='O':
                        matriz[2][1]='O'
                    else:
                        continue
                if item=='5':
                    if matriz[2][5]!='X' and matriz[2][5]!='O':
                        matriz[2][5]='O'
                    else:
                        continue
                if item=='6':
                    if matriz[2][9]!='X' and matriz[2][9]!='O':
                        matriz[2][9]='O'
                    else:
                        continue
                if item=='7':
                    if matriz[4][1]!='X' and matriz[4][1]!='O':
                        matriz[4][1]='O'
                    else:
                        continue
                if item=='8':
                    if matriz[4][5]!='X' and matriz[4][5]!='O':
                        matriz[4][5]='O'
                    else:
                        continue
                if item=='9':
                    if matriz[4][9]!='X' and matriz[4][9]!='O':
                        matriz[4][9]='O'
                    else:
                        continue
            count+=1
            
    else:
        while(count<9):
            item=''
            os.system(''+['clear', 'cls'][(os.name)=='nt'])
            print('\nJogo do Welho:\n\n')
            print("Jogada: "+str(count)+"\n\n")
            printMatriz(matriz)
            e=check_winner(matriz)
            if e!=0 and count%2==0:
                e+=1
            if e>0:
                break
            if count%2==0:
                item=input("  X - > ")
                if item!='1' and item!='2' and item!='3' and item!='4' and item!='5' and item!='6' and item!='7' and item!='8' and item!='9':
                    continue
                #switch(item)
                if item=='1':
                    if matriz[0][1]!='X' and matriz[0][1]!='O':
                        matriz[0][1]='X'
                    else:
                        continue
                if item=='2':
                    if matriz[0][5]!='X' and matriz[0][5]!='O':
                        matriz[0][5]='X'
                    else:
                        continue
                if item=='3':
                    if matriz[0][9]!='X' and matriz[0][9]!='O':
                        matriz[0][9]='X'
                    else:
                        continue
                if item=='4':
                    if matriz[2][1]!='X' and matriz[2][1]!='O':
                        matriz[2][1]='X'
                    else:
                        continue
                if item=='5':
                    if matriz[2][5]!='X' and matriz[2][5]!='O':
                        matriz[2][5]='X'
                    else:
                        continue
                if item=='6':
                    if matriz[2][9]!='X' and matriz[2][9]!='O':
                        matriz[2][9]='X'
                    else:
                        continue
                if item=='7':
                    if matriz[4][1]!='X' and matriz[4][1]!='O':
                        matriz[4][1]='X'
                    else:
                        continue
                if item=='8':
                    if matriz[4][5]!='X' and matriz[4][5]!='O':
                        matriz[4][5]='X'
                    else:
                        continue
                if item=='9':
                    if matriz[4][9]!='X' and matriz[4][9]!='O':
                        matriz[4][9]='X'
                    else:
                        continue
            if count%2==1:
                item=computer_move(log_mymove,matriz,count)
                if item!=1 and item!=2 and item!=3 and item!=4 and item!=5 and item!=6 and item!=7 and item!=8 and item!=9:
                    continue
                #switch(item)
                if item==1:
                    if matriz[0][1]!='X' and matriz[0][1]!='O':
                        matriz[0][1]='O'
                    else:
                        continue
                if item==2:
                    if matriz[0][5]!='X' and matriz[0][5]!='O':
                        matriz[0][5]='O'
                    else:
                        continue
                if item==3:
                    if matriz[0][9]!='X' and matriz[0][9]!='O':
                        matriz[0][9]='O'
                    else:
                        continue
                if item==4:
                    if matriz[2][1]!='X' and matriz[2][1]!='O':
                        matriz[2][1]='O'
                    else:
                        continue
                if item==5:
                    if matriz[2][5]!='X' and matriz[2][5]!='O':
                        matriz[2][5]='O'
                    else:
                        continue
                if item==6:
                    if matriz[2][9]!='X' and matriz[2][9]!='O':
                        matriz[2][9]='O'
                    else:
                        continue
                if item==7:
                    if matriz[4][1]!='X' and matriz[4][1]!='O':
                        matriz[4][1]='O'
                    else:
                        continue
                if item==8:
                    if matriz[4][5]!='X' and matriz[4][5]!='O':
                        matriz[4][5]='O'
                    else:
                        continue
                if item==9:
                    if matriz[4][9]!='X' and matriz[4][9]!='O':
                        matriz[4][9]='O'
                    else:
                        continue
                #switch(count)
                if count==1:
                    log_mymove[0]=item
                if count==3:
                    log_mymove[1]=item
                if count==5:
                    log_mymove[2]=item
                if count==7:
                    log_mymove[3]=item
            count+=1
            
    print_result(matriz,e,count)
    play_again=input('\nJogar Novamente? (s/n) ')
    if play_again=='n':
        break