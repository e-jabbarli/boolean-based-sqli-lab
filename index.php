<?php

include 'connect.php';

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $sql = "SELECT name FROM my_table where id = $id ";
}
else {
    die("Incorrect path");
}

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    echo "This record exists.";
} else {
    echo "No record found.";
}


$conn->close();
?>