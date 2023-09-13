import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/tasks"


def update_task(summary, description, new_task_id):
    task_data = {
        "summary": summary,
        "description": description
    }
    url = "%s/%s" % (URL, new_task_id)
    response = requests.put(url, json=task_data)
    if response.status_code == 204:
        pprint("Task updated successfully.")
    else:
        pprint("Task update failed.")


if __name__ == "__main__":
    print("Update a new task: ")
    new_task_id = input("Which task do you want to update?")
    summary = input("Summary: ")
    description = input("Description: ")
    update_task(summary, description)