trip_durations = [1.1, 0.8, 2.5, 2.6]

trip_fares = ("6.25", "5.25", "10.50", "8.05")

trips = {
    "miles": trip_durations,
    "fares": trip_fares
}

trips = dict(zip(trip_durations, trip_fares))
print(trips)
duration= trip_durations[2]
print(f"The 3'rd trip was {trips[duration]} miles and cost {trips[duration]}")