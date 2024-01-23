<?php
// Chemin vers votre fichier de base de données SQLite
$databasePath = 'chemin/vers/votre/base.db';

// Créer une connexion à la base de données SQLite
$conn = new SQLite3($databasePath);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['uname'];
    $password = $_POST['psw'];

    // Requête SQL pour récupérer l'utilisateur avec le nom d'utilisateur fourni
    $sql = "SELECT * FROM nom_de_votre_table WHERE nom_utilisateur = :username";
    $stmt = $conn->prepare($sql);
    $stmt->bindValue(':username', $username, SQLITE3_TEXT);
    $result = $stmt->execute();

    if ($result) {
        $row = $result->fetchArray(SQLITE3_ASSOC);

        if ($row && password_verify($password, $row['mot_de_passe'])) {
            echo "Authentification réussie!";
            // Redirigez l'utilisateur vers une page après l'authentification réussie
        } else {
            echo "Mot de passe incorrect.";
        }
    } else {
        echo "Nom d'utilisateur incorrect.";
    }
}
?>
