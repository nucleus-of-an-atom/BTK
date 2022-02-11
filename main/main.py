# imports
import sys,os
sys.path.append("../")
from conf.conf import *
from tk import intp as intp
from tk.intp import *
sys.path.remove("../")

# gui
config=read("config.conf")
btn2_lbl=find(config,"btn2","label")
btn3_lbl=find(config,"btn3","label")

Gui.__style__("style.css")
g = vars(intp)
pkg=["pack_start",True,True,0]
Win("root",[],
    Box("hbox",pkg,["orientation=Vars.hori"],
        Box("vbox1",pkg,["orientation=Vars.vert"],
            Btn("btn1",["label='btn1'"]),
        ),
        Box("vbox2",pkg,["orientation=Vars.vert","spacing=10"],
            Btn("btn2",[f"label='{btn2_lbl}'"]),
            Btn("btn3",[f"label='{btn3_lbl}'"]),
        )
    ),
)
click_count=0
def btn1_click(w):
    global click_count
    click_count+=1
    w.set_label(f"You clicked me! You clicked me {click_count} times!")
g["btn1"].connect("clicked",btn1_click)
Gui.__run__(g["root"])
