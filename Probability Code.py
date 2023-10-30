import math
def calculate_odds(probability):
    return probability / (1 / probability)
probability = float(input("Enter the probability of an event (between 0 and 1):"))
odds = calculate_odds(probability)
print(f"The offs of the event happening are: {odds: .2f} to 1")