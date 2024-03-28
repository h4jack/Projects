<?php
$servername = "localhost";
$username = "username";
$password = "do_not_look";
$conn = "";
function connect_db($db_name){
    global $servername, $username, $password, $conn; 
    $conn = mysqli_connect($servername, $username, $password);
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    
    $create_db = "CREATE DATABASE if not exists $db_name";
    if (mysqli_query($conn, $create_db)) {
        $conn =  mysqli_connect($servername, $username, $password, $db_name);
    } else {
        return "Error creating database: " . mysqli_error($conn);
    }
}
function close_db(){
    global $conn;
    mysqli_close($conn);
}
?>