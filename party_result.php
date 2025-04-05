<?php
if (isset($_POST['items'])) {
    $selected = implode(",", $_POST['items']);
    $output = shell_exec("python3 party_planner.py items=$selected");
    echo $output;
} else {
    echo "<h2>No items selected!</h2>";
}
?>
