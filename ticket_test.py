import pytest
import ticket

t = ticket.Ticket("Attila the Hun", "Horse stopped running.")

def test_ticket():
  ticket_id = t.id
  assert str(t) == f"Ticket {ticket_id}: User: Attila the Hun, Status: open, Issue: Horse stopped running."
