import pytest
import ticket

t = ticket.Ticket("Attila the Hun", "Horse stopped running.")

def test_ticket():
  ticket_id = t.id
  assert str(t) == f"Ticket {ticket_id}: User: Attila the Hun, Status: open, Issue: Horse stopped running."

def test_add_note():
  assert len(t.notes) == 1
  t.add_note("Tried rebooting horse.")
  assert len(t.notes) == 2

def test_fetch_notes():
  assert t.fetch_notes() == {0: 'Horse stopped running.', 1: 'Tried rebooting horse.'}
