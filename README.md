# 🌱 Farm Management System

A **Python-based Farm Management System** that uses **Object-Oriented Programming (OOP)** to manage farm resources such as **animals, crops, equipment, and workers** through a simple, interactive command-line interface.

---

## 📌 Features

- ✅ Add new records for animals, crops, equipment, and workers  
- ✅ Display all farm records  
- ✅ Search for a specific record by ID  
- ✅ Update selected attributes based on the record type  
- ✅ Delete records using their unique ID  
- ✅ Sort all records alphabetically by name  
- ✅ Fully menu-driven terminal interface  

---

## 🧱 Object-Oriented Structure

| Class      | Description                                            |
|------------|--------------------------------------------------------|
| `Farm`     | Base class containing common attributes like ID and name |
| `Animal`   | Inherits from `Farm\`; adds species and age             |
| `Crop`     | Inherits from `Farm`; adds crop type and harvest time   |
| `Equipment`| Inherits from `Farm`; adds equipment type and condition |
| `Worker`   | Inherits from `Farm`; adds role and salary              |

Each subclass implements its own version of the `display_details()` method.

---

## 🚀 Getting Started

### 📁 Clone the Repository

```
bash
git clone https://github.com/YOUR_USERNAME/Farm-Management-System.git
cd Farm-Management-System
```

### ▶️ Run the Program

Make sure you have Python installed. Then run:

```
bash
python main.py
```

---

## 🎓 Learning Objectives

This project demonstrates key Python and OOP concepts:

- Inheritance and polymorphism  
- Encapsulation of class attributes  
- CRUD operations with dynamic lists  
- Building CLI menus and user input validation  

---

## 📌 Example Menu

```
Farm Management System
1. Add a New Record
2. Display All Records
3. Search for a Record by ID
4. Update a Record
5. Delete a Record by ID
6. Sort Records
7. Exit
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contributing

Pull requests and suggestions are welcome! If you have ideas to improve the system or want to add file-saving features, feel free to fork the repo and open a PR.

---

## 📫 Contact

Made with ❤️ by [Ziyad Azzaz]  
GitHub: [https://github.com/YOUR_USERNAME](https://github.com/ZiyadAzzaz)
