# Import libraries in virtual environment

import rich
from rich import print
import pandas as pd
from rich.console import Console
from rich.table import Table
import csv
import os

# Create a Console 
console = Console()
console.print("Here is some Current NBA Player Data", style="bold cyan")

# Create table
table = Table(title="Favorite NBA Players")

# Define table columns
table.add_column("Players Name", justify="left", style="blue", no_wrap=True)
table.add_column("Current Team", justify="left", style="green")
table.add_column("Jersey Number", style="red")

# Add Player data 

table.add_row("Lebron James", "Los Angeles Lakers", "23")
table.add_row("Demar Derozan", "Sacramento Kings", "11")
table.add_row("Stephen Curry", "Golden State Warriors","30")
table.add_row("Jayson Tatum", "Boston Celtics", "0")


# Print the table to the console
console.print(table)


console.print("\n[bold green]Enter Your Favorite Current NBA Player:[/bold green]")



# Expand on this script
def get_user_input():
    player_name = input("Enter the Players name: ")
    team_name = input("Enter the team of the player: ")
    jersey_number = input("Enter the jersey number of the player: ")
    return player_name, team_name, jersey_number


#Data Confirmation
def confirm_data(player_name, team_name, jersey_number):
    console.print(f"\n[bold yellow]Please confirm the data you entered:[/bold yellow]")
    console.print(f"Player Name: {player_name}")
    console.print(f"Team: {team_name}") 
    console.print(f"Jersey Number: {jersey_number}")
    return input("\nIs the data correct? (yes/no): ").strip().lower() == 'yes'


# Function to save data to a file
def save_data_to_file(data, filename="nba_data.csv"):
    df = pd.DataFrame(data, columns=["Player Name", "Team Name", "Jersey Number"])
    df.to_csv(filename, index=False)
    console.print(f'Data saved to {os.path.abspath(filename)}')


# main function to run the script
def main():
    nba_data = []
    
    while True:
        
        player_name, team_name, jersey_number = get_user_input()

        
        if confirm_data(player_name, team_name, jersey_number):
            nba_data.append([player_name, team_name, jersey_number])
            console.print("\n[bold green]Data added.[/bold green]")
        else:
            console.print("\n[bold red]Please re-enter the data.[/bold red]")
            continue

        
        if input("\nDo you want to add another player? (yes/no): ").strip().lower() != 'yes':
            break
    
    # Save the data to csv file
    save_data_to_file(nba_data)

if __name__ == "__main__":
    main()
