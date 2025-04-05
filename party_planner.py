import cgi

# Lista de ítems
party_items = [
    "Cake", "Balloons", "Music System", "Lights", "Catering Service", "DJ", "Photo Booth",
    "Tables", "Chairs", "Drinks", "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
]

# Valores asignados a cada ítem
party_values = [
    20, 21, 10, 5, 8, 3, 15,
    7, 12, 6, 9, 18, 4, 2, 11
]

# Obtener parámetros del formulario
form = cgi.FieldStorage()
selected_indices = form.getvalue("items")

print("Content-Type: text/html\n")

if not selected_indices:
    print("<h2>No items were selected!</h2>")
else:
    try:
        indices = [int(i.strip()) for i in selected_indices.split(",")]
        selected_names = [party_items[i] for i in indices]
        selected_values = [party_values[i] for i in indices]

        base_code = selected_values[0]
        for val in selected_values[1:]:
            base_code &= val

        # Ajustar el código base
        final_code = base_code
        if base_code == 0:
            final_code += 5
            message = "Epic Party Incoming!"
        elif base_code > 5:
            final_code -= 2
            message = "Let's keep it classy!"
        else:
            message = "Chill vibes only!"

        # Mostrar el resultado en HTML
        print("<h2>Selected Items:</h2>")
        print(", ".join(selected_names))
        print(f"<h3>Base Party Code: {base_code}</h3>")
        print(f"<h3>Final Party Code: {final_code}</h3>")
        print(f"<p><strong>Message:</strong> {message}</p>")

    except Exception as e:
        print(f"<p>Error: {e}</p>")
