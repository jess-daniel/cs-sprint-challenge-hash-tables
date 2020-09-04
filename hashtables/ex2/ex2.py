#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


cache = {}


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []

    for ticket in tickets:
        # starting place
        if ticket.source == "NONE":
            route.append(ticket.destination)
        cache[ticket.source] = ticket.destination

    # print(route)
    current_ticket = cache[route[0]]
    # print(current_ticket)

    count = 1

    while count < length:
        route.append(current_ticket)
        # print(route)
        current_ticket = cache[current_ticket]
        count += 1
    return route
