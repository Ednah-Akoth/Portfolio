<!-- This will be used in all the files where the database needs to be connected -->

<?php
//connect to database

// $host = '127.0.0.1';
// $user = 'tona';
// $password = 'Code20';
// $db = 'crud_app';

// $conn = mysqli_connect($host,$user,$password,$db);

$conn = mysqli_connect('localhost', 'ednah', '!128#mucious@98', 'crud_app');

//Check connection
if (!$conn) { //if connection is not successful
    echo 'connection error' . mysqli_connect_error();
}
