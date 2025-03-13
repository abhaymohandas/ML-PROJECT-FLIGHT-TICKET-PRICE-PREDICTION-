FLIGHT TICKET PRICE PREDICTION

The main objective of this machine learning project is to build and compare different regression models to accurately predict flight ticket prices. The goal is to develop a reliable model that estimates ticket prices based on various features such as airline, departure time, duration, number of stops, and booking time. This model will help both passengers and airlines make informed pricing decisions, optimize ticket purchases, and improve market transparency.

FEATURES

The various features of the cleaned dataset are explained below:

Airline: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.
Flight: Flight stores information regarding the plane's flight code. It is a categorical feature.
Source City: City from which the flight takes off. It is a categorical feature having 6 unique cities.
Departure Time: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.
Stops: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.
Arrival Time: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.
Destination City: City where the flight will land. It is a categorical feature having 6 unique cities.
class1: A categorical feature that contains information on seat class1; it has two distinct values: Business and Economy.
Duration: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.
Days Left: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.
Price: Target variable stores information of the ticket price.
