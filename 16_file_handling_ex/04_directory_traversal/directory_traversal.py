import os


def get_files(folder: str, level: int):
    if level == 0:
        return

    for file in os.listdir(folder):
        file_or_dir = os.path.join(folder, file)

        if os.path.isfile(file_or_dir):
            extension = os.path.splitext(file_or_dir)[1]

            if extension not in files_for_report:
                files_for_report[extension] = []
            files_for_report[extension].append(file)
        else:
            get_files(file_or_dir, level - 1)


files_for_report = {}
directory = "../"

get_files(directory, 2)

with open("report.txt", "w") as report:
    for ext, files in sorted(files_for_report.items()):
        report.write(f"{ext}\n")

        for name in sorted(files):
            report.write(f"- - - {name}\n")
