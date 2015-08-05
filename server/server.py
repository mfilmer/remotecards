#from twisted.internet import gtk3reactor
#gtk3reactor.install()

#from twisted.internet import reactor

from gi.repository import Gtk
from gi.repository import Gdk

class EventHandler(object):
    def gtk_main_quit(self, *args):
        Gtk.main_quit(*args)
    
    def hide_window(self, window, *args):
        window.hide()
        return True
    
    def on_startbutton_clicked(self, *args):
        print "starting"
    
    def on_chatbutton_clicked(self, *args):
        chatwindow = builder.get_object("chatwindow")
        chatwindow.show_all()
    
    def on_chatentryview_key_press_event(self, widget, event):
        if event.keyval == 65293 and not event.state & Gdk.ModifierType.SHIFT_MASK:
            print "sending"
            return True
        
    #def on_playerstreeview_selection_changed(self, *args):
    #    print "selected I guess"

builder = Gtk.Builder()
builder.add_from_file("maingui.glade")

mainwindow = builder.get_object("mainwindow")
mainwindow.show_all()

#chatwindow = builder.get_object("chatwindow")
#chatwindow.show_all()

builder.connect_signals(EventHandler())


store = Gtk.ListStore(str)
store.append(["first"])
store.append(["second"])
store.append(["third"])
store.append(["first"])
store.append(["second"])
store.append(["third"])
store.append(["first"])
store.append(["second"])
store.append(["third"])
store.append(["first"])
store.append(["second"])
store.append(["third"])
store.append(["first"])
store.append(["second"])
store.append(["third"])


playerstreeview = builder.get_object("playerstreeview")
playerstreeview.set_model(store)

renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Title", renderer, text=0)
playerstreeview.append_column(column)


Gtk.main()
