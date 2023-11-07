import csv

class ReadAndWriteData:
    def __init__(self, csv_file):
        self.data = []
        self.read_data_from_csv(csv_file)

    def read_data_from_csv(self, csv_file):
        try:
            with open(csv_file, mode='r', newline='') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    self.data.append(row)
        except FileNotFoundError:
            print(f"CSV file '{csv_file}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def display_data(self):
        if not self.data:
            print("No data to display.")
        else:
            print("Name\tSkillSet\tExperience")
            for row in self.data:
                print(f"{row['Name']}\t{row['SkillSet']}\t{row['Experience']}")

if __name__ == "__main__":
    csv_file = "data.csv"  # Replace with the path to your CSV file
    data_handler = ReadAndWriteData(csv_file)
    data_handler.display_data()
