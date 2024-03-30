"""This exercise requires you to work with multiple classes."""


class PublicTransport:
    def __init__(self, route: list[str]):
        self.route = route

    def calculate_fare(self, start_stop: str, end_stop: str) -> float:
        # Do not write a body for this method. Each subclass should define its own calculate_fare function.
        pass

    def __str__(self) -> str:
        # Do not write a body fot this method. Each subclass should define its own string representation.
        pass


class Trip:
    def __init__(self, transport, stops, fare):
        self.transport = transport
        self.stops = stops
        self.fare = fare

    def __str__(self) -> str:
        """Return the formatted message: `Using '{transport}' ({amount_of_stops} stops), costing {fare}.`.

        Replace {transport} with the string representation of the specific transport used for the trip.
        Replace {amount_of_steps} with the amount of steps required to make this trip.
        Replace {fare} with the amount of fare required to make this trip.
        """
        return f"Using '{self.transport}' ({self.stops} stops), costing {self.fare}."


class TripPlanner:
    transports: list[PublicTransport] = []

    @classmethod
    def find_trips(cls, start_stop: str, end_stop: str) -> list[Trip]:
        """Return possible trips from start_stop to end_stop sorted by fare from lowest to highest."""
        possible_trips = []
        for transport in cls.transports:
            fare = transport.calculate_fare(start_stop, end_stop)
            if fare is not None:
                stops = abs(transport.route.index(start_stop) - transport.route.index(end_stop))
                trip = Trip(str(transport), stops, fare)
                possible_trips.append(trip)
        return sorted(possible_trips, key=lambda x: x.fare)

    @classmethod
    def plan_trip(cls):
        print('Welcome to Trip Planner 9000!')
        print('This trip planner will show you all the ways to get from A to B.\n')

        start_stop = input('Where would you like to travel from?  - ')
        end_stop = input('Where would you like to tarvel to?  - ')
        possible_trips = cls.find_trips(start_stop, end_stop)

        if len(possible_trips) == 0:
            print(f'\nSorry. There are no available routes from {start_stop} to {end_stop} at this time.')
            return

        print(f'There are {len(possible_trips)} available routes from {start_stop} to {end_stop}:')
        for i in range(len(possible_trips)):
            trip = possible_trips[i]
            print(f'{i + 1}. {trip}')


class Bus(PublicTransport):
    def __init__(self, route: list[str], nr: int):
        super().__init__(route)
        self.nr = nr

    def calculate_fare(self, start_stop, end_stop):
        if start_stop not in self.route or end_stop not in self.route:
            return None
        return round(1.50, 2)

    def __str__(self) -> str:
        return f"Bus {self.nr} {self.route[-1]}"


class TrolleyBus(PublicTransport):
    def __init__(self, route: list[str], nr: int):
        super().__init__(route)
        self.nr = nr
        self.fare = 1.00

    def calculate_fare(self, start_stop, end_stop):
        if start_stop not in self.route or end_stop not in self.route:
            return None
        stops = self.route.index(end_stop) - self.route.index(start_stop)
        base_fare = 1.00
        additional_fare = ((stops - 1) // 3) * 0.20
        return round(base_fare + additional_fare, 2)

    def __str__(self) -> str:
        return f"TrolleyBus {self.nr} {self.route[-1]}"


class Train(PublicTransport):
    def __init__(self, route: list[str], zones: dict[str, str]):
        super().__init__(route)
        self.zones = zones

    def calculate_fare(self, start_stop, end_stop):
        if start_stop not in self.route or end_stop not in self.route:
            return None
        
        fare = 0
        zones_visited = []
        
        for stop in self.route[self.route.index(start_stop): self.route.index(end_stop) + 1]:
            zone = self.zones[stop]
            if zone not in zones_visited:
                fare += self._get_zone_fare(zone)
                zones_visited.append(zone)
        
        return round(fare, 2)

    def _get_zone_fare(self, zone):
        if zone == 'Green':
            return 0.75
        elif zone == 'Blue':
            return 0.55
        elif zone == 'Red':
            return 1.00

    def __str__(self) -> str:
        return f"Train {self.route[0]} - {self.route[-1]}"
