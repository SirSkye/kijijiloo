from fastapi import FastAPI, HTTPException
app = FastAPI()

# dummy 'DB'
tasks = {
    "1": {
        "category": "food",
        "status": "open",
        "location": "UTD",
        "ID": "001",
        "title": "Pizza delivery needed",
        "description": "Need someone to pick up pizza from Dominos"
    },
    "2": {
        "category": "food",
        "status": "open",
        "location": "Richardson",
        "ID": "002",
        "title": "Grocery shopping help",
        "description": "Need help with weekly grocery shopping"
    },
    "3": {
        "category": "transportation",
        "status": "closed",
        "location": "Plano",
        "ID": "003",
        "title": "Ride to airport",
        "description": "Need ride to DFW airport on Friday morning"
    },
    "4": {
        "category": "moving",
        "status": "open",
        "location": "Dallas",
        "ID": "004",
        "title": "Moving boxes",
        "description": "Need help moving boxes to new apartment"
    },
    "5": {
        "category": "cleaning",
        "status": "in_progress",
        "location": "UTD",
        "ID": "005",
        "title": "Dorm room cleaning",
        "description": "Looking for someone to help clean dorm room"
    },
    "6": {
        "category": "food",
        "status": "open",
        "location": "Frisco",
        "ID": "006",
        "title": "Meal prep assistance",
        "description": "Need help preparing meals for the week"
    },
    "7": {
        "category": "tutoring",
        "status": "open",
        "location": "UTD",
        "ID": "007",
        "title": "Math tutoring needed",
        "description": "Need help with Calculus 2"
    },
    "8": {
        "category": "delivery",
        "status": "closed",
        "location": "Richardson",
        "ID": "008",
        "title": "Package pickup",
        "description": "Need someone to pick up package from post office"
    },
    "9": {
        "category": "pet_care",
        "status": "open",
        "location": "Dallas",
        "ID": "009",
        "title": "Dog walking",
        "description": "Need someone to walk my dog twice daily"
    },
    "10": {
        "category": "tech_help",
        "status": "open",
        "location": "UTD",
        "ID": "010",
        "title": "Computer repair",
        "description": "Laptop won't turn on, need tech support"
    },
    "11": {
        "category": "food",
        "status": "in_progress",
        "location": "Plano",
        "ID": "011",
        "title": "Restaurant pickup",
        "description": "Pick up dinner from local restaurant"
    },
    "12": {
        "category": "yard_work",
        "status": "open",
        "location": "Richardson",
        "ID": "012",
        "title": "Lawn mowing",
        "description": "Need lawn mowed this weekend"
    },
    "13": {
        "category": "assembly",
        "status": "open",
        "location": "Frisco",
        "ID": "013",
        "title": "Furniture assembly",
        "description": "Need help assembling IKEA furniture"
    },
    "14": {
        "category": "transportation",
        "status": "open",
        "location": "Dallas",
        "ID": "014",
        "title": "Carpool to campus",
        "description": "Looking for carpool partner to UTD"
    },
    "15": {
        "category": "cleaning",
        "status": "closed",
        "location": "UTD",
        "ID": "015",
        "title": "Apartment cleaning",
        "description": "Deep cleaning needed before move-out"
    },
    "16": {
        "category": "shopping",
        "status": "open",
        "location": "Plano",
        "ID": "016",
        "title": "Gift shopping help",
        "description": "Need help finding birthday gift"
    },
    "17": {
        "category": "food",
        "status": "open",
        "location": "UTD",
        "ID": "017",
        "title": "Coffee run",
        "description": "Quick coffee pickup from Starbucks"
    },
    "18": {
        "category": "event_help",
        "status": "in_progress",
        "location": "Richardson",
        "ID": "018",
        "title": "Party setup",
        "description": "Need help setting up for birthday party"
    },
    "19": {
        "category": "laundry",
        "status": "open",
        "location": "Dallas",
        "ID": "019",
        "title": "Laundry assistance",
        "description": "Need help with laundry pickup and drop-off"
    },
    "20": {
        "category": "study_help",
        "status": "open",
        "location": "UTD",
        "ID": "020",
        "title": "Study group partner",
        "description": "Looking for study partner for finals week"
    }
}

# get list of tasks
@app.get("/tasks")
def view_tasks():
    values = list(tasks.values())  # only task info idk why
    return tasks


# get specific task
@app.get("/task/{task_id}")
def get_task(task_id: str):
    keys_list = list(tasks.keys())
    return tasks[task_id]

# create a task
@app.post("/create")
def make_task(category: str, title: str, location: str, desc: str):
    keys_list = list(tasks.keys())
    listof_attributes = {"category": category, "status": "open", "location": location, "ID": "stand-in", "title": title, "description": desc}
    task_id = str(1 + int(keys_list[-1]))
    tasks[task_id] = listof_attributes
    return tasks
# notes^: need to add in user ID once ID generation code is complete

@app.patch("/task/{task_id}/status")
def change_status(task_id: str, status: str):
    if status != "open" || status != "cancelled" || status != "completed":
        raise HTTPException(status_code = 400, detail = "status not found")
    else 