import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
file_path = 'camera_dataset.csv'  # Ensure the CSV file is in the same directory as this script
camera_data = pd.read_csv(file_path)

# Handle missing values by replacing them with the median of numeric columns
camera_data.fillna(camera_data.median(numeric_only=True), inplace=True)

# Define a class to handle dataset operations
class CameraDatasetHandler:
    def __init__(self, data):
        self.data = data

    # Filter dataset by release year range
    def filter_by_year(self, start_year, end_year):
        return self.data[(self.data['Release date'] >= start_year) & 
                         (self.data['Release date'] <= end_year)]
    
    # Filter dataset by a maximum price
    def filter_by_price(self, max_price):
        return self.data[self.data['Price'] <= max_price]

    # Add a new camera entry to the dataset
    def add_new_camera(self, details):
        new_entry = pd.DataFrame([details], columns=self.data.columns)
        self.data = pd.concat([self.data, new_entry], ignore_index=True)

    # Get a statistical summary of the dataset
    def get_summary(self):
        return self.data.describe()

# Extend the base handler with additional functionality
class CameraDatasetHandlerExtended(CameraDatasetHandler):
    # Retrieve details of cameras matching a specific model name
    def retrieve_camera_details(self, model_name):
        return self.data[self.data['Model'].str.contains(model_name, case=False)]
    
    # Update the price of a camera based on its model name
    def update_camera_price(self, model_name, new_price):
        self.data.loc[self.data['Model'].str.contains(model_name, case=False), 'Price'] = new_price

# Instantiate the extended handler class
camera_handler_ext = CameraDatasetHandlerExtended(camera_data)

# Define functions for visualizing the data
def visualize_price_distribution(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data['Price'], bins=30, edgecolor='k', alpha=0.7)
    plt.title('Distribution of Camera Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def visualize_resolution_vs_price(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Max resolution'], data['Price'], alpha=0.7)
    plt.title('Max Resolution vs Price')
    plt.xlabel('Max Resolution (pixels)')
    plt.ylabel('Price ($)')
    plt.grid(alpha=0.3)
    plt.show()

# Define a CLI class to interact with the dataset
class CameraCLI:
    def __init__(self, camera_handler):
        self.camera_handler = camera_handler

    # Display the menu options
    def display_menu(self):
        print("\n--- Camera Dataset CLI ---")
        print("1. View Dataset Summary")
        print("2. Filter by Release Year")
        print("3. Filter by Price")
        print("4. Add a New Camera")
        print("5. Retrieve Camera Details")
        print("6. Update Camera Price")
        print("7. Visualize Data")
        print("8. Exit")

    # Handle user input and execute corresponding actions
    def handle_input(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")
            
            if choice == '1':
                print("\n--- Dataset Summary ---")
                print(self.camera_handler.get_summary())
            
            elif choice == '2':
                start_year = int(input("Enter start year: "))
                end_year = int(input("Enter end year: "))
                filtered_data = self.camera_handler.filter_by_year(start_year, end_year)
                print(f"\nFiltered Cameras ({start_year}-{end_year}):")
                print(filtered_data)

            elif choice == '3':
                max_price = float(input("Enter maximum price: "))
                filtered_data = self.camera_handler.filter_by_price(max_price)
                print(f"\nFiltered Cameras (Price <= ${max_price}):")
                print(filtered_data)

            elif choice == '4':
                print("\n--- Add a New Camera ---")
                details = {
                    "Model": input("Enter Model: "),
                    "Release date": int(input("Enter Release Year: ")),
                    "Max resolution": float(input("Enter Max Resolution: ")),
                    "Low resolution": float(input("Enter Low Resolution: ")),
                    "Effective pixels": float(input("Enter Effective Pixels: ")),
                    "Zoom wide (W)": float(input("Enter Zoom Wide (W): ")),
                    "Zoom tele (T)": float(input("Enter Zoom Tele (T): ")),
                    "Normal focus range": float(input("Enter Normal Focus Range: ")),
                    "Macro focus range": float(input("Enter Macro Focus Range: ")),
                    "Storage included": float(input("Enter Storage Included: ")),
                    "Weight (inc. batteries)": float(input("Enter Weight (inc. batteries): ")),
                    "Dimensions": float(input("Enter Dimensions: ")),
                    "Price": float(input("Enter Price: "))
                }
                self.camera_handler.add_new_camera(details)
                print("New camera added successfully!")

            elif choice == '5':
                model_name = input("Enter the camera model name to retrieve: ")
                retrieved_data = self.camera_handler.retrieve_camera_details(model_name)
                print(f"\nDetails of {model_name}:")
                print(retrieved_data)

            elif choice == '6':
                model_name = input("Enter the camera model name to update: ")
                new_price = float(input("Enter the new price: "))
                self.camera_handler.update_camera_price(model_name, new_price)
                print(f"Updated the price of {model_name} successfully!")

            elif choice == '7':
                print("\n--- Visualization Options ---")
                print("1. Price Distribution")
                print("2. Max Resolution vs Price")
                viz_choice = input("Enter your choice (1-2): ")
                if viz_choice == '1':
                    visualize_price_distribution(self.camera_handler.data)
                elif viz_choice == '2':
                    visualize_resolution_vs_price(self.camera_handler.data)
                else:
                    print("Invalid choice.")

            elif choice == '8':
                print("Exiting the CLI. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

# Run the CLI for user interaction
camera_cli = CameraCLI(camera_handler_ext)
camera_cli.handle_input()