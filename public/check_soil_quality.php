<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $ph = $_POST['ph'];
    $moisture = $_POST['moisture'];
    $nutrients = $_POST['nutrients'];
    $soil_type = $_POST['soil_type'];
    $last_crop = $_POST['last_crop'];
    $weather_type = $_POST['weather_type'];

    // Create data array
    $data = json_encode(array(
        'ph' => $ph,
        'moisture' => $moisture,
        'nutrients' => $nutrients,
        'soil_type' => $soil_type,
        'last_crop' => $last_crop,
        'weather_type' => $weather_type
    ));

    // Send POST request to Flask API
    $options = array(
        'http' => array(
            'header'  => "Content-Type: application/json\r\n",
            'method'  => 'POST',
            'content' => $data,
        ),
    );
    $context  = stream_context_create($options);
    $result = @file_get_contents('http://127.0.0.1:5000/predict', false, $context);

    if ($result === FALSE) {
        $error = error_get_last();
        die('Error: ' . $error['message']);
    }

    $response = json_decode($result, true);

    // Display the result
    echo "<div class='container'>";
    echo "<h2>Recommended Crop</h2>";
    if (isset($response['error'])) {
        echo "<p>Error: <strong>{$response['error']}</strong></p>";
    } else {
        echo "<p>The recommended crop for you is: <strong>{$response['prediction']}</strong></p>";
    }
    echo "</div>";
}
?>


<?php include 'header.php'; ?>
<h2>Find the Best Crop to Plant</h2>
<div id="publicId">Some Content</div>

<form method="POST" action="check_soil_quality.php">
    <label for="ph">pH Level:</label>
    <input type="text" id="ph" name="ph" required><br>
    <label for="moisture">Moisture Level:</label>
    <input type="text" id="moisture" name="moisture" required><br>
    <label for="nutrients">Nutrient Level:</label>
    <input type="text" id="nutrients" name="nutrients" required><br>
    <label for="soil_type">Soil Type:</label>
    <select id="soil_type" name="soil_type" required>
        <option value="Loamy">Loamy</option>
        <option value="Clay">Clay</option>
        <option value="Sandy">Sandy</option>
    </select><br>
    <label for="last_crop">Last Crop:</label>
    <select id="last_crop" name="last_crop" required>
        <option value="Tomato">Tomato</option>
        <option value="Lettuce">Lettuce</option>
        <option value="Wheat">Wheat</option>
        <option value="Corn">Corn</option>
        <option value="Barley">Barley</option>
    </select><br>
    <label for="weather_type">Weather Type:</label>
    <select id="weather_type" name="weather_type" required>
        <option value="Sunny">Sunny</option>
        <option value="Rainy">Rainy</option>
        <option value="Cloudy">Cloudy</option>
    </select><br>
    <button type="submit">Get Recommended Crop</button>
</form>
