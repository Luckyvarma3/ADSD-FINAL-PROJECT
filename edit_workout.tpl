<!-- views/edit_workout.tpl -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Workout</title>
</head>
<body>
    <h1>Edit Workout</h1>

    <form action="/update_workout/{{ workout['id'] }}" method="post">
        <label for="customer_id">Customer ID:</label>
        <input type="text" id="customer_id" name="customer_id" value="{{ workout['customer_id'] }}" required>
        <label for="hours">Workout Hours:</label>
        <input type="text" id="hours" name="hours" value="{{ workout['hours'] }}" required>
        <label for="bottle_module">Bottle Module:</label>
        <input type="text" id="bottle_module" name="bottle_module" value="{{ workout['bottle_module'] }}">
        <button type="submit">Save Changes</button>
    </form>

    <p><a href="/workouts">Back to Workouts</a></p>
</body>
</html>
