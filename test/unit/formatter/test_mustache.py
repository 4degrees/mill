# :coding: utf-8
# :copyright: Copyright (c) 2013 Martin Pengelly-Phillips
# :license: See LICENSE.txt.

import pystache

from sawmill.log import Log
from sawmill.formatter.mustache import Mustache


def test_format():
    '''Test formatted log result is as expected.'''
    log = Log(message='A message', level='info')
    template = Mustache('{{level}}:{{message}}')
    assert template.format([log]) == ['info:A message']


def test_batch_format():
    '''Test batch formatting collection of related logs.'''
    logs = [
        Log(message='A message', level='info'),
        Log(message='Another message', level='debug')
    ]
    template = Mustache(
        '{{#logs}}{{level}}:{{message}}\n{{/logs}}',
        batch=True
    )
    assert template.format(logs) == [
        'info:A message\ndebug:Another message\n'
    ]


def test_no_error_with_missing_values():
    '''Test missing values don't cause error.'''
    log = Log(message='A message')
    template = Mustache('{{level}}:{{message}}')
    assert template.format([log]) == [':A message']


def test_conditional():
    '''Test conditional statement.'''
    template = Mustache('{{#level}}{{.}}:{{/level}}{{message}}')

    log = Log(message='A message')
    assert template.format([log]) == ['A message']

    log = Log(level='info', message='A message')
    assert template.format([log]) == ['info:A message']


def test_callback():
    '''Test using callback.'''
    template = Mustache('{{#level}}{{.}}:{{/level}}{{message}}')

    log = Log(
        message='A message',
        level=lambda text: 'info' + pystache.render(text)
    )
    assert template.format([log]) == ['info:A message']


