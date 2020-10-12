__version__ = '0.1.0'

from gi.repository import Gio, GLib


def upload(file, collector, metadata):
    """
    upload sends a message on the system DBus to com.redhat.yggdrasil1, invoking
    the com.redhat.yggdrasil1.Upload method and returns the response.
    """
    bus = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)
    proxy = Gio.DBusProxy.new_sync(bus, Gio.DBusProxyFlags.NONE, None,
                                   "com.redhat.yggdrasil1",
                                   "/com/redhat/yggdrasil1",
                                   "com.redhat.yggdrasil1", None)
    res = proxy.call_sync(
        "Upload",
        GLib.Variant("(ssa{sv})", (file, collector, metadata)),
        Gio.DBusCallFlags.NO_AUTO_START, -1, None)
    return res.unpack()[0]
