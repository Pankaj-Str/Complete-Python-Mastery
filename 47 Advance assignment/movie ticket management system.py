import json
from datetime import datetime

class Movie:
    def __init__(self, title, duration, rating):
        self.title = title
        self.duration = duration
        self.rating = rating
        self.show_times = []

    def __str__(self):
        return f"{self.title} ({self.duration} min, {self.rating})"

    def add_show_time(self, show_time):
        self.show_times.append(show_time)

    def remove_show_time(self, show_time):
        self.show_times.remove(show_time)

class Theater:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.movies = []
        self.seats = {}

    def add_movie(self, movie):
        self.movies.append(movie)
        for show_time in movie.show_times:
            self.seats[show_time] = [True] * self.capacity

    def remove_movie(self, movie):
        self.movies.remove(movie)
        for show_time in movie.show_times:
            del self.seats[show_time]

    def display_movies(self):
        for movie in self.movies:
            print(movie)

    def display_show_times(self, movie):
        for show_time in movie.show_times:
            print(show_time.strftime("%Y-%m-%d %H:%M"))

    def book_ticket(self, movie, show_time, num_tickets):
        if show_time not in self.seats:
            raise ValueError("Invalid show time")
        available_seats = self.seats[show_time].count(True)
        if available_seats < num_tickets:
            raise ValueError(f"Not enough seats available. Only {available_seats} seats left.")
        booked_seats = []
        for i, seat in enumerate(self.seats[show_time]):
            if seat and len(booked_seats) < num_tickets:
                self.seats[show_time][i] = False
                booked_seats.append(i + 1)
        return booked_seats

    def cancel_booking(self, movie, show_time, seat_numbers):
        if show_time not in self.seats:
            raise ValueError("Invalid show time")
        for seat in seat_numbers:
            if seat <= 0 or seat > self.capacity:
                raise ValueError(f"Invalid seat number: {seat}")
            self.seats[show_time][seat - 1] = True

class TicketSystem:
    def __init__(self):
        self.theaters = []

    def add_theater(self, theater):
        self.theaters.append(theater)

    def remove_theater(self, theater):
        self.theaters.remove(theater)

    def display_theaters(self):
        for theater in self.theaters:
            print(f"{theater.name} (Capacity: {theater.capacity})")

    def save_to_file(self, filename):
        data = {
            "theaters": [
                {
                    "name": theater.name,
                    "capacity": theater.capacity,
                    "movies": [
                        {
                            "title": movie.title,
                            "duration": movie.duration,
                            "rating": movie.rating,
                            "show_times": [st.isoformat() for st in movie.show_times]
                        }
                        for movie in theater.movies
                    ],
                    "seats": {st.isoformat(): seats for st, seats in theater.seats.items()}
                }
                for theater in self.theaters
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        self.theaters = []
        for theater_data in data["theaters"]:
            theater = Theater(theater_data["name"], theater_data["capacity"])
            for movie_data in theater_data["movies"]:
                movie = Movie(movie_data["title"], movie_data["duration"], movie_data["rating"])
                movie.show_times = [datetime.fromisoformat(st) for st in movie_data["show_times"]]
                theater.add_movie(movie)
            theater.seats = {datetime.fromisoformat(st): seats for st, seats in theater_data["seats"].items()}
            self.add_theater(theater)

def main():
    ticket_system = TicketSystem()
    try:
        ticket_system.load_from_file("ticket_system_data.json")
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found. Starting with an empty system.")

    while True:
        print("\nMovie Ticket Management System")
        print("1. Add a new theater")
        print("2. Add a new movie to a theater")
        print("3. Display all theaters")
        print("4. Display movies in a specific theater")
        print("5. Book a ticket")
        print("6. Cancel a booking")
        print("7. Save and exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter theater name: ")
            capacity = int(input("Enter theater capacity: "))
            theater = Theater(name, capacity)
            ticket_system.add_theater(theater)
            print("Theater added successfully!")

        elif choice == "2":
            theater_name = input("Enter theater name: ")
            theater = next((t for t in ticket_system.theaters if t.name == theater_name), None)
            if theater:
                title = input("Enter movie title: ")
                duration = int(input("Enter movie duration (in minutes): "))
                rating = input("Enter movie rating: ")
                movie = Movie(title, duration, rating)
                show_time = input("Enter show time (YYYY-MM-DD HH:MM): ")
                movie.add_show_time(datetime.strptime(show_time, "%Y-%m-%d %H:%M"))
                theater.add_movie(movie)
                print("Movie added successfully!")
            else:
                print("Theater not found.")

        elif choice == "3":
            ticket_system.display_theaters()

        elif choice == "4":
            theater_name = input("Enter theater name: ")
            theater = next((t for t in ticket_system.theaters if t.name == theater_name), None)
            if theater:
                theater.display_movies()
            else:
                print("Theater not found.")

        elif choice == "5":
            theater_name = input("Enter theater name: ")
            theater = next((t for t in ticket_system.theaters if t.name == theater_name), None)
            if theater:
                movie_title = input("Enter movie title: ")
                movie = next((m for m in theater.movies if m.title == movie_title), None)
                if movie:
                    show_time = datetime.strptime(input("Enter show time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                    num_tickets = int(input("Enter number of tickets: "))
                    try:
                        booked_seats = theater.book_ticket(movie, show_time, num_tickets)
                        print(f"Tickets booked successfully! Seat numbers: {booked_seats}")
                    except ValueError as e:
                        print(f"Booking failed: {e}")
                else:
                    print("Movie not found.")
            else:
                print("Theater not found.")

        elif choice == "6":
            theater_name = input("Enter theater name: ")
            theater = next((t for t in ticket_system.theaters if t.name == theater_name), None)
            if theater:
                movie_title = input("Enter movie title: ")
                movie = next((m for m in theater.movies if m.title == movie_title), None)
                if movie:
                    show_time = datetime.strptime(input("Enter show time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                    seat_numbers = list(map(int, input("Enter seat numbers to cancel (comma-separated): ").split(",")))
                    try:
                        theater.cancel_booking(movie, show_time, seat_numbers)
                        print("Booking cancelled successfully!")
                    except ValueError as e:
                        print(f"Cancellation failed: {e}")
                else:
                    print("Movie not found.")
            else:
                print("Theater not found.")

        elif choice == "7":
            ticket_system.save_to_file("ticket_system_data.json")
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()