<?php
session_start();
include 'db_config.php';
$name = $real_name = $short_bio = $long_bio = "";

// IS IN USE BY DELETE
if (isset($_POST['delete'])) {
    $id_to_delete = mysqli_real_escape_string($conn, $_POST['id_to_delete']);
    $sql = "DELETE FROM heroes WHERE id = $id_to_delete";
    if (mysqli_query($conn, $sql)) {
        //success;
        $_SESSION['msg'] = "Hero Deleted!";
        header('Location: main_admin.php');
    } else {
        //failure
        echo 'query error: ' . mysqli_error($conn);
    }
}

// if (isset($_POST['edit'])) {

//     $id_to_edit = mysqli_real_escape_string($conn, $_POST['id_to_edit']);
//     echo $id_to_edit;
//     $sql = "SELECT * FROM heroes WHERE id = $id_to_edit";
//     //get the query result
//     $result = mysqli_query($conn, $sql);
//     //Fetch the results in a array format
//     //this time we only need one row, so not fetch all but fetch
//     $hero = mysqli_fetch_assoc($result);
//     // echo $hero;
//     //set the variables
//     $name = $hero['name'];
//     $real_name = $hero['real_name'];
//     $short_bio = $hero['short_bio'];
//     $long_bio = $hero['long_bio'];

// }

//we are checking if that ID is set
// BEING USED TO RETRIEVE HERO DETAILS

if (isset($_GET['id'])) {
    $id = mysqli_real_escape_string($conn, $_GET['id']);

    //make sql
    $sql = "SELECT * FROM heroes WHERE id = $id"; //Selecting the respective hero details
    //get the query result
    $result = mysqli_query($conn, $sql);

    //Fetch the results in a array format
    //this time we only need one row, so not fetch all but fetch
    $hero = mysqli_fetch_assoc($result);
    $name = $hero['name'];
    $real_name = $hero['real_name'];
    $short_bio = $hero['short_bio'];
    $long_bio = $hero['long_bio'];

    //Free memory
    mysqli_free_result($result);
    mysqli_close($conn);

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

    <!-- All heros have the same style -->

    <link href="./assets/css/hero1.css" rel="stylesheet" type="text/css" />

    <link href="./assets/css/hero.css" rel="stylesheet" type="text/css" />
    <link href="./assets/css/style1.css" rel="stylesheet" type="text/css" />
    <title>heroBio</title>
  </head>

  <body>
    <!-- start of header -->
    <header class="header">
      <nav class="nav">
        <div class="navbar-brand">
          <img src="./assets/img/x-logo.png" class="logo padding-1" />
        </div>
      </nav>
    </header>

    <!-- End of header -->

    <!-- First checks if hero exists -->
    <?php if ($hero): ?>
      <div class="container m-5 d-flex justify-content-around">
        <div class="rectangle d-flex align-items-end justify-content-center">
          <img class="img-fluid img-1" style="width: 100%; height: 100%; " src="./assets/img/angel.png" alt="" />
        </div>
        <div class="content align-content-start">
          <!-- Name -->
          <div class="text">
            <h2><?php echo htmlspecialchars($hero['name']); ?></h2>
          </div>
          <!-- Real name -->
          <div class="text">
            <h2><?php echo htmlspecialchars($hero['real_name']); ?></h2>
          </div>
          <!-- short bio -->
          <div class="paragraph">
            <p>
              <?php echo htmlspecialchars($hero['short_bio']); ?>
            </p>
          </div>
          <!-- Long Bio -->
          <div class="paragraph">
            <p>
              <?php echo htmlspecialchars($hero['long_bio']); ?>
            </p>
          </div>
        </div>
      </div>
      

    <?php else: ?>
        <!-- Echos when there is no such hero -->
        <h2>No Such Hero Exists!</h2>
    <?php endif;?>
    <footer class="footer">
      <p>Designed with &#10084; by Group 18.</p>
    </footer>
  </body>
</html>


