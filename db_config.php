<?php
$host = "localhost";
$user = "root";
$pass = "";
$db_name = "lanka_guide_db";

$conn = new mysqli($host, $user, $pass, $db_name);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully to LankaGuide Database";
?>