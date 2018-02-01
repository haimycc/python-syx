from core2 import initial_state, render, key as rusty_key
from textui import step, parse, dispatch
from pytest import raises

def test_parse():
    assert parse('move up') == ['move', 'up']
    assert parse('move in there') == ['move', 'in there']
    assert parse('take bottle') == ['take', 'bottle']
    assert parse('take rusty key') == ['take', 'rusty key']

def test_parse_error():
    with raises(Exception) as err_info:
        parse('move')
    assert str(err_info.value) == 'Expected: `take <item>` or `move <direction>`'

def test_dispatch():
    in_street = initial_state.set(location_name='Street')
    with_key = in_street.transform(
        ['inventory'], [rusty_key], #rusty key added to inventory
        ['world', 'Street', 'items'], {}, # rusty key removed from location
    )
    assert dispatch(initial_state, 'move', 'east') == in_street
    assert dispatch(in_street, 'take', 'rusty key') == with_key

def test_dispatch_error():
    with raises(Exception) as err_info:
        dispatch(initial_state, 'move', 'up')
    assert str(err_info.value) == 'Invalid argument!'


import mock # unittest.mock on Python 3

@mock.patch('textui.print')
@mock.patch('textui.raw_input')
def test_step(m_input, m_print):
    m_input.return_value = 'move east'
    new_state = step(initial_state)
    in_street = initial_state.set(location_name='Street')
    assert new_state == in_street
    m_print.assert_any_call(render(initial_state))
    m_input.assert_called_once_with('> ')
    m_print.assert_any_call('Okay.')
