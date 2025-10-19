<?php
header('Content-Type: application/json');

// Conexión a la base de datos
$host = "mysql.inf.uct.cl";
$user = "dvillegas"; // Cambia según tu configuración
$pass = "Tynv.7985";     // Cambia según tu configuración
$db   = "A2025_dvillegas"; // Cambia por tu nombre de BD

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
    die(json_encode(["error" => "Error de conexión: " . $conn->connect_error]));
}

// Consulta SELECT
$sql = "SELECT * FROM multiplicadores";
$result = $conn->query($sql);

$datos = [];
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $datos[] = $row;
    }
}

echo json_encode($datos, JSON_PRETTY_PRINT);
$conn->close();
?>
