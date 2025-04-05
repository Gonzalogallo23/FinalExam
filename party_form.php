<!DOCTYPE html>
<html>
<head>
    <title>Digital Party Planner</title>
</head>
<body>
    <h2>Select Your Party Items</h2>
    <form action="party_result.php" method="get">
        <p>Select one or more party items:</p>
        <?php
        $items = [
            "Cake", "Balloons", "Music System", "Lights", "Catering Service", "DJ", "Photo Booth",
            "Tables", "Chairs", "Drinks", "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
        ];
        foreach ($items as $index => $item) {
            echo "<label><input type='checkbox' name='items[]' value='$index'> $item</label><br>";
        }
        ?>
        <br>
        <input type="submit" value="Plan Party">
    </form>
</body>
</html>
