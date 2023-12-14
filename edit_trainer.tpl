<!-- views/edit_trainer.tpl -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Trainer</title>
</head>
<body>
    <h1>Edit Trainer</h1>

    <form action="/update_trainer/{{ trainer['id'] }}" method="post">
        <label for="name">Trainer Name:</label>
        <input type="text" id="name" name="name" value="{{ trainer['name'] }}" required>
        <button type="submit">Save Changes</button>
    </form>

    <p><a href="/trainers">Back to Trainers</a></p>
</body>
</html>
