import pytest
from ticket_system import TicketSystem

ts = TicketSystem()

def test_ticket_system_created():
    assert type(ts) == TicketSystem

def test_create_agent():
  assert len(ts.list_agents()) == 0
  ts.create_agent("Sam Popowich", "Library Systems")
  assert len(ts.list_agents()) == 1

def test_create_ticket():
  assert len(ts.list_tickets()) == 0
  ts.create_ticket("Attila the Hun", "Horse stopped running.")
  assert len(ts.list_tickets()) == 1
