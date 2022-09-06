#方塊初始化
front=['g','g','g','g','g','g','g','g','g']
back=['b','b','b','b','b','b','b','b','b']
left=['o','o','o','o','o','o','o','o','o']
right=['r','r','r','r','r','r','r','r','r']
up=['w','w','w','w','w','w','w','w','w']
down=['y','y','y','y','y','y','y','y','y']
changea=''
changeb=''
changec=''
changed=''

#定義打亂函式
def scramble3():
     import random
     moves = [1, 2, 11 , 12 , 21 , 22]
     director = ["" , "'" , "2"]
     lengh = random.randint(18, 21)


     #隨機打亂
     scmoves = []
     scdir = []
     for x in range(lengh):
          scmoves.append(random.choice(moves))
          scdir.append(random.choice(director))

     #檢查不合情況
     for x in range(1, lengh):
          if scmoves[x] == scmoves[x-2] or scmoves[x] == scmoves[x-1]:
               while scmoves[x] == scmoves[x-1] or abs(scmoves[x] - scmoves[x-1]) == 1:
                    scmoves[x] = random.choice(moves)
                         
     #資料整理
     letter = {1:'R', 2:'L', 11:'U', 12:'D', 21:'F', 22:'B'}
     scletter = [letter[x] if x in letter else x for x in scmoves]
     rescmove=[]
     for x in range(lengh):
          rescmove.append(scletter[x] + scdir[x])
     #印出打亂     
     for x in range(lengh):
          print(rescmove[x] ,end=' ')
     print()
     print('-----')  
     #回傳打亂
     return rescmove

#定義動作
def F():
     changea=front[0]
     changeb=front[2]
     changec=front[8]
     changed=front[6]
     front[0]=changed
     front[2]=changea
     front[8]=changeb
     front[6]=changec

     changea=front[1]
     changeb=front[3]
     changec=front[5]
     changed=front[7]
     front[3]=changed
     front[5]=changea
     front[1]=changeb
     front[7]=changec

     changea=up[6]
     changeb=right[0]
     changec=down[2]
     changed=left[8]
     right[0]=changea
     down[2]=changeb
     left[8]=changec
     up[6]=changed

     changea=up[7]
     changeb=right[3]
     changec=down[1]
     changed=left[5]
     right[3]=changea
     down[1]=changeb
     left[5]=changec
     up[7]=changed

     changea=up[8]
     changeb=right[6]
     changec=down[0]
     changed=left[2]
     right[6]=changea
     down[0]=changeb
     left[2]=changec
     up[8]=changed
def B():
     changea=back[0]
     changeb=back[2]
     changec=back[8]
     changed=back[6]
     back[0]=changed
     back[2]=changea
     back[8]=changeb
     back[6]=changec

     changea=back[1]
     changeb=back[3]
     changec=back[5]
     changed=back[7]
     back[3]=changed
     back[5]=changea
     back[1]=changeb
     back[7]=changec

     changea=up[2]
     changeb=left[0]
     changec=down[6]
     changed=right[8]
     left[0]=changea
     down[6]=changeb
     right[8]=changec
     up[2]=changed

     changea=up[1]
     changeb=left[3]
     changec=down[7]
     changed=right[5]
     left[3]=changea
     down[7]=changeb
     right[5]=changec
     up[1]=changed

     changea=up[0]
     changeb=left[6]
     changec=down[8]
     changed=right[2]
     left[6]=changea
     down[8]=changeb
     right[2]=changec
     up[0]=changed
def L():
     changea=left[0]
     changeb=left[2]
     changec=left[8]
     changed=left[6]
     left[0]=changed
     left[2]=changea
     left[8]=changeb
     left[6]=changec

     changea=left[1]
     changeb=left[3]
     changec=left[5]
     changed=left[7]
     left[3]=changed
     left[5]=changea
     left[1]=changeb
     left[7]=changec

     changea=up[0]
     changeb=front[0]
     changec=down[0]
     changed=back[8]
     front[0]=changea
     down[0]=changeb
     back[8]=changec
     up[0]=changed

     changea=up[3]
     changeb=front[3]
     changec=down[3]
     changed=back[5]
     front[3]=changea
     down[3]=changeb
     back[5]=changec
     up[3]=changed

     changea=up[6]
     changeb=front[6]
     changec=down[6]
     changed=back[2]
     front[6]=changea
     down[6]=changeb
     back[2]=changec
     up[6]=changed
def R():
     changea=right[0]
     changeb=right[2]
     changec=right[8]
     changed=right[6]
     right[0]=changed
     right[2]=changea
     right[8]=changeb
     right[6]=changec

     changea=right[1]
     changeb=right[3]
     changec=right[5]
     changed=right[7]
     right[3]=changed
     right[5]=changea
     right[1]=changeb
     right[7]=changec

     changea=up[8]
     changeb=back[0]
     changec=down[8]
     changed=front[8]
     back[0]=changea
     down[8]=changeb
     front[8]=changec
     up[8]=changed

     changea=up[5]
     changeb=back[3]
     changec=down[5]
     changed=front[5]
     back[3]=changea
     down[5]=changeb
     front[5]=changec
     up[5]=changed

     changea=up[2]
     changeb=back[6]
     changec=down[2]
     changed=front[2]
     back[6]=changea
     down[2]=changeb
     front[2]=changec
     up[2]=changed
def U():

     changea=up[0]
     changeb=up[2]
     changec=up[8]
     changed=up[6]
     up[0]=changed
     up[2]=changea
     up[8]=changeb
     up[6]=changec

     changea=up[1]
     changeb=up[3]
     changec=up[5]
     changed=up[7]
     up[3]=changed
     up[5]=changea
     up[1]=changeb
     up[7]=changec

     changea=back[2]
     changeb=right[2]
     changec=front[2]
     changed=left[2]
     right[2]=changea
     front[2]=changeb
     left[2]=changec
     back[2]=changed

     changea=back[1]
     changeb=right[1]
     changec=front[1]
     changed=left[1]
     right[1]=changea
     front[1]=changeb
     left[1]=changec
     back[1]=changed

     changea=back[0]
     changeb=right[0]
     changec=front[0]
     changed=left[0]
     right[0]=changea
     front[0]=changeb
     left[0]=changec
     back[0]=changed
def D():

     changea=down[0]
     changeb=down[2]
     changec=down[8]
     changed=down[6]
     down[0]=changed
     down[2]=changea
     down[8]=changeb
     down[6]=changec

     changea=down[1]
     changeb=down[3]
     changec=down[5]
     changed=down[7]
     down[3]=changed
     down[5]=changea
     down[1]=changeb
     down[7]=changec

     changea=back[6]
     changeb=right[6]
     changec=front[6]
     changed=left[6]
     right[6]=changec
     front[6]=changed
     left[6]=changea
     back[6]=changeb

     changea=back[7]
     changeb=right[7]
     changec=front[7]
     changed=left[7]
     right[7]=changec
     front[7]=changed
     left[7]=changea
     back[7]=changeb

     changea=back[8]
     changeb=right[8]
     changec=front[8]
     changed=left[8]
     right[8]=changec
     front[8]=changed
     left[8]=changea
     back[8]=changeb

def antiF():
     for _ in range(0,3):
          F()
def antiB():
     for _ in range(0,3):
          B()
def antiL():
     for _ in range(0,3):
          L()
def antiR():
     for _ in range(0,3):
          R()
def antiU():
     for _ in range(0,3):
          U()
def antiD():
     for _ in range(0,3):
          D()

def doubleF():
     for _ in range(0,2):
          F()
def doubleB():
     for _ in range(0,2):
          B()
def doubleL():
     for _ in range(0,2):
          L()
def doubleR():
     for _ in range(0,2):
          R()
def doubleU():
     for _ in range(0,2):
          U()
def doubleD():
     for _ in range(0,2):
          D()

movement={"F":F,
          "B":B,
          "L":L,
          "R":R,
          "U":U,
          "D":D,
          "F'":antiF,
          "B'":antiB,
          "L'":antiL,
          "R'":antiR,
          "U'":antiU,
          "D'":antiD,
          "F2":doubleF,
          "B2":doubleB,
          "L2":doubleL,
          "R2":doubleR,
          "U2":doubleU,
          "D2":doubleD,}
#設定動作
scmove=scramble3()
for x in range(0,len(scmove)):
     movement[scmove[x]]()
print('')
print(up)
print(left)
print(front)
print(right)
print(back)
print(down)

def printcube():
     print(
                                                            "    " + up[0] + up[1] + up[2] + "\n" +
                                                            "    " + up[3] + "w" + up[5] + "\n" +
                                                            "    " + up[6] + up[7] + up[8] + "\n\n" +
                    left[0] + left[1] + left[2] + " " + front[0] + front[1] + front[2] + " " + right[0] + right[1] + right[2] + " " + back[0] + back[1] + back[2] + "\n" +
                    left[3] + "o" + left[5] + " " + front[3] + "g" + front[5] + " " + right[3] + "r" + right[5] + " " + back[3] + "b" + back[5] + "\n" +
                    left[6] + left[7] + left[8] + " " + front[6] + front[7] + front[8] + " " + right[6] + right[7] + right[8] + " " + back[6] + back[7] + back[8] + "\n\n" +
                                                            "    " + down[0] + down[1] + down[2] + "\n" +
                                                            "    " + down[3] + "y" + down[5] + "\n" +
                                                            "    " + down[6] + down[7] + down[8] + "\n"
                )

printcube()