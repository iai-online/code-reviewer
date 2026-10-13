import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def first_text(response):
  """Returns the text of the first text block in the Messages API response."""
  for block in response.content:
    if block.type == "text":
      return block.text
  return ""

def parse_diff(diff_text: str):
  """
  Maps each file in a unified diff to the new-file line numbers it shows.
  
  Returns a dictionary like {"app/orders.py": {12, 13, 14, 15}}.
  Added lines and context lines both count, because both are visible in the diff. 
  """
  visible = {}
  current_file = None
  new_line = 0
  for line in diff_text.splitlines():
    if line.startswith("+++ "):
      current_file = line[4:].strip()
      if current_file.startswith("b/"):
        current_file = current_file[2:]
      visible[current_file] = set()
    elif line.startswith("@@"):
      match = re.search(r"\+(\d+)", line)   # @@ -15,7 +15,7 @@
      if match:
        new_line = int(match.group(1))
    elif current_file is None or line.startswith("---"):
      continue
    elif line.startswith("+") or line.startswith(" "):
      visible[current_file].add(new_line)
      new_line += 1
    # Lines that start with "-" exist only in the old file, so they are skipped

  return visible