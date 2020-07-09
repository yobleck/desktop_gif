#python gifs.py >/dev/null
import subprocess, time, random, os, multiprocessing;
from PIL import Image;
from PyQt5 import QtWidgets, QtCore, QtGui;
import sys, select, tty, termios; #https://www.darkcoding.net/software/non-blocking-console-io-is-not-possible/


def do_thing(filename, width, height):
    app = QtWidgets.QApplication(["v"]);
    win = QtWidgets.QMainWindow();
    
    win.setAttribute(QtCore.Qt.WA_ShowWithoutActivating); #stops new window from stealing focus
    win.setFocusPolicy(QtCore.Qt.NoFocus); #does this do anything?
    win.setWindowFlags(QtCore.Qt.WindowStaysOnBottomHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool); #window always behind,no title bar/taskbar icon
    win.resize(width, height);
    win.move(100,0);

    label = QtWidgets.QLabel(win); #label in window
    display = QtGui.QMovie(os.getcwd() + "/" + filename); #display gif
    label.setMovie(display); #TODO: speed too fast
    label.resize(width,height);
    #TODO: hide taskbar icon
    #actually show everything on screen
    win.show();
    label.show();
    display.start();
    app.exec();
#do_thing("tumblr_mstgs7dxe91rdu90go1_1280.webp", 1000, 1000);

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []);
old_settings = termios.tcgetattr(sys.stdin);

#"""
list_master = os.listdir();
list_master.remove("gifs.py"); list_master.remove("5iZDULY.mp4"); #remove problem files
list_temp = list(list_master);

try:
    tty.setcbreak(sys.stdin.fileno());
    
    time_to_switch = True; timer = time.perf_counter();
    while(True):
        if(time_to_switch): #show gif
            filename = random.choice(list_temp);
            #print(filename);
            list_temp.remove(filename); #remove previous file from list so it dosnt play again too soon
            width, height = Image.open(os.getcwd() + "/" + filename).size;
            
            thread = multiprocessing.Process(target=do_thing, args=(filename,width,height,)); #open gif in separate thread so main loop can keep running
            thread.daemon = True;
            thread.start();
            time_to_switch = False;
            
        if(not list_temp):
            list_temp = list(list_master); #reset list if empty
        
        if(time.perf_counter()-timer > 300): #change to new gif after time elapses
            timer = time.perf_counter();
            thread.kill(); #merc the thread
            thread.join();
            time_to_switch = True;
        
        if(isData()):
            c = sys.stdin.read(1);
            if(c == "\x1b"): #esc key
                thread.kill(); #merc the thread
                thread.join();
                break;
        time.sleep(.01);
finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings);
#"""
