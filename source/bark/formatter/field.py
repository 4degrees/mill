# :coding: utf-8
# :copyright: Copyright (c) 2013 Martin Pengelly-Phillips
# :license: See LICENSE.txt.

from .base import Formatter


class Field(Formatter):
    '''Format :py:class:`~bark.log.Log` to string according to item list.'''

    IGNORE, ERROR = ('ignore', 'error')

    def __init__(self, keys, mode=IGNORE, template='{key}={value}',
                 item_separator=':'):
        '''Initialise formatter with *keys* to look for in specific order.

        *mode* determines how to handle a missing key when formatting a log.
        The default IGNORE will substitute an empty string for the missing
        value. An alternative is ERROR, which would cause an error to be
        raised.

        *template* is used to format the key and value of each field and
        *item_separator* will separate each item.

        '''
        super(Field, self).__init__()
        self.keys = keys
        self.mode = mode
        self.template = template
        self.item_separator = item_separator

    def format(self, log):
        '''Return formatted data representing *log*.'''
        data = []
        for key in self.keys:
            if not key in log:
                if self.mode is self.ERROR:
                    raise KeyError()
                else:
                    value = ''
            else:
                value = log[key]

            entry = self.template.format(key=key, value=value)
            if entry:
                data.append(entry)

        return self.item_separator.join(data)

