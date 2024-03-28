<?php 
include "dbconnect.php"; //include the database connect module which contain credentials.

//declare global variables...
//bool variables
$is_dberror = false;
$user_exists = false;
$error_code = 0;
$error_msg = "";

//start the session for storing user log.
session_start();

//connect to database and create database with the table if not exists.
connect_db("users");
$sql_query = "CREATE TABLE IF NOT EXISTS users(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    email VARCHAR(50),
    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)";
if(!mysqli_query($conn, $sql_query)){
    $is_dberror = true;
}

if(isset($_POST['username']) && isset($_POST['password'])){
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);

    $sql_query = "SELECT username FROM users WHERE username = '$username';";
    $result = mysqli_query($conn, $sql_query);
    $nums = mysqli_num_rows($result);
    if($nums == 0){
        $user_exists = false;
    }elseif($nums > 1){
        $is_dberror = true; //multiple user fuond with same username..
    }else{
        $user_exists = true;
    }

    if (isset($_POST['email']) && isset($_POST['cpassword'])) {
        $email = mysqli_real_escape_string($conn, $_POST['email']);
        $cpassword = mysqli_real_escape_string($conn, $_POST['cpassword']);
        if(!$user_exists){
            if($password == $cpassword){
                $sql_query = "INSERT INTO users (username, password, email) VALUES ('$username','$password','$email')";
                if(!mysqli_query($conn, $sql_query)){
                    $is_dberror = true;
                }
            }else{
                $error_msg = "password not matched type again.";
                $error_code = 4;
            }
        }else{
            $error_code = 1; //user exists.
            $error_msg = "user exists already..";
        }
    } else {
        if(!$user_exists){
            $error_msg = "user not exist try to Register.";
            $error_code = 2; //user not exists.
        }else{
            $sql_query = "SELECT * FROM users WHERE username = '$username' AND password = '$password';";
            $result = mysqli_query($conn, $sql_query);
            $nums = mysqli_num_rows($result);
            if($nums == 0){
                $error_msg = "password is wrong.";
                $error_code = 3;
            }elseif($nums > 1){
                $is_dberror = true; //multiple user fuond with same username..
            }elseif($nums == 1){
                $row = mysqli_fetch_assoc($result);
                $_SESSION['username'] = $row['username'];
                $_SESSION['email'] = $row['email'];
                $_SESSION['reg_date'] = $row['reg_date'];
            }
        }
    }
    
}
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SignIn</title>
    <link rel="stylesheet" href="style.css">
</head>

<body onload="onLoad()">
    <div class="main">
        <div class="sign-box">
            <div class="switch-mode"><button class="sign-switch sign-up-switch">Register</button><button
                    class="sign-switch sign-in-switch">Log In</button></div>

            <p id="log-msg" class="log-msg"><?php
            //show errors that is been occured
            if($is_dberror){
                echo "this is rare error{$is_dberror}.<br>please don't make any action and report the developer.";
            }else{
                echo $error_msg;
            }
            ?></p>
            <form action="" class="register" id="register" method="post" style="display:none;">
                <input autocomplete="username" type="text" name="username" id="username" placeholder="Username"
                    class="inputfrom username" required>
                <input autocomplete="email" type="email" name="email" id="email" placeholder="Email"
                    class="inputfrom email" required>
                <input autocomplete="off" type="password" name="password" id="password" placeholder="Password"
                    class="inputfrom password" required>
                <input autocomplete="off" type="password" name="cpassword" id="cpassword" placeholder="Confirm Password"
                    class="inputfrom password" required>
                <br>
                <button type="submit" class="sign-btn">Sign Up</button>
            </form>

            <form action="" class="login" id="login" method="post">
                <input autocomplete="username" type="text" name="username" id="username" placeholder="Username"
                    class="inputfrom username" required>
                <input autocomplete="off" type="password" name="password" id="password" placeholder="Password"
                    class="inputfrom password" required>
                <br>
                <div id="forget-pass">Forget Password?</div>
                <button type="submit" class="sign-btn">Sign In</button>
            </form>
            <?php
	    if(isset($_SESSION['username'])){
                //user is logged in no need to check.
                if(isset($_SESSION['username'])){
                    $username = $_SESSION['username'];
                    $email = $_SESSION['email'];
                    $date = $_SESSION['reg_date'];
                    echo "
                    <div>
                        <h3>User Details</h3>
                        <p class=\"inputfrom\">Username : $username</p>
                        <p class=\"inputfrom\">Email    : $email</p>
                        <p class=\"inputfrom\">Password : ********</p>
                        <p class=\"inputfrom\">Date : $date</p>
                        <form action=\"\" method=\"post\">
                            <input type=\"hidden\" name=\"logout\" value=\"logout\">
                            <button type=\"submit\" class=\"sign-btn\">Log Out</button>
                        </form>
                    </div>
                    <style>
                        .switch-mode{
                            display: none;
                        }
                        .register{
                            display: none;
                        }
                        .login{
                            display: none;
                        }
                    </style>";
                }
            }elseif(isset($_POST['logout'])){
                // Unset all of the session variables
                session_destroy();
                header("Location: index.php");
                exit;
            }
	    ?>
        </div>
    </div>
    <script>
    const signUpSwitch = document.querySelector('.sign-up-switch');
    const signInSwitch = document.querySelector('.sign-in-switch');
    const login = document.getElementById('login');
    const register = document.getElementById('register');

    signUpSwitch.addEventListener('click', () => {
        login.style.display = 'none';
        register.style.display = 'block';
    });

    signInSwitch.addEventListener('click', () => {
        login.style.display = 'block';
        register.style.display = 'none';
    });
    </script>
</body>

</html>