#!/usr/bin/env python3

import cgi
import os

party_items = [
    "Cake", "Balloons", "Music System", "Lights", "Catering Service", "DJ", "Photo Booth",
    "Tables", "Chairs", "Drinks", "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
]

party_values = [
    20, 21, 10, 5, 8, 3, 15,
    7, 12, 6, 9, 18, 4, 2, 11
]

# Get inputs from environment or CGI
query = os.environ.get("QUERY_STRING", "")
items_str = ""
if "items=" in query:
    items_str = query.split("items=")[-1].replace("%2C", ",")

print("Content-Type: text/html\n")
print("<pre>")  # Maintain formatting

# Show available party items
print("Available Party Items:\n")
for index, item in enumerate(party_items):
    print(f"{index}: {item}")
print("\n")

print("Enter item indices separated by commas (e.g., 0, 2):", items_str)
print("\n")

if not items_str:
    print("No items were selected.")
else:
    try:
        indices = [int(i.strip()) for i in items_str.split(",") if i.strip().isdigit()]
        selected_names = [party_items[i] for i in indices]
        selected_values = [party_values[i] for i in indices]

        base_code = selected_values[0]
        for val in selected_values[1:]:
            base_code &= val

        # Adjust final code
        final_code = base_code
        adjust_info = ""
        if base_code == 0:
            final_code += 5
            adjust_info = f"{base_code} + 5 = {final_code}"
            message = "Epic Party Incoming!"
        elif base_code > 5:
            final_code -= 2
            adjust_info = f"{base_code} - 2 = {final_code}"
            message = "Let's keep it classy!"
        else:
            adjust_info = f"{base_code} (no change)"
            message = "Chill vibes only!"

        print("Selected Items:", ", ".join(selected_names))
        print(f"Base Party Code: {' & '.join(str(v) for v in selected_values)} = {base_code}")
        print(f"Adjusted Party Code: {adjust_info}")
        print(f"Final Party Code: {final_code}\n")
        print("Message:", message)

    except Exception as e:
        print("Error:", e)

print("</pre>")
