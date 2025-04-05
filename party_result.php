<?php
$selected = isset($_GET['items']) ? $_GET['items'] : [];

if (empty($selected)) {
    echo "<p>No items selected.</p>";
    exit;
}

// Convertimos el array a string separado por comas
$indices = implode(",", $selected);

// Ejecutamos el script Python con los parámetros
$command = escapeshellcmd("python3 party_planner.py items=" . escapeshellarg($indices));
$output = shell_exec($command);

// Mostrar el resultado
echo $output;
?>
