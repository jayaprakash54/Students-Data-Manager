import json

class StudentsDatabase:

    def __init__(self):
        self.students_data = {}

    def pass_status(self, score):
        return "Pass" if score>30 else "Fail"

    def insert_data(self,name,address,city,country,pincode,sat_score):
        if name in self.students_data:
            print(f"{name} name already exist, please enter a uniques name")
        else:
            self.students_data[name] = {
                "Address"  : address,
                "City"     : city,
                "Country"  : country,
                "Pincode"  : pincode,
                "sat_score": sat_score,
                "Passed"   : self.pass_status(sat_score)
            }
        print(f"Data for {name} inserted successfully.")

    def view_all_data(self):
        return json.dumps(self.students_data, indent=4)

    def get_rank(self,name):
        if name not in self.students_data:
            return f"No data found for {name}."

        sorted_results = sorted(self.students_data.items(), key=lambda x: x[1]["sat_score"], reverse=True)
        for rank, (candidate_name, data) in enumerate(sorted_results, start=1):
            if candidate_name == name:
                return f"Rank of {name}: {rank}"

    def update_score(self, name, score):
        if name not in self.students_data:
            print(f"please enter valid student name")
        else:
            self.students_data[name]["sat_score"] = score
            self.students_data[name]["Passed"] = self.pass_status(score)
            print(f"Score updated for {name}.")

    def delete_one_record(self, name):
        if name in self.students_data:
            del self.students_data[name]
            print(f"{name} student data deleted successfully")
        else:
            print(f"No data found for {name}.")

    def average_sat_score(self):
        if not self.students_data:
            return "No data available to calculate average."
        total = sum(data["sat_score"] for data in self.students_data.values())
        average_score = total/len(self.students_data)
        return f"Average SAT Score: {average_score:.2f}"

    def filter_by_status(self,status):
        filtered_results = {name:data for name,data in self.students_data.items() if self.data["passed"].lower()==status.lower()}
        return json.dumps(filtered_results, indent=4)

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.students_data, file, indent=4)
        print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    manager = StudentsDatabase()

    while True:
        print("\nMenu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Calculate Average SAT Score")
        print("7. Filter records by Pass/Fail Status")
        print("8. Save data to JSON file")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            address = input("Enter address: ")
            city = input("Enter city: ")
            country = input("Enter country: ")
            pincode = input("Enter pincode: ")
            sat_score = int(input("Enter SAT score: "))
            manager.insert_data(name, address, city, country, pincode, sat_score)
        elif choice == '2':
            print(manager.view_all_data())
        elif choice == '3':
            name = input("Enter name: ")
            print(manager.get_rank(name))
        elif choice == '4':
            name = input("Enter name: ")
            new_score = int(input("Enter new SAT score: "))
            manager.update_score(name, new_score)
        elif choice == '5':
            name = input("Enter name: ")
            manager.delete_one_record(name)
        elif choice == '6':
            print(manager.average_sat_score3())
        elif choice == '7':
            status = input("Enter status (Pass/Fail): ")
            print(manager.filter_by_status(status))
        elif choice == '8':
            filename = input("Enter filename: ")
            manager.save_to_json(filename)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")









