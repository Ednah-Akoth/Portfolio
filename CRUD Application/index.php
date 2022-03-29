<?php
// Connection to database
include 'db_config.php';

// write query for all users
$sql = 'SELECT username, password FROM users'; //all columns from table pizza
//make query and get result
$result = mysqli_query($conn, $sql);

//Fetch the resulting rows  as an array
$users = mysqli_fetch_all($result, MYSQLI_ASSOC); // We are getting it back as an associative array
// print_r($users);
//Result: Array ( [0] => Array ( [username] => edakoth [password] => 12898 ) [1] => Array ( [username] => adamaAlu [password] => whynot2 ) )
//Free result from memory
mysqli_free_result($result);
//Close connection
mysqli_close($conn);

//Here, we will validate the form in terms of correctness of the input
$username = $password = $general = ""; //initialize to empty to avoid errors before the form is run
$errors = array('username' => '', 'password' => '', 'general' => '');

//ChECKING USERNAME
if (isset($_POST['submit'])) {
    // Checking if the user has entered data
    if (empty($_POST['username'])) {
        $errors['username'] = 'username is required';
    } else {
        $username = $_POST['username'];
        if (!preg_match('/^[a-zA-Z0-9]+$/', $username)) {
            $errors['username'] = 'username should only contain lowercase letters a-z, uppercase letters A-Z, and numbers 0-9.';
        }

    }
//CHECKING PASSWORD

    if (empty($_POST['password'])) {
        $errors['password'] = 'password is required';
    } else {
        $password = $_POST['password'];
    }

    //WRITE A FOR LOOP
    for ($i = 0; $i < count($users); $i++) {

        if ($username == $users[$i]['username'] && $password == $users[$i]['password']) {
            header('location: main_admin.php');
        } else {
            $errors['general'] = 'Incorrect username or password';
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
    <title>Log In</title>
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
      <div class="d-flex justify-content-center">
        <img class="" src="./assets/img/angel.png" alt="" />
      </div>
      <form action="index.php" method='POST'>
        <!-- Error shown when username or password is wrong -->
        <div class="red-text"><?php echo $errors['general'] ?></div>
        <!-- Username -->
        <div class="mb-3">
          <input
            type="text"
            id="user"
            name="username"
            placeholder="Username"
            value="<?php echo htmlspecialchars($username) ?>"
          />
          <div class="red-text"><?php echo $errors['username'] ?></div>
        </div>
        <!-- Password -->
        <div class="mb-3">
          <input type="password" id="pwd" name="password" placeholder="Password" value = "<?php echo htmlspecialchars($password) ?>" />
          <div class="red-text"><?php echo $errors['password'] ?></div>
        </div>

       <!-- Confirm button -->

        <div class="mb-3 d-flex justify-content-center">
          <button type="submit" name="submit" value="submit" class="btn">Log In</button>          
        </div>

        <div>
            <p class="other_btn"><a href="signup.php" >Create Account</a></p>
            <p class="other_btn"><a href="main.php" >Continue as Guest</a></p>
        </div>
      </form>
    </div>
    <footer class="footer">
      <p>Designed with &#10084; by Group 18.</p>
    </footer>
  </body>
</html>
