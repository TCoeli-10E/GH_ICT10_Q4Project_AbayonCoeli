from pyscript import display
from js import document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

classmates = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
absences = np.zeros(len(days), dtype=int)

def clear_output():
    output_element = document.getElementById("output")
    if output_element is None:
        return
    output_element.innerHTML = ""


def render_classmates():
    clear_output()
    if not classmates:
        display("<p>No classmates added yet.</p>", target="output")
        return

    display("<p>List of classmates:</p>", target="output")
    for item in classmates:
        display(
            f"Hi! I am {item['name']}. From {item['section']}. "
            f"My favorite subject is {item['subject']}.",
            target="output"
        )


def any_sample(event=None):
    name = document.getElementById("input1").value.strip() or "Unknown"
    section = document.getElementById("input2").value.strip() or "Unknown"
    subject = document.getElementById("input3").value.strip() or "Unknown"

    classmates.append({
        "name": name,
        "section": section,
        "subject": subject,
    })
    render_classmates()


def update_graph():
    clear_output()
    plt.figure()
    plt.plot(days, absences, marker="o", linestyle="-", color="blue")
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid(True)
    display(plt, target="output")
    plt.close()


def handle_submit(event):
    event.preventDefault()
    day = document.getElementById("day").value
    number = int(document.getElementById("absences").value)
    if day in days:
        absences[days.index(day)] = number
    update_graph()

attendance_form = document.getElementById("attendance-form")
if attendance_form is not None:
    attendance_form.onsubmit = handle_submit
    update_graph()
else:
    render_classmates()



