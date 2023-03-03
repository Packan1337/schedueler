from modules import *
from transferer import *


class Window:
    def main_window():
        layout = [
            [sg.Text("PACKAN'S SCHEDUELER", font=("Arial", 45),
                     enable_events=True, key="-PACKAN_GITHUB-")],
            [sg.Text("")],
            [sg.Push(),
             sg.Text("Employee", font=("Arial", 14)),
             sg.Combo(["Alicia", "Aria", "Gul", "Katja", "Lina"],
                      font=("Arial", 14), key="-EMPLOYEE-"),
             sg.Push(),
             sg.FileBrowse("SELECT A FILE", font=(
                 "Arial", 14), key="-SELECTOR-"),
             sg.Button("CONVERT TO CALENDAR", font=(
                 "Arial", 14), key="-CONVERT-"),
             sg.Push()]
        ]

        window = sg.Window("Packan's Schedueler", layout)

        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Cancel":
                break

            elif event == "-PACKAN_GITHUB-":
                webbrowser.open("https://github.com/Packan1337/schedueler")

            elif event == "-CONVERT-":
                print("got here")
                Window.verify_window(
                    file_to_verify=values["-SELECTOR-"], employee=values["-EMPLOYEE-"])

        window.close()

    def success_window():
        layout = [
            [sg.Push(), sg.Text("Successfully added events to calendar!",
                                font=("Arial", 14)), sg.Push()],
            [sg.Push(), sg.Button("OK", font=("Arial", 14), key="-OK-"), sg.Push()]
        ]

        window = sg.Window("Success!", layout, modal=True)

        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "-OK-":
                break

    def verify_window(file_to_verify, employee):
        layout = [
            [sg.Text(f"Do you want to use {os.path.basename(file_to_verify)}?", font=(
                "Arial", 14))],
            [sg.Push(),
             sg.Button("YES", font=("Arial", 14), key="-YES-"),
             sg.Button("NO", font=("Arial", 14), key="-NO-"),
             sg.Push()]
        ]

        window = sg.Window("Packan's Schedueler", layout, modal=True)

        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Cancel":
                break

            elif event == "-YES-":
                Event.create_event(Event.extractor(file_to_verify, employee))
                break

            elif event == "-NO-":
                break

        window.close()
