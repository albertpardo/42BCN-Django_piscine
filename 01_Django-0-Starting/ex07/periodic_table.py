def get_element_from_line(line):
    name, rest = line.split(" = ")
    attributes = rest.split(", ")

    data = {}
    for attr in attributes:
        key, value = attr.split(":")
        data[key.strip()] = value.strip()
    data["position"] = int(data["position"])
    element = {"name": name}
    element.update(data)

    return element


def read_elements(filename):
    elements = []

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        if line:
            elements.append(get_element_from_line(line))

    return elements


def build_rows(elements):
    rows = []
    current_row = []

    for element in elements:
        if element["position"] == 0 and current_row:
            rows.append(current_row)
            current_row = []
        current_row.append(element)
    if current_row:
        rows.append(current_row)

    return rows


def create_cell(element):
    html = ""
    html += '        <td style="border:1px solid black; padding:10px; text-align:center;">\n'
    html += "          <h4>" + element["name"] + "</h4>\n"
    html += "          <ul>\n"
    html += "            <li>No " + element["number"] + "</li>\n"
    html += "            <li>" + element["small"] + "</li>\n"
    html += "            <li>" + element["molar"] + "</li>\n"
    html += "            <li>" + element["electron"] + " electron</li>\n"
    html += "          </ul>\n"
    html += "        </td>\n"

    return html


def generate_html(rows, filename):
    f = open(filename, "w")
    
    f.write("<!DOCTYPE html>\n")
    f.write('<html lang="en">\n')
    f.write("  <head>\n")
    f.write('    <meta charset="utf-8">\n')
    f.write("    <title>Periodic Table</title>\n")
    f.write("  </head>\n")
    f.write("  <body>\n")
    f.write('    <table style="border-collapse:collapse;">\n')
    for row in rows:
        f.write("      <tr>\n")
        columns = ['        <td style="border:1px solid black; padding:10px;"></td>\n'] * 18
        for element in row:
            columns[element["position"]] = create_cell(element)
        for cell in columns:
            f.write(cell)
        f.write("      </tr>\n")
    f.write("    </table>\n")
    f.write("  </body>\n")
    f.write("</html>\n")

    f.close()


def periodic_table():

    html_file = "periodic_table.html"
    data_file = "../d01/ex07/periodic_table.txt"

    elements = read_elements(data_file)
    rows = build_rows(elements)
    generate_html(rows, html_file)


if __name__ == '__main__':
    periodic_table()
