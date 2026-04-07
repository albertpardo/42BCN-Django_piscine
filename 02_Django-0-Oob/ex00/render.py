import sys
import os
import settings

def render_template(template_file):

    with open(template_file, "r") as f:
        content = f.read()

    try:
        rendered = content.format(**settings.__dict__)
    except KeyError as e:
        raise KeyError(f"Variable {e} not found in settings.py")

    html_file = template_file.replace(".template", ".html")

    with open(html_file, "w") as f:
        f.write(rendered)

    return html_file


if __name__ == '__main__':

    # Check argument number
    if len(sys.argv) != 2:
        print("Usage: render.py <file.template>")
        sys.exit(1)

    template_file = sys.argv[1]

    # Check extension
    if not template_file.endswith(".template"):
        print(f"Error: file '{template_file}' must have .template extension")
        sys.exit(1)

    # Check file exists
    if not os.path.exists(template_file):
        print(f"Error: file '{template_file}' does not exist")
        sys.exit(1)

    try:
        html = render_template(template_file)
        print(f"HTML file generated: {html}")

    except KeyError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
