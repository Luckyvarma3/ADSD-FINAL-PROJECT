<!-- views/trainers.tpl -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gym Trainers</title>
</head>
<body>
    <h1>Gym Trainers</h1>
    
    <ul>
        % for trainer in trainers:
            <li>{{ trainer['name'] }} <a href="/edit_trainer/{{ trainer['id'] }}">Edit</a> <a href="/delete_trainer/{{ trainer['id'] }}">Delete</a></li>
        % end
    </ul>

    <form action="/add_trainer" method="post">
        <label for="name">Trainer Name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Add Trainer</button>
    </form>
    
    <p><a href="/">Back to Home</a></p>
</body>
</html>
