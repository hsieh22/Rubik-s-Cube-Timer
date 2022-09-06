import scramble
import movesticker
import tkinter as tk
import csv
import os
from datetime import datetime
import time

#基本視窗
win = tk.Tk()
win.title('Random Scramble Generator')
win.geometry('850x650')
win.config(background = '#323232')

time_list = []
sc_list = []   

#顯示打亂圖形
labelList = []
def draw_scramble():

    stikers = movesticker.move_as_scramble(sc)
    
    for k in range(6):
        for i in range(3):
            for j in range(3):
                xstart = 500
                ystart = 400
                num = 9 * k + 3 * i + j + 1
                var = 'L' + str(num)
                var = tk.Label(text='    ',bg=stikers[k][i*3+j])
                if k == 0:
                    var.place(x=(j+3)*26+4+xstart,y=i*25+ystart)
                elif k <= 4:
                    var.place(x=(j+3*(k-1))*26+4*(k-1)+xstart,y=(i+3)*25+4+ystart)
                elif k == 5:
                    var.place(x=(j+3)*26+4+xstart,y=(i+6)*25+4*2+ystart)
                labelList.append(var)
                
#隱藏打亂圖形
def hide_draw_scramble():   
    for i in range(0,len(labelList)):
        labelList[i].place_forget()

sc = scramble.scramble3()   #一打開就產生第一組sc
draw_scramble() #一打開就顯示第一次打亂圖形

#產生新打亂
def gen_sc():
    global sc
    sc = scramble.scramble3()   #從scramble程式產生sc,sc為一陣列,如['R',"U'",'L',...]
    sc_btn.config(text = sc)    #將sc_btn的文字設定為sc
    draw_scramble() #更新打亂圖形

#設置物件
sc_btn = tk.Button(text = sc , fg = 'white', highlightbackground = '#000000',highlightthickness = 0,font = 'Arial 30' ) #顯示打亂,按下則產生新打亂
sc_btn.pack(anchor='n')

solve_show = tk.Label(text = 'solve: 0', fg = 'white', bg = '#323232',font = 'Arial 30')    #顯示為第幾次復原
solve_show.place(x=30, y=180)

mo3_show = tk.Label(text = 'mo3 ----', fg = 'white', bg = '#323232',font = 'Arial 30')  #顯示mo3
mo3_show.place(x=30, y=220)

ao5_show = tk.Label(text = 'ao5 ----', fg = 'white', bg = '#323232',font = 'Arial 30')  #顯示ao5
ao5_show.place(x=30, y=260)

ao12_show = tk.Label(text = 'ao12 ----', fg = 'white', bg = '#323232',font = 'Arial 30')    #顯示ao12
ao12_show.place(x=30, y=300)

mean_show = tk.Label(text = 'mean ----', fg = 'white', bg = '#323232',font = 'Arial 30')    #顯示mean
mean_show.place(x=30, y=340)

time_1_show = tk.Button(fg = 'white', highlightbackground = '#000000',highlightthickness = 0,font = 'Arial 30') #顯示上一次時間,按下則print出該次sc
time_1_show.place(x=30, y=400)

time_2_show = tk.Button(fg = 'white', highlightbackground = '#000000',highlightthickness = 0,font = 'Arial 30') #顯示上上次時間,按下則print出該次sc
time_2_show.place(x=30, y=445)

time_3_show = tk.Button(fg = 'white', highlightbackground = '#000000',highlightthickness = 0,font = 'Arial 30')
time_3_show.place(x=30, y=490)

time_4_show = tk.Button(fg = 'white', highlightbackground = '#000000',highlightthickness = 0,font = 'Arial 30')
time_4_show.place(x=30, y=535)  

time_5_show = tk.Button(fg = 'white', highlightbackground = '#000000',highlightthickness = 0,font = 'Arial 30')
time_5_show.place(x=30, y=580)

plus_two_btn = tk.Button(text = '+2', fg = 'white', highlightbackground = '#000000',highlightthickness = 0,font = 'Arial 20')   #計時完按下則該次時間+2,再按一下取消
plus_two_btn.place(x=420, y=270)

dnf_btn = tk.Button(text = 'DNF', fg = 'white', highlightbackground = '#000000',highlightthickness = 0,font = 'Arial 20')   #計時完按下則該次為DNF,再按一下取消
dnf_btn.place(x=410, y=310)

def hide_object():
        sc_btn.pack_forget()    #隱藏sc
        solve_show.place_forget()   #隱藏第幾次復原
        mo3_show.place_forget()     #隱藏mo3
        ao5_show.place_forget()     #隱藏ao5 
        ao12_show.place_forget()    #隱藏ao12  
        mean_show.place_forget()    #隱藏mean    
        time_1_show.place_forget()  #隱藏過去五次成績
        time_2_show.place_forget()
        time_3_show.place_forget()
        time_4_show.place_forget()  
        time_5_show.place_forget()
        plus_two_btn.place_forget()     #隱藏+2按鈕
        dnf_btn.place_forget()      #隱藏DNF按鈕
        export.place_forget()   #隱藏export按鈕
        hide_draw_scramble()    #隱藏打亂圖形

def show_object():
        sc_btn.pack(anchor='n')     #顯示sc
        solve_show.place(x=30, y=180)   #顯示第幾次復原
        mo3_show.place(x=30, y=220)     #顯示mo3
        ao5_show.place(x=30, y=260)     #顯示ao5 
        ao12_show.place(x=30, y=300)    #顯示ao12  
        mean_show.place(x=30, y=340)    #顯示mean
        time_1_show.place(x=30, y=400)  #顯示過去五次成績
        time_2_show.place(x=30, y=445)
        time_3_show.place(x=30, y=490)
        time_4_show.place(x=30, y=535)  
        time_5_show.place(x=30, y=580)
        plus_two_btn.place(x=420, y=270)    #顯示+2按鈕
        dnf_btn.place(x=410, y=310)     #顯示DNF按鈕
        export.place(x=380,y=350)       #顯示export按鈕



#碼表 
t_ms = 0 #運行時間
t_s = 0
t_m = 0
time_show = tk.Label(text = '%02d.%02d' % (t_s, t_ms),fg='white',bg = '#323232',font = 'Arial 120') #一打開就顯示時間
time_show.place(x=280,y=100)

#開始計時
run = 2 #計算mean時避免/0
after_cancel = None
press_plus2 = 0
press_dnf = 0
time_start = None

def space_trigger(x):
    global run, t_m,t_ms,t_s ,press_plus2 ,press_dnf,time_start
    press_plus2 = press_dnf = 0
    
    if run %2 == 0:      #計時開始&歸零  
        t_ms = 0
        t_s = 0
        t_m = 0
        run += 1
        time_start = time.time()    #記錄開始時間
        timer_start()   #觸發碼表
        hide_object()   #隱藏物件

    else:       #計時結束
        time_list.append(t_ms)
        sc_list.append(sc)
        calculate_ao5(int(run/2))
        calculate_mo3(int(run/2))
        calculate_ao12(int(run/2))
        calculate_mean(int(run/2))
        time_list_show(int(run/2))
        solve_show.config(text = 'solve: ' + str(int(run/2)))
        
        gen_sc()    #產生新打亂、同時繪製新圖形
        show_object()   #顯示物件
        
        run += 1
        timer_stop()


def timer_start():  #碼表開始運行
    global  t_ms , after_cancel                                  
    time_now = time.time()  #當下時間
    t_ms = (time_now - time_start)*1000     #開始時間 - 當下時間 = 經過秒數
    time_show.config(text = time_translation(t_ms, t_s, t_m))   #改成用time_translate 
    after_cancel = win.after(1,timer_start) #每個1ms呼叫自身
    
def timer_stop():   #碼表停止
    global after_cancel
    win.after_cancel(after_cancel)
    after_cancel = None 

def time_translation(ms, s, m): #將ms轉換成m,s,ms
    while ms >= 1000:
        s = s + 1
        ms -= 1000
    while s >= 60:
        m = m + 1
        s -= 60  
    if m > 0 :
        return str(m) + ':' + "%02d" % s + '.' + "%03d" % ms   
    else:
        return str(s) + '.' + "%03d" % ms

def calculate_ao5(n):
    if n >= 5:
        ao5 = int((sum(time_list[n-5:n]) - max(time_list[n-5:n]) - min(time_list[n-5:n])) / 3)
        if ao5 < 0 :
            ao5_show.config(text = 'ao5: DNF' )
        else:
            ao5_show.config(text = 'ao5: ' + str(time_translation(ao5,0,0)) )

def calculate_mo3(n):
    if n >= 3:
        mo3 = int(sum(time_list[n-3:n]) / 3)
        if mo3 < 0 :
            mo3_show.config(text = 'mo3: DNF' )
        else:
            mo3_show.config(text = 'mo3: ' + str(time_translation(mo3,0,0)) )

def calculate_ao12(n):
    if n >= 12:
        ao12 = int((sum(time_list[n-12:n]) - max(time_list[n-12:n]) - min(time_list[n-12:n])) / 10)
        if ao12 < 0 :
            ao12_show.config(text = 'ao12: DNF' )
        else:
            ao12_show.config(text = 'ao12: ' + str(time_translation(ao12,0,0)) )


def calculate_mean(n):
    mean_list = []
    for i in range(0 , n):
        if time_list[i] >= 0 :
            mean_list.append(time_list[i])
    if len(mean_list) == 0 :
        mean_show.config(text = 'mean: DNF')
    else: 
        mean = int(sum(mean_list[0:i+1]) / len(mean_list))
        mean_show.config(text = 'mean: ' + str(time_translation(mean,0,0)) )

def time_list_show(n):
    if n >= 5:
        if time_list[n-5] < 0 :
             time_5_show.config(text = 'DNF')
        else:    time_5_show.config(text = time_translation(time_list[n-5],0,0))
    if n >= 4:
        if time_list[n-4] < 0 :
             time_4_show.config(text = 'DNF')
        else:    time_4_show.config(text = time_translation(time_list[n-4],0,0))
    if n >= 3:
        if time_list[n-3] < 0 :
             time_3_show.config(text = 'DNF')
        else:    time_3_show.config(text = time_translation(time_list[n-3],0,0))
    if n >= 2:
        if time_list[n-2] < 0 :
             time_2_show.config(text = 'DNF')
        else:    time_2_show.config(text = time_translation(time_list[n-2],0,0))
    if n >= 1:
        if time_list[n-1] < 0 :
             time_1_show.config(text = 'DNF')
        else:    time_1_show.config(text = time_translation(time_list[n-1],0,0))


def show_sc(x):     #按下按鈕顯示打亂步驟 x = 第幾個
    n = int(run/2)-1
    print(time_translation(time_list[n-x],0,0),end=' ')
    for i in range(len(sc_list[n-x])):
        print(sc_list[n-x][i] ,end=' ')
    print()

def plus_two():
    global press_plus2
    press_plus2 += 1
    n = int(run/2)-1
    if press_plus2 % 2 == 1 :
        time_list[n-1] += 2000
    else:
        time_list[n-1] -= 2000
    calculate_ao5(n)
    calculate_ao12(n)
    calculate_mean(n)
    calculate_mo3(n)
    time_list_show(n)

def dnf():
    global press_dnf
    press_dnf += 1 
    n = int(run/2)-1
    if press_dnf % 2 == 1 :
        time_list[n-1] -=  10000000
    else:
        time_list[n-1] +=  10000000
    calculate_ao5(n)
    calculate_ao12(n)
    calculate_mean(n)
    calculate_mo3(n)
    time_list_show(n)

#偵測開始、結束計時
win.bind('<KeyRelease>', space_trigger)

#按鈕執行函式
sc_btn.config(command = gen_sc)
time_1_show.config(command = lambda: show_sc(1))    #預設tkinter Button控制的函數不可有參數
time_2_show.config(command = lambda: show_sc(2))    #若需參數要在函數前加 lambda:
time_3_show.config(command = lambda: show_sc(3))
time_4_show.config(command = lambda: show_sc(4))
time_5_show.config(command = lambda: show_sc(5))
plus_two_btn.config(command = plus_two)
dnf_btn.config(command = dnf)

#輸出資料
def export_csv():
    #開啟輸出的 CSV 檔案
    datetime_dt = datetime.today()
    file_name = str(os.getcwd())+'//Downloads//TimeOutput_' + str(datetime_dt.strftime("%Y_%m_%d_%H_%M_%S")) + '.csv' 
    with open(file_name, 'w', newline='') as csvFile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvFile)
        #標題
        writer.writerow(['No.','Time','Scramble'])
  
        for i in range(0,len(time_list)):
            t = time_translation(time_list[i],0,0)
            writer.writerow([str(i+1),t,sc_list[i]])

export = tk.Button(text = 'Export CSV' , fg = 'white', highlightbackground = '#000000',highlightthickness = 0,font = 'Arial 20')
export.config(command = export_csv)
export.place(x=380,y=350)
                   
#常駐主視窗
win.attributes('-topmost', True)
win.mainloop()