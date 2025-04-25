class MovieTicket:
    def __init__(self, movie_name, theater, show_time, ticket_price):
        self.movie_name = movie_name
        self.theater = theater
        self.show_time = show_time
        self.ticket_price = ticket_price

    def book_ticket(self):
        print("\nBooking Details")
        print(f"Movie: {self.movie_name}")
        print(f"Theater: {self.theater}")
        print(f"Show Time: {self.show_time}")
        print(f"Ticket Price: ${self.ticket_price}")

movie_name = input("Enter movie name: ")
theater = input("Enter theater name: ")
show_time = input("Enter show time: ")
ticket_price = float(input("Enter ticket price: "))

ticket1 = MovieTicket(movie_name, theater, show_time, ticket_price)
ticket1.book_ticket()
