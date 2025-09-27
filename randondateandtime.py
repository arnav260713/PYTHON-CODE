import random
import datetime

def random_date(start, end):
    """
    Generate a random datetime between two datetime objects.
    """
    # Convert start and end dates to timestamps (seconds since 1970)
    start_timestamp = int(start.timestamp())
    end_timestamp = int(end.timestamp())

    # Pick a random second between them
    random_timestamp = random.randint(start_timestamp, end_timestamp)

    # Convert back to datetime
    return datetime.datetime.fromtimestamp(random_timestamp)

# Example usage:
start_date = datetime.datetime(2024, 1, 1, 0, 0, 0)   # Jan 1, 2024
end_date = datetime.datetime(2025,1 , 1, 0, 0, 0) # Dec 31, 2024

print("Random Date and Time:", random_date(start_date, end_date))