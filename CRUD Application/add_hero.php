<?php
// Connection to database
include 'db_config.php';
//INITIALIZING THE VARIABLES to empty to avoid errors before the form is run
$name = $real_name = $short_bio = $long_bio = $hero_img = "";
$errors = array('name' => '', 'real_name' => '', 'short_bio' => '', 'long_bio' => '', 'hero_img' => '');

if (isset($_POST['submit'])) {
    //CHECK name
    if (empty($_POST['name'])) {
        $errors['name'] = "Hero's name is required";
    } else {
        $name = $_POST['name'];
    }

    //CHECK real_name
    if (empty($_POST['real_name'])) {
        $errors['real_name'] = "Hero's Real name is required";
    } else {
        $real_name = $_POST['real_name'];

    }

    //CHECK short bio
    if (empty($_POST['short_bio'])) {
        $errors['short_bio'] = "Hero's Short Bio is required";
    } else {
        $short_bio = $_POST['short_bio'];
    }
    //CHECK long bio
    if (empty($_POST['long_bio'])) {
        $errors['long_bio'] = "Hero's Long Bio is required";
    } else {
        $long_bio = $_POST['long_bio'];
    }

    //Uploading form content if there are no errors
    if (array_filter($errors)) {

    } else { //post them into the database
        $name = mysqli_real_escape_string($conn, $_POST['name']);
        $real_name = mysqli_real_escape_string($conn, $_POST['real_name']);
        $short_bio = mysqli_real_escape_string($conn, $_POST['short_bio']);
        $long_bio = mysqli_real_escape_string($conn, $_POST['long_bio']);

        //create sql
        $sql = "INSERT INTO heroes(name,real_name,short_bio,long_bio) VALUES('$name', '$real_name', '$short_bio','$long_bio')";
        //Save to db and check
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

    <form action="add_hero.php" method='POST'>

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
          <div class="red-text"><?php echo $errors['name'] ?></div>
        </div>
        <!-- REAL HERO NAME -->
        <div class="mb-3">
            <label class="form-label" for="form4Example3">Real Name</label>
            <input
            type="text"
            id="user"
            name="real_name"
            placeholder="Enter the hero's real name"
            value="<?php echo htmlspecialchars($real_name) ?>"/>
            <div class="red-text"><?php echo $errors['real_name'] ?></div>
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
            value="<?php echo htmlspecialchars($short_bio) ?>"/>

            <div class="red-text"><?php echo $errors['short_bio'] ?></div>
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
            value="<?php echo htmlspecialchars($long_bio) ?>"/>

            <div class="red-text"><?php echo $errors['long_bio'] ?></div>
        </div>


        <!-- Adding Hero Image
        <div>
            <label for="image">Choose a hero image</label><br>
            <input type="file" name="hero_img" id="hero_img" accept=".jpg, .jpeg, .png"/><br>
            <div class="red-text"><?php echo $errors['hero_img'] ?></div>
        </div>
         -->

       <!-- Confirm button -->
        <div class="mb-3 d-flex justify-content-center">
          <button type="submit" name="submit" value="submit" class="btn">Create</button>
        </div>

    </form>
    </div>
    <footer class="footer">
      <p>Designed with &#10084; by Group 18.</p>
    </footer>
  </body>
</html>
