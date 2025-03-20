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

def test_assign_ticket():
  ts.create_agent("Sam Popowich", "Library Systems")
  ts.create_ticket("Attila the Hun", "Horse stopped running.")
  assert len(ts.agents[0].tickets) == 0
  ts.assign_ticket(ts.agents[0], ts.tickets[0])
  assert len(ts.agents[0].tickets) == 1
