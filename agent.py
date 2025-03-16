import uuid
import ticket

class Agent:
  def __init__(self, name, department):
    self.name = name
    self.department = department
    self.agent_id = uuid.uuid4()
    self.tickets = []

  def __repr__(self):
    return f"Name: {self.name}, Department: {self.department}, ID: {self.agent_id}, Tickets Assigned: {len(self.tickets)}"

  def assign_ticket(self, ticket):
    self.tickets.append(ticket)

