# imports
import sys,os
sys.path.append("../")
from conf.conf import *
from tk import intp as intp
from tk.intp import *
sys.path.remove("../")
g = vars(intp)

#variables

#gui
Win("win",[],
    HeaderBar("hb",[],True,
        Box("hbCenter",Vars.pks,["orientation=Vars.hori"],
            SE("hbSearch",[])
        ),
        Label("hbLabelLeft",["label='NEWS!'"])
    ),
    Box("root",Vars.pks,["orientation=Vars.vert"],
        Label("news",["label='Ive made more changes :)'"])
    )
)

#after interpret
g["hbSearch"].set_placeholder_text("Type to search")
Funcs._Class(g["hbSearch"],"hbSearch")
Funcs._Class(g["news"],"news")

Gui.__style__("./style.css")
Gui.__run__(g["win"])
