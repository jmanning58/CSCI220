## This program helps analyze traffic patterns
## Jacob Manning

## Specifications:
    # Need to get from the user:
        # how many roads surveyed
        # how many days was each road surveyed
        # how many cars traveled on that day
    # Compute average amount of cars per day
    # Sum of all cars
    # Ouputs:
        # Average per day
        # Total number of cars
        # Average per road

## Design:
    # Ask user for: 
        # "how_many_roads" -> roads surveyed
    # "all_cars" -> variable that will change with amount of cars
    # Loop for road details with ("how_many_roads"):
        # Ask user for:
            # "days" -> days road was surveyed
            # Loop for days with ("days")
                # Ask user for:
                    # "day_cars" -> number of cars on each day
                # "cars" -> total number of cars -> sum of "day_cars"
            # "road_average" -> "cars"/"days"
        # "all_cars" - "cars"+"all_cars"
        # Print "road_average"
    # "total_ave" - total average number of cars per road
    # Final Outputs:
        # Print "all_cars"
        # Print "total_ave"

def traffic():

    # Asking for amount of roads
    how_many_roads = eval(input("How many roads were surveyed? "))

    #storage varibale
    all_cars = 0
    
    # Asking for how many days
    for i in range(how_many_roads):
        how_many_days = eval(input("How many days was road " +str(i+1)+ " surveyed? "))
        cars = 0

        # Cars per day
        for j in range(how_many_days):
            day_cars = eval(input("How many cars traveled on day " +str(j+1)+ "? "))
            cars = day_cars + cars

        # These are calculated after each road
        all_cars = cars + all_cars    
        road_average = round(cars/how_many_days, 1)
        print("Road", i+1, "had an average of", road_average, "vehicles per day.")
        print()

    total_ave = round(all_cars/how_many_roads, 2)
    # Final values for user
    print("Total number of vehicles traveled on all roads: ", all_cars)
    print("Average number of vehicles per road: ", total_ave)

traffic()