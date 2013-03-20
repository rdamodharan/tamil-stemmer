#!/usr/bin/env python
import sys
import re

import pygtk
pygtk.require('2.0')
import gtk

import popen2

class Stemmer:
    def __init__(self, argv):
        if len(argv) > 1:
            self.stemmer = argv[1]
        else:
            self.stemmer = "./stemwords"
        
    def stemWord(self,str):
        self.fin, self.fout = popen2.popen2(self.stemmer + " -l ta")
        self.fout.write(str)
        self.fout.write("\n")
        self.fout.close()
        res=self.fin.readlines()
        self.fin.close()
        return res
        

class TamilStemmerGUI:
    def __init__(self):
        self.stemmer = Stemmer(sys.argv)
        self.word_count = 0
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect('delete_event', self.delete_event)
        self.window.connect('destroy',self.destroy)
        self.window.set_title('Tamil Stemmer GUI')
        self.window.set_size_request(350,400)
       
        self.list = gtk.ListStore(int,str,str,str)
       
        self.entry = gtk.Entry()
        self.entry.connect('activate', self.add_new_row, self.list)
       
        self.tvcolumn1 = gtk.TreeViewColumn('No.')
        self.cell1 = gtk.CellRendererText()
        self.tvcolumn1.pack_start(self.cell1,True)
        self.tvcolumn1.add_attribute(self.cell1,'text',0)
        self.tvcolumn1.set_resizable(True)
        
        self.tvcolumn2 = gtk.TreeViewColumn('Word')
        self.cell2 = gtk.CellRendererText()
        self.tvcolumn2.pack_start(self.cell2,True)
        self.tvcolumn2.add_attribute(self.cell2,'text',1)
        self.tvcolumn2.set_min_width(175)
       
        self.tvcolumn3 = gtk.TreeViewColumn('Stemmed word')
        self.cell3 = gtk.CellRendererText()
        self.tvcolumn3.pack_start(self.cell3,True)
        self.tvcolumn3.add_attribute(self.cell3,'text',2)
        
        self.tview = gtk.TreeView(self.list)
        self.tview.append_column(self.tvcolumn1)
        self.tview.append_column(self.tvcolumn2)
        self.tview.append_column(self.tvcolumn3)
        self.tview.set_grid_lines(gtk.TREE_VIEW_GRID_LINES_BOTH)
       
        self.scrollwindow = gtk.ScrolledWindow()
        self.scrollwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.scrollwindow.add(self.tview)
                
        self.textview = gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textview.set_editable(False)
        self.textview.set_justification(gtk.JUSTIFY_CENTER)
        
        self.scrolledwindow2 = gtk.ScrolledWindow()
        self.scrolledwindow2.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
        self.scrolledwindow2.add(self.textview)
       
        self.vbox = gtk.VBox(False,5)
        self.vbox.pack_start(self.entry,expand=False,fill=False,padding=0)
        self.vbox.pack_start(self.scrollwindow,expand=True,fill=True,padding=0)
        self.vbox.pack_start(self.scrolledwindow2,expand=True,fill=True,padding=0)
       
        self.window.add(self.vbox)
        self.window.show_all()
       
    def delete_event(self,widget,event,data=None):
        return False
   
    def destroy(self,widget,data=None):
        gtk.main_quit()
                  
    def add_new_row(self, entry, list):
        text = entry.get_text()
        res = self.stemmer.stemWord(text)
        pattern = re.compile(r"(^.*?: \[\d+\]|[{\[\]\|#}'])")
        stem = res.pop().strip("\n")
        newres = ""
        for i in res:
            newres = newres + i #pattern.sub('',i)
        self.word_count += 1
        list.append((self.word_count,text, stem ,newres))
        self.textbuffer.set_text(newres)
        entry.set_text("")
        return True
   
    def main(self):
        gtk.main()
       
   
if __name__ == "__main__":
    app = TamilStemmerGUI()
    app.main()
