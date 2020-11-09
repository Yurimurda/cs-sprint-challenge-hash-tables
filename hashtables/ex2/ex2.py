#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    route = []

    for ticket in tickets:
        hash_table[ticket.source] = ticket.destination

    destination = hash_table["NONE"]
    while destination != "NONE":
        route.append(destination)
        destination = hash_table[destination]

    route.append("NONE")

    return route
