<?php
$allmYDegree = array();

$allmYDegree = $_POST["mydegree"];


// $_SESSION["mydegree"] = print_r($allmYDegree);

// header("location:guesstext.php");


$sum = 0;  

foreach ($allmYDegree as $num) {  
    $sum += $num;  
}  

echo $sum / count($allmYDegree) ;  // خروجی: 15  

?>