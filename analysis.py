# Bridget LaBonney
# Project Analysis Code
# CPE 400

import numpy
import sys
import matplotlib.pyplot as plt

def giveme(name, storage, data, num):
    t = 0;
    for i in data:
        if(i == name):
            storage.append(num);
        else:
            storage.append(0);
        t = t + 1;
def dfh(des):
    plt.hist(des);
    plt.ylabel("No. of Packets");
    plt.title("Destination Frequency Histogram");
    plt.show();

def dot(des, time):
    #some data seperation is needed
    host = [];
    rem = [];
    local = [];
    con = [];
    giveme("host", host, des, 1)
    giveme("remote ()", rem, des, .7);
    giveme("localhost ()", local, des, .5);
    giveme("controller", con, des, .3);
    plt.scatter(time, host, s = .5, label = "host");
    plt.scatter(time, rem, s = .5, label = "remote()")
    plt.scatter(time, local, s = .5, label = "localhost()")
    plt.scatter(time, con, s = .5, label = "controller")
    plt.legend();
    plt.title("Destination Over Time");
    plt.axis([0, 100, .1, 1.1]);
    plt.xticks([1, 25, 50, 75, 100]);
    plt.yticks([]);
    plt.show();
    
def pfh(pro):
    plt.hist(pro);
    plt.ylabel("No. of Packets");
    plt.title("Protocol Frequency Histogram");
    plt.show();
def pot(pro, time):
    host = [];
    rem = [];
    local = [];
    con = [];
    usb = [];
    giveme("L2CAP", host, pro, 1)
    giveme("controller", rem, pro, .7);
    giveme("HCI_EVT", local, pro, .5);
    giveme("HCI_CMD", con, pro, .3);
    giveme("HCI_USB", usb, pro, .61);
    plt.scatter(time, host, s = .5, label = "L2CAP");
    plt.scatter(time, rem, s = .5, label = "controller")
    plt.scatter(time, local, s = .5, label = "HCI_EVT")
    plt.scatter(time, con, s = .5, label = "HCI_CMD")
    plt.scatter(time, usb, s = .5, label = "HCI_USB")
    plt.legend();
    plt.title("Protocols Over Time");
    plt.axis([0, 100, .1, 1.1]);
    plt.xticks([1, 25, 50, 75, 100]);
    plt.yticks([]);
    plt.show();
  
def plotim(length, time):
    plt.plot(time, length);
    plt.title("Packet Length Over Time");
    plt.axis([0, 100, 0, 15]);
    plt.xticks([1, 25, 50, 75, 100]);
    plt.yticks([]);
    plt.show();
def srd(des, info):
    t = 0;
    sent = [];
    rcvd = [];
    for i in info:
        
        if(i[0] == "R"):
            rcvd.append(des[t]);
        if(i[0] == "S"):
            sent.append(des[t]);
        t = t + 1;
    
    #now we need to count the number of each destination
    rem = 0;
    host = 0;
    local = 0;
    controller = 0;
    for i in rcvd:
        if(i == "remote ()"):
            rem = rem + 1;
        if(i == "host"):
            host = host + 1;
        if(i == "controller"):
            controller = controller + 1;
        if(i == "localhost ()"):
            local = local + 1;
    
    y = [rem, host, local, controller];
    x = [0, 4, 8, 12];
    plt.bar(x, y, label = "Recieved");
    for i in sent:
        if(i == "remote ()"):
            rem = rem + 1;
        if(i == "host"):
            host = host + 1;
        if(i == "controller"):
            controller = controller + 1;
        if(i == "localhost ()"):
            local = local + 1;
    y2 = [rem, host, local, controller];
    x2 = [16, 20, 26, 30];
    plt.bar(x2, y2, label = "Sent");
    plt.axis([0, 30, 0, 20]);
    plt.yticks([0, 10, 20]);
    plt.legend();
    plt.title("Sent and Recieved Packets Based on Destination");
    plt.xticks([0, 4, 8, 12, 16, 20, 26, 30], labels = ["remote()", "host", "localhost()", "controller", "remote()", "host", "localhost()", "controller"]);
    plt.show();

def main():
    filename = 'c:/users/bridg/Desktop/x.txt';
    file = open(filename, "r")

    # Data is pre-cleaned thanks to csv format which is converted to
    # tab delimited .txt
    #for i in d:

    p = file.readline(); #ditches title lines
    pn = [];
    time = [];
    source = [];
    des = [];
    pro = [];
    length = [];
    info = [];
    
    print("Loading data...");
    while file:
        p = file.readline();
        p = p.split('\t');
       # print(p);
        #' ' means EOF
        if(p[0] == ''):
            break;
        pn.append(p[0]);
        time.append(p[1]);
        source.append(p[2]);
        des.append(p[3]);
        pro.append(p[4]);
        length.append(p[5]);
        info.append(p[6]);

    x = 1;
    while x != '0':
        print("Analysis Menu:");
        print("1 - Destination Frequency Histogram");
        print("2 - Destinations over Time");
        print("3 - Protocol Frequency Histogram");
        print("4 - Protocol over Time");
        print("5 - Packet Length over Time");
        print("6 - Sent & Recieved Based on Destination");
        print("0 - EXIT");
        x = input("Enter your Menu Option: ");
        #scrub input
        x.strip();
        x.replace(" ", "");
        if x == '1':
            dfh(des);
        elif x == '2':
            dot(des, time);
        elif x == '3':
            pfh(pro);
        elif x == '4':
            pot(pro, time);
        elif x == '5':
            plotim(length, time);
        elif x == '6':
            srd(des, info);
        elif x != '0':
            print("Invalid input! Please try again.");
        else:
            sys.exit();
       
        
       
        

        
    
main();
main();
#data has now been gathered. analysis time!
"""
#destination of packet according to information
cvd = []; # recieved something
sent = []; #sent something
t = 0;
for i in info:
    i.split(' ');
   # print(i[0]);
    if(i[0] == "S"):
        sent.append(des[t]);
    if(i[0] == "R"):
        
#plt.hist(rcvd);
#plt.hist(length);
#plt.hist(des);
#plt.hist(source);
#plt.ylabel("No. of Packets");



con = [];
for i in des:
    
    if(i == "host"):
        con.append(i);
        
c = len(con);

#print(c)"""
