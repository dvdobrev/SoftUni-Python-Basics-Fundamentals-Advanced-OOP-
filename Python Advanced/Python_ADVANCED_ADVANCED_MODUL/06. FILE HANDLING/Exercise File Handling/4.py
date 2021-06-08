import os
from pathlib import Path

def get_report_for_extensions(files):
    report = {}
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report

dir_content = os.listdir()

files = [el for el in dir_content if os.path.isfile(el)]
report_info = get_report_for_extensions(files)

result_str = ""
for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    result_str += f"{extension}\n"
    for name in file_names:
        result_str += f"--- {name}{extension}\n"

path_to_desktop_file = os.path.join(os.environ["USERPROFILE"], "Desktop", "report.txt")
with open(path_to_desktop_file, "a") as file:
    file.write(result_str)