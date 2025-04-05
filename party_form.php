<!DOCTYPE html>
<html>
<head>
    <title>Party Planner</title>
</head>
<body>
    <h1>Select Your Party Items</h1>
    <form action="party_result.php" method="post">
        <?php
        $items = [
            "Cake", "Balloons", "Music System", "Lights", "Catering Service", "DJ", "Photo Booth",
            "Tables", "Chairs", "Drinks", "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
        ];

        foreach ($items as $index => $item) {
            echo "<input type='checkbox' name='items[]' value='$index'> $index: $item<br>";
        }
        ?>
        <br>
        <input type="submit" value="Plan Party">
    </form>
</body>
</html>
