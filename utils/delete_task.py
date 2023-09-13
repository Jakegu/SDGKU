import requests

URL = "http://127.0.0.1:5000/tasks"


def delete_task(URL):
    
    response = requests.delete(URL)
    if response.status_code == 204:
        print("Task deleted successfully.")
    else:
        print("Task deletion failed.")


if __name__ == "__main__":
    print("Delete a task: ")
    delete_task(URL)