<?php

include 'db_config.php';

// if the form's update button is clicked, we need to process the form

if (isset($_POST['update'])) {
    $id = $_POST['id'];
    $name = $_POST['name'];
    $real_name = $_POST['real_name'];
    $short_bio = $_POST['short_bio'];
    $long_bio = $_POST['long_bio'];

    // write the update query
    try {
        $sql = "UPDATE heroes SET name = '$name', real_name = '$real_name', short_bio = '$short_bio', long_bio = '$long_bio' WHERE id = $id";

    } catch (Exception $e) {
        $e->getMessage();
        exit;
    }

    if (mysqli_query($conn, $sql)) {
        //If connection successful
        //Redirect them to the heros page
        echo '<script type="text/javascript"> alert("Hero Added!")</script>';
        header('Location: main_admin.php');
    } else {
        //if there is an error, print it out
        echo 'query error: ' . mysqli_error($conn);
    }

}

// if the 'id' variable is set in the URL, we know that we need to edit a record
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    // write SQL to get user data
    $sql = "SELECT * FROM heroes WHERE id = $id ";
    //Execute the sql
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $name = $row['name'];
            $real_name = $row['real_name'];
            $short_bio = $row['short_bio'];
            $long_bio = $row['long_bio'];
            $id = $row['id'];
        }

    }

}

?>


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />

    <link href="./assets/css/style1.css" rel="stylesheet" type="text/css" />
    <title>Add Hero</title>
  </head>

  <body>
    <header class="header">
      <nav class="nav">
        <div class="navbar-brand">
          <img src="./assets/img/x-logo.png" class="logo padding-1" />
        </div>
      </nav>
    </header>
    <div
      class="contact-form m-5 d-flex flex-column align-items-center justify-content-center"
    >

    <form action="edit_hero.php" method='POST'>

        <!-- HERO NAME -->
        <div class="mb-3">
            <label class="form-label" for="form4Example3">Hero Name</label>
          <input
            type="text"
            id="user"
            name="name"
            placeholder="Enter hero name"
            value="<?php echo htmlspecialchars($name) ?>"
          />
          <input type="hidden" name="id" value="<?php echo $id; ?>">

        </div>
        <!-- REAL HERO NAME -->
        <div class="mb-3">
            <label class="form-label" for="form4Example3">Real Name</label>
            <input
            type="text"
            id="user"
            name="real_name"
            placeholder="Enter the hero's real name"
            value="<?php echo htmlspecialchars($real_name); ?>"/>

        </div>

        <!-- Short Bio -->
        <div class="form-outline mb-4">
            <label class="form-label" for="form4Example3">Short Bio</label>
            <input
            type="text"
            id="user"
            name="short_bio"
            placeholder="Enter the hero's short bio"
            size="50"
            value="<?php echo htmlspecialchars($short_bio); ?>"/>


        </div>
        <!-- Long Bio -->
        <div class="form-outline mb-4">
            <label class="form-label" for="form4Example3">Long Bio</label>
            <input
            type="text"
            id="user"
            name="long_bio"
            placeholder="Enter the hero's long bio"
            size="50"
            value="<?php echo htmlspecialchars($long_bio); ?>"/>


        </div>



       <!-- Confirm button -->
        <div class="mb-3 d-flex justify-content-center">
          <button type="submit" name="update" value="update" class="btn">Update</button>
        </div>

    </form>
    </div>
    <footer class="footer">
      <p>Designed with &#10084; by Group 18.</p>
    </footer>
  </body>
</html>