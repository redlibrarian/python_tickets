import uuid

class Ticket:
  def __init__(self, user, issue):
    self.user = user
    self.issue = issue
    self.status = "open"
    self.id = uuid.uuid4()
    self.notes = [issue]

  def __repr__(self):
    return f"Ticket {self.id}: User: {self.user}, Status: {self.status}, Issue: {self.issue}"

  def fetch_notes(self):
    for index, note in enumerate(self.notes):
      print(f"{index}. {note}")

  def add_note(self, note):
    self.notes.append(note)
