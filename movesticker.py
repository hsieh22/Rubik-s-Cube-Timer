front=['#03DD01','#03DD01','#03DD01','#03DD01','#03DD01','#03DD01','#03DD01','#03DD01','#03DD01'] #green
back=['#1100FF','#1100FF','#1100FF','#1100FF','#1100FF','#1100FF','#1100FF','#1100FF','#1100FF'] #blue
left=['#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01'] #orange
right=['#FF0100','#FF0100','#FF0100','#FF0100','#FF0100','#FF0100','#FF0100','#FF0100','#FF0100'] #red
up=['#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF'] #white
down=['#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00'] #yellow 
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



def move_as_scramble(scramble_word): 
     global front, back, left, right, up, down
     front=['#03DD01','#03DD01','#03DD01','#03DD01','#03DD01','#03DD01','#03DD01','#03DD01','#03DD01'] #green
     back=['#1100FF','#1100FF','#1100FF','#1100FF','#1100FF','#1100FF','#1100FF','#1100FF','#1100FF'] #blue
     left=['#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01','#FFAA01'] #orange
     right=['#FF0100','#FF0100','#FF0100','#FF0100','#FF0100','#FF0100','#FF0100','#FF0100','#FF0100'] #red
     up=['#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF'] #white
     down=['#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00','#FEFF00'] #yellow 

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

     for x in range(0,len(scramble_word)):#設定動作
          movement[scramble_word[x]]()
          
     stick_color=[]
     stick_color.append(up)
     stick_color.append(left)
     stick_color.append(front)
     stick_color.append(right)
     stick_color.append(back)
     stick_color.append(down)
     
     return stick_color