import gi
from gi.repository import Gtk
gi.require_version("Gtk", "3.0")


class Interface(Gtk.Window):
    animation_frame = Gtk.Image()
    label = Gtk.Label()

    def __init__(self):
        print("initialize interface module")
        Gtk.Window.__init__(self, title="Bot")
        Gtk.Window.set_default_size(self, 750, 500)
        Gtk.Window.set_icon_from_file(self, "bot.gif")

        self.label.set_markup("<big>Hello World!</big>")
        self.animation_frame.set_from_file("bot.gif")

        screen = Gtk.Fixed()
        screen.put(self.animation_frame, 125, 0)
        screen.put(self.label, 125, 475)
        self.add(screen)

        self.connect("destroy", Gtk.main_quit)

    def update_label(self, text):
        label_text = "<big><b>" + text + "</b></big>"
        self.label.set_markup(label_text)

    def update_animation_frame(self, widget, facefile):
        widget.set_from_file(facefile)

    def run(self):
        # self.show_all()
        Gtk.main()
