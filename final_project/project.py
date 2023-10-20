import re
import pandas as pd
import matplotlib.pyplot as plt  # Import the matplotlib library
data = pd.read_csv('housing_data.csv', sep=',')


def is_valid_location(location):
    # Use a regular expression to validate the location format (City, State)
    location_pattern = r"^[a-zA-Z\s,.'-]+,\s[a-zA-Z\s.'-]+$"
    return re.match(location_pattern, location) is not None

def fetch_nearest_metro_region(location):
    # Read the data from the CSV file and find the nearest metro region based on the location
    if not data['RegionName'].str.contains(location).any():
        state = location.split(',')[1].strip()
        suggestion = data[data['StateName'] == state]['RegionName']
        suggestion = suggestion.reset_index(drop = True)
        suggestion.index += 1
        print(f'Your city is not in our list. Please choose the nearest metro from\n{suggestion}')
    else:
        return location

def get_value(target):
    home_value = data[data['RegionName'] == target]['2023-08-31'].values[0]
    print(f"Home Value for the nearest metro region to {target}: ${home_value:.0f}")
    return home_value


def plot_historic_home_value(target_city, location):
    # Extract the years and home values from the data
    date_columns = [col for col in target_city.columns if col not in ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName']]
    target_city.set_index('RegionName', inplace=True)
    target_city = target_city[date_columns]

    target_city = target_city.T
    unique_years = []
    annual_averages = []

    for i in range(0, len(target_city), 12):  # Assuming data is monthly
        annual_data = target_city.iloc[i:i+12]
        annual_average = annual_data.mean().values[0]
        annual_averages.append(annual_average)
        year = int(annual_data.index[0].split('-')[0])
        unique_years.append(year)  # Append years to the list

    # Create a line chart
    plt.figure(figsize=(12, 6))
    plt.plot(unique_years, annual_averages, marker='o', linestyle='-')

    #plt.plot(target_city.index, target_city, marker='o', linestyle='-')
    plt.title(f'Annual Home Value Trend for {location}')
    plt.xlabel('Year')
    plt.ylabel('Home Value')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Show the chart
    plt.show()
    plt.savefig('plot.png')  # Save the plot as a PNG file
    print('The trend chart is now saved in the project directory folder')

def main():
    while True:
        location = input("Enter the city and state (e.g., City, State): ")
        if is_valid_location(location):
            if fetch_nearest_metro_region(location):
                target = location
                break
        else:
            print("Invalid location format. Please enter a valid location in the format 'City, State'.")
    
    get_value(target)
    response = input("Do you want to see a historic annual value chart? (yes/no): ").strip().lower()
    if response.lower() == 'yes':
        # Extract historic data (assuming there's a 'Year' column in your CSV)
        historic_data = data[data['RegionName'] == target]  # You should populate this list with data from your CSV
        plot_historic_home_value(historic_data, location)  # Change 'years' to the desired number of years
    else:
        print("Okay, no chart will be shown.")

if __name__ == "__main__":
    main()
