#python gifs.py >/dev/null
import subprocess, time, random, os, multiprocessing;
from PIL import Image;
from PyQt5 import QtWidgets, QtCore, QtGui;


def do_thing(filename, width, height):
    app = QtWidgets.QApplication(["v"]);
    win = QtWidgets.QMainWindow();
    
    win.setAttribute(QtCore.Qt.WA_ShowWithoutActivating); #stops new window from stealing focus
    win.setFocusPolicy(QtCore.Qt.NoFocus); #does this do anything?
    win.setWindowFlags(QtCore.Qt.WindowStaysOnBottomHint | QtCore.Qt.FramelessWindowHint); #window always in back and no title bar
    win.resize(width, height);
    win.move(100,100);

    label = QtWidgets.QLabel(win); #label in window
    display = QtGui.QMovie(os.getcwd() + "/" + filename); #display gif
    label.setMovie(display);
    label.resize(width,height);
    
    setting = QtCore.QSettings();
    setting.setValue("key",1);
    
    #actually show everything on screen
    win.show();
    label.show();
    display.start();
    app.exec();
#do_thing("tumblr_mstgs7dxe91rdu90go1_1280.webp", 1000, 1000);
#"""
list_master = os.listdir();
list_master.remove("gifs.py"); list_master.remove("5iZDULY.mp4"); #remove problem files
list_temp = list(list_master);

while(True):
    filename = random.choice(list_temp);
    #print(filename);
    list_temp.remove(filename); #remove previous file from list so it dosnt play again too soon
    width, height = Image.open(os.getcwd() + "/" + filename).size;
    
    thread = multiprocessing.Process(target=do_thing, args=(filename,width,height,)); #open gif in separate thread so main loop can keep running
    thread.daemon = True;
    thread.start();
    
    time.sleep(5);
    thread.kill(); #merc the thread
    thread.join();
    if(not list_temp):
        list_temp = list(list_master); #rest list if empty
#"""
