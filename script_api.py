import System
import structure_form as sf


class Node:
    """Wraps the contained elements with a start and end node."""
    def __init__(self, name, expand=False):
        self.name = name
        self.expand = expand

    def __enter__(self):
        sf.StartNode(self.name)

    def __exit__(self, exc_type, exc_value, traceback):
        sf.EndNode(self.expand)


def add_byte(name):
    """Adds unsigned byte as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.Byte](name)


def add_sbyte(name):
    """Adds signed byte as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.SByte](name)


def add_ushort(name):
    """Adds unsigned short as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.UInt16](name)


def add_short(name):
    """Adds signed short as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.Int16](name)


def add_uint(name):
    """Adds unsigned int as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.UInt32](name)


def add_int(name):
    """Adds signed int as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.Int32](name)


def add_ulong(name):
    """Adds unsigned long as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.UInt64](name)


def add_long(name):
    """Adds signed long as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.Int64](name)


def add_float(name):
    """Adds single-precision float as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.Single](name)


def add_double(name):
    """Adds double-precision float as a field with given name to the structure view, and returns the value."""
    return sf.Add[System.Double](name)


def add_bool(name):
    """
    Adds 1 byte bool as a field with given name to the structure view, and returns the value.
    - false when byte is 0, true otherwise
    """
    return sf.Add[System.Boolean](name)


def add_str(name):
    """
    Adds a 1-byte/character string preceded by its length as a short, and returns the value
    - Format: [NN NN] [SS SS ...]
    """
    with Node(name):
        size = sf.Add[System.Int16]('size')
        data = sf.AddField(name, size)
        return System.Text.Encoding.UTF8.GetString(data, 0, size)


def add_unicode_str(name):
    """
    Adds a 2-byte/character string preceded by its length as a short, and returns the value.
    - Format: [NN NN] [SSSS SSSS ...]
    """
    with Node(name):
        size = sf.Add[System.Int16]('size') * 2
        data = sf.AddField(name, size)
        return System.Text.Encoding.Unicode.GetString(data, 0, size)


def add_field(name, length=0):
    """Adds a field with given name and length to the structure view, and returns System.Byte[]."""
    sf.AddField(name, length)


def remaining():
    """Returns the number of bytes remaining unprocessed in the packet."""
    return sf.Remaining()


def start_node(name):
    """Adds a sub node with given name as the new parent until required matching EndNode, and returns nothing."""
    sf.StartNode(name)


def end_node(expand=False):
    """Completes the last StartNode, expanding contents if expand is true, and returns nothing."""
    sf.EndNode(expand)


def log(message, level='Info'):
    """Logs the specified message with a log level. (Trace, Debug, Info, Warn, Error, Fatal)"""
    sf.Log(message, level)
