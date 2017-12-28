import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

import os

class Sweep(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Sweep")
        self.set_size_request(600, 400)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.button = Gtk.Button()
        self.button.set_label("Sweep")
        self.button.connect("clicked", self.on_clicked)
        vbox.pack_start(self.button, False, False, 0)

    def on_clicked(self, *args):
        home = os.path.expanduser('~')
        base = os.path.join(home,'.config','google-chrome','Default')
        for filename in ['History', 'History-journal']:
            os.remove(os.path.join(base, filename))

win = Sweep()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
