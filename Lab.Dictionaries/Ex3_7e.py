
trips_dict = {1.1: 6.25, 0.8: 5.25, 2.5: 10.50, 2.6: 8.05}

trips_list_programmatic = [{'duration': duration, 'fare': fare} for duration, fare in trips_dict.items()]

print(trips_list_programmatic)

third_trip_programmatic = trips_list_programmatic[2]
print(f"The 3rd trip was {third_trip_programmatic['duration']} miles and cost ${third_trip_programmatic['fare']:.2f}.")
