# Main Class
class Farm:
    def __init__(self, farm_id, name):
        self.farm_id = farm_id
        self.name = name

    def display_details(self):
        return f"ID: {self.farm_id}, Name: {self.name}"


# Derived Classes
class Animal(Farm):
    def __init__(self, farm_id, name, species, age):
        super().__init__(farm_id, name)
        self.species = species
        self.age = age

    def display_details(self):
        return f"Animal - ID: {self.farm_id}, Name: {self.name}, Species: {self.species}, Age: {self.age} years"


class Crop(Farm):
    def __init__(self, farm_id, name, crop_type, harvest_time):
        super().__init__(farm_id, name)
        self.crop_type = crop_type
        self.harvest_time = harvest_time

    def display_details(self):
        return f"Crop - ID: {self.farm_id}, Name: {self.name}, Type: {self.crop_type}, Harvest Time: {self.harvest_time} days"


class Equipment(Farm):
    def __init__(self, farm_id, name, equip_type, condition):
        super().__init__(farm_id, name)
        self.equip_type = equip_type
        self.condition = condition

    def display_details(self):
        return f"Equipment - ID: {self.farm_id}, Name: {self.name}, Type: {self.equip_type}, Condition: {self.condition}"


class Worker(Farm):
    def __init__(self, farm_id, name, role, salary):
        super().__init__(farm_id, name)
        self.role = role
        self.salary = salary

    def display_details(self):
        return f"Worker - ID: {self.farm_id}, Name: {self.name}, Role: {self.role}, Salary: ${self.salary}"


# Data Storage
farm_records = []


# Functional Requirements
def add_record():
    try:
        print("\nChoose Farm Type to Add:")
        print("1. Animal\n2. Crop\n3. Equipment\n4. Worker")
        choice = int(input("Enter choice: "))

        farm_id = input("Enter ID: ")
        name = input("Enter Name: ")

        if choice == 1:
            species = input("Enter Species: ")
            age = int(input("Enter Age: "))
            farm_records.append(Animal(farm_id, name, species, age))

        elif choice == 2:
            crop_type = input("Enter Crop Type: ")
            harvest_time = int(input("Enter Harvest Time (days): "))
            farm_records.append(Crop(farm_id, name, crop_type, harvest_time))

        elif choice == 3:
            equip_type = input("Enter Equipment Type: ")
            condition = input("Enter Condition (New/Used): ")
            farm_records.append(Equipment(farm_id, name, equip_type, condition))

        elif choice == 4:
            role = input("Enter Role: ")
            salary = float(input("Enter Salary: "))
            farm_records.append(Worker(farm_id, name, role, salary))

        else:
            print("Invalid choice!")
            return

        print("Record added successfully!")
    except ValueError:
        print("Invalid input. Please try again.")


# Display all records
def display_all():
    if not farm_records:
        print("\nNo records available.")
    else:
        print("\nFarm Records:")
        for record in farm_records:
            print(record.display_details())


# Search records
def search_record():
    search_id = input("\nEnter ID to Search: ")
    found = False
    for record in farm_records:
        if record.farm_id == search_id:
            print(record.display_details())
            found = True
            break
    if not found:
        print("Record not found!")


# Update records
def update_record():
    update_id = input("\nEnter ID to Update: ")
    for record in farm_records:
        if record.farm_id == update_id:
            if isinstance(record, Animal):
                record.age = int(input("Enter new Age: "))
            elif isinstance(record, Crop):
                record.harvest_time = int(input("Enter new Harvest Time: "))
            elif isinstance(record, Equipment):
                record.condition = input("Enter new Condition: ")
            elif isinstance(record, Worker):
                record.salary = float(input("Enter new Salary: "))
            print("Record updated successfully!")
            return
    print("Record not found!")


# Delete records
def delete_record():
    delete_id = input("\nEnter ID to Delete: ")
    global farm_records
    farm_records = [record for record in farm_records if record.farm_id != delete_id]
    print("Record deleted successfully!")


def sort_records():
    farm_records.sort(key=lambda record: record.name.lower())
    print("\nRecords sorted by Name!")
    display_all()

# Menu-Driven Interface
def menu():
    while True:
        print("\nFarm Management System")
        print("1. Add a New Record")
        print("2. Display All Records")
        print("3. Search for a Record by ID")
        print("4. Update a Record")
        print("5. Delete a Record by ID")
        print("6. Sort Records")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_record()
            elif choice == 2:
                display_all()
            elif choice == 3:
                search_record()
            elif choice == 4:
                update_record()
            elif choice == 5:
                delete_record()
            elif choice == 6:
                sort_records()
            elif choice == 7:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Try again!")
        except ValueError:
            print("Invalid input. Enter a number.")


# Run the Program
if __name__ == "__main__":
    menu()
    
    
     
# End of Program