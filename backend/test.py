from fastapi import FastAPI
app = FastAPI()

# dummy 'DB'
tasks = {
    "001": [{"category": "food",
                "status": "open",
                 "location": "UTD",
                  "ID": "001" }],
    "002": [{"category": "food",
                "status": "open",
                 "location": "UTD",
                  "ID": "001" }],
}

# get list of tasks
@app.get("/tasks")
def view_tasks():
    values = list(tasks.values())  # only task info idk why
    return tasks


# get specific task
@app.get("/task{task_id}")
def get_task(task_id: int):
    for i in list(tasks.keys()):
        if i == task_id:
            return tasks

# 