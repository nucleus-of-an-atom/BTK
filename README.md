# BTK
An easy to use "module" with HTML-like-syntax for making guis with Gtk and Python

# Getting started
Hello world app
```
# imports
import sys,os
sys.path.append("../")
from conf.conf import *
from tk import intp as intp
from tk.intp import *
sys.path.remove("../")
g = vars(intp)

#gui
Win("root",[],
  Label("lbl1",["label='Hello World!'"]),
)
Gui.__run__(g["root"])
```
Understanding the code
- Everything between #imports and #gui are necessary for the code to run. `g = vars(intp)` just allows you to get a dict with added items. You can change it if you wish, just note that if you do, you'll later access items with <custom-var>["widget_name"], and not g["widget_name"].
- Win() is a class that creates a window. It is one of the "normal widgets". Normal widgets just accept the following arguments (in chronological order): 
    - name/id to access it later (string)
    - other arguments that the Gtk widget takes in (list). For example, "label='label for a btn or lbl'"
    - items to pack in the widget
  Layout widgets (like boxes), however, take in the following arguments (in chronological order):
    - name/id to access it later (string)
    - packing arguments (list). For example, ["pack_start",True,True,0] or ["pack_end",True,False,0]
    - other arguments that the Gtk widget takes in (list). For example, "orientation='Vars.hori'" or "spacing=10"
    - items to pack in the widget

For a pre-made template,
- Clone this repository with `git clone https://github.com/nucleus-of-an-atom/BTK.git`
- Cd into the main folder in the terminal, and also open the folder with your preferred IDE/Editor
- Remove the code after the #gui part, and add your own code :)

# Getting help
There's a demo file here, to hopefully make it easier to understand. There's also another repository called "Music", from where you can have a look at a more detailed and practical application of the code. 

# Demo app
- Clone this repository with `git clone https://github.com/nucleus-of-an-atom/BTK.git`
- Cd into the main folder with `cd main` and run the python file with `python3 main.py`
