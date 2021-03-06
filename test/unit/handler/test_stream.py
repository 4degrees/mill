# :coding: utf-8
# :copyright: Copyright (c) 2013 Martin Pengelly-Phillips
# :license: See LICENSE.txt.

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from mock import Mock

from sawmill.log import Log
from sawmill.handler.stream import Stream


def test_output():
    '''Test outputting to specified stream.'''
    target = StringIO()
    formatter = Mock()
    formatter.format = Mock(return_value='A message')

    stream = Stream(
        stream=target,
        formatter=formatter
    )

    log = Log(level='info', message='A message')
    stream.handle(log)

    assert target.getvalue() == 'A message'


def test_flush_when_supported_by_stream():
    '''Test flush when supported by stream.'''
    target = Mock()
    target.flush = Mock()

    stream = Stream(
        stream=target,
    )

    stream.flush()

    assert target.flush.called


def test_flush_when_unsupported_by_stream():
    '''Test flush executes without error when unsupported by stream.'''
    target = Mock()

    stream = Stream(
        stream=target,
    )

    stream.flush()


def test_teardown_open_stream():
    '''Teardown open stream.'''
    target = StringIO()

    stream = Stream(stream=target)
    stream.output(['test'])
    stream.teardown()

    assert not target.closed
    assert target.getvalue() == 'test'


def test_teardown_closed_stream():
    '''Teardown closed stream without error.'''
    target = StringIO()
    stream = Stream(stream=target)
    target.close()
    stream.teardown()
