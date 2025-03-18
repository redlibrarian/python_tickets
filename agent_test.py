import pytest
import agent
import ticket

a = agent.Agent("Gengis Khan", "Mongol Horde")

def test_agent():
  agent_id = a.agent_id
  assert str(a) == f"Name: Gengis Khan, Department: Mongol Horde, ID: {agent_id}, Tickets Assigned: 0"

def test_assign_tickets():
  assert len(a.tickets) == 0
  t = ticket.Ticket("Attila the Hun", "Horse stopped running")
  a.assign_ticket(t)
  assert len(a.tickets) == 1
