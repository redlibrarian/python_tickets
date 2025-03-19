import pytest
from ticket_system import TicketSystem

ts = TicketSystem()

def test_ticket_system_created():
    assert type(ts) == TicketSystem
