import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
# from gi.repository import Gdk

from sugar3.graphics.icon import Icon
from sugar3.graphics import style
import editfonts.globals as globals


class PageHeading(Gtk.Alignment):
    def __init__(self, heading="", fontSize='40000'):

        super(PageHeading, self).__init__(xalign=0,
                                          yalign=0.5,
                                          xscale=0,
                                          yscale=0)

        # Making the Page Heading
        self.headingBox = Gtk.Box()

        HEADING_STRING = "<span foreground='black' size='{}' font='Cantarell' \
        font_weight='medium'>{}</span>".format(fontSize, heading)

        self.pageHeading = Gtk.Label()
        self.pageHeading.set_markup(HEADING_STRING)
        self.headingBox.add(self.pageHeading)
        self.add(self.headingBox)


class ImageButton(Gtk.Button):
    """
    This is just a button with a image inside it
    """

    def __init__(self, icon_name,
                 stroke_color=globals.USER_COLOR[0],
                 fill_color=globals.USER_COLOR[1],
                 bg_color=globals.ACTIVITY_BG,
                 pixel_size=82.5):

        super(ImageButton, self).__init__()
        self.icon = Icon(icon_name=icon_name,
                         pixel_size=style.zoom(pixel_size),
                         stroke_color=style.Color(stroke_color)
                         .get_svg(),
                         fill_color=style.Color(fill_color).get_svg())

        self.set_image(self.icon)
        self.props.relief = Gtk.ReliefStyle.NONE
        self.modify_bg(Gtk.StateType.NORMAL,
                       style.Color(bg_color).get_gdk_color())

    def get_icon(self):
        return self.icon


class DisplayData(Gtk.Alignment):
    def __init__(self,
                 heading=None,
                 text=None,
                 headingSize='15000',
                 textSize='10000'):
        super(DisplayData, self).__init__(xalign=0,
                                          yalign=0.5,
                                          xscale=0,
                                          yscale=0)

        self.box = Gtk.VBox()

        if heading is None:
            self.heading = ''
        else:
            self.heading = heading

        if text is None:
            self.text = ''
        else:
            self.text = text

        # FIXME: Use MarkupLabel below # noqa
        HEADING_STRING = "<span foreground='black' size='{}' font='Cantarell' \
        font_weight='bold'>{}</span>".format(headingSize, self.heading)
        TEXT_STRING = "<span foreground='black' size='{}' font='Cantarell'>\
        {}</span>".format(textSize, self.text)

        self.headingLable = Gtk.Label()
        self.headingLable.set_markup(HEADING_STRING)
        self.headingLable.set_alignment(0, 0.5)

        self.textLable = Gtk.Label()
        self.textLable.set_markup(TEXT_STRING)
        self.textLable.set_alignment(0, 0.5)

        # buffer = Gtk.TextBuffer()
        # buffer.set_markup(TEXT_STRING)
        # self.textView = Gtk.TextView(buffer)

        self.box.pack_start(self.headingLable, False, False, 5)
        self.box.pack_start(self.textLable, False, False, 5)
        self.add(self.box)
        self.show_all()

# Making a font info box


class FontInfoBox(Gtk.VBox):
    """
    Add all the info that needs to be displayed for the current selected font
    """

    def __init__(self, font):
        super(FontInfoBox, self).__init__()

        # Specify the info to be displayed
        fontName = DisplayData("Name", font.info.familyName)
        self.pack_start(fontName, False, False, 5)

        fontVersion = DisplayData("Version", str(font.info.versionMajor) +
                                  "." + str(font.info.versionMinor))
        self.pack_start(fontVersion, False, False, 5)

        fontTrademark = DisplayData("Trademark", font.info.trademark)
        self.pack_start(fontTrademark, False, False, 5)


class MarkupLabel(Gtk.Label):
    """
    Create a label with markup format as arguments
    """
    def __init__(self, text, color='black', size='10000', font='Cantarell',
                 weight='medium'):
        super(MarkupLabel, self).__init__()

        string = "<span foreground='{}' size='{}' font='{}' \
        font_weight='{}'>{}</span>".format(color, size, font, weight, text)

        self.set_markup(string)


class FormatLabel(MarkupLabel):
    """
    Create a label with a preset style
    """
    def __init__(self, text, style):
        super(FormatLabel, self).__init__(text,
                                          color=style['color'],
                                          size=style['size'],
                                          font=style['font'],
                                          weight=style['weight'])
