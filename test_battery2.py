import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')


#I DIDN'T USE THIS
@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b





def describe_battery():

    def it_shows_current_charge():
        b = Battery(100)
        assert b.getCharge() == 100

    
    def it_shows_the_battery_capacity():
        b = Battery(100)
        assert b.getCapacity() == 100



    def it_returns_partial_battery(partially_charged_battery):
        b = partially_charged_battery
        assert b.getCharge() == 70



        ##MOCK THIS 
    def test_external_monitor_for_recharge():  
        #Create a mock for the external monitor
        mock_external_monitor = Mock()

        #Create a Battery instance with the mock as the external monitor
        b = Battery(100, external_monitor=mock_external_monitor)

        #Recharge the battery
        b.recharge(30)

        #Verify that notify_recharge was called with the correct updated charge
        assert mock_external_monitor.notify_recharge(100) 


    #current battery is at 100, if we recharge it 40 more than it will fail. Make sure charge is == capacity
    def it_doesnt_go_past_capacity():
        b = Battery(100)
        assert b.recharge(40) == False
        assert b.getCharge() == b.getCapacity()


    def it_drains_the_battery():
        b = Battery(100)
        assert b.drain(50) == True
        assert b.getCharge() == 50
        


    def drain_does_not_go_under_zero():
        b = Battery(100)
        assert b.drain(-10) == False
        


    def test_external_monitor_for_drain():
        mock_external_monitor = Mock()

        b = Battery(100, external_monitor=mock_external_monitor)

        b.drain(20)
        assert mock_external_monitor.notify_drain(80)


    def it_doesnt_recharge_with_negative_numbers_or_zeros(partially_charged_battery):
        b = partially_charged_battery

        assert b.recharge(-5) == False
        assert b.recharge(0) == False

    
    