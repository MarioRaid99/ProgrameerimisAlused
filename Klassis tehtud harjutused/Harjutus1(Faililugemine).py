import csv


def read_file_contents(filename: str) -> str:
    """Read file contents into string."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def read_file_contents_to_list(filename: str) -> list:
    """Read file contents into list of lines."""
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def read_csv_file(filename: str) -> list:
    """Read CSV file into list of rows."""
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return [row for row in reader]


def write_contents_to_file(filename: str, contents: str) -> None:
    """Write contents to file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """Write lines to file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def write_csv_file(filename: str, data: list) -> None:
    """Write data into CSV file."""
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """Merge information from two files into one CSV file."""
    dates = {}
    with open(dates_filename, "r", encoding="utf-8") as file:
        for line in file:
            name, date = line.strip().split(":")
            dates[name] = date

    towns = {}
    with open(towns_filename, "r", encoding="utf-8") as file:
        for line in file:
            name, town = line.strip().split(":")
            towns[name] = town

    merged_data = [("name", "town", "date")]
    for name in dates:
        merged_data.append((name, towns.get(name, "-"), dates[name]))
    for name in towns:
        if name not in dates:
            merged_data.append((name, towns[name], "-"))

    write_csv_file(csv_output_filename, merged_data)