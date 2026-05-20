import requests
from bs4 import BeautifulSoup
import csv

# function to save data on csv file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Car Name', 'Price'])
        writer.writerows(data)
    print(f"Data saved to {filename}")

car = input("Enter manufacturer name:")