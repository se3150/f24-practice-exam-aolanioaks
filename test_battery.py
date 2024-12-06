import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b


@pytest.fixture
def battery_with_monitor():
    mock_monitor = Mock()
    return Battery(100, external_monitor=mock_monitor), mock_monitor


def describe_Battery():


    def it_returns_current_charge(partially_charged_battery):
        assert partially_charged_battery.getCharge() == 70

    
    def it_charges_partially(partially_charged_battery):
        b = partially_charged_battery
        assert b.recharge(40) is True
        assert b.getCharge() == 100


    def it_charges_fully(charged_battery):
        b = charged_battery
        assert b.getCharge() == 100


    def it_does_not_exceed_capacity(charged_battery):
        b = charged_battery
        assert b.recharge(50) is False
        assert b.getCharge() == b.getCapacity()

    def it_notifies_external_monitor(battery_with_monitor):
        b, monitor = battery_with_monitor
        b.mCharge = 80
        b.recharge(10)
        monitor.notify_recharge.assert_called_once_with(90)

    def it_returns_false_with_invalid_input(charged_battery):
        b = charged_battery
        assert b.recharge(-10) is False
        assert b.getCharge() == b.getCapacity()


def describe_get_capacity():
    
    def it_returns_capacity(charged_battery):
        assert charged_battery.getCapacity() == 100


def describe_get_charge():

    def it_returns_current_charge(partially_charged_battery):
        assert partially_charged_battery.getCharge() == 70


def describe_drain():

    def it_reduces_charge(partially_charged_battery):
        b = partially_charged_battery
        assert b.drain(20) is True
        assert b.getCharge() == 50

    def it_doesnt_go_below_zero(charged_battery):
        b = charged_battery
        b.mCharge = 10
        assert b.drain(20) is True
        assert b.getCharge() == 0

    def it_notifies_external_monitor(battery_with_monitor):
        b, monitor = battery_with_monitor
        b.drain(30)
        monitor.notify_drain.assert_called_once_with(70)