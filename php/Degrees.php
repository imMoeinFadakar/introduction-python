<?php

if (isset($_GET["Degree1"]) && isset($_GET["Degree2"]) && isset($_GET["Degree3"])){

$degree1 = $_GET["Degree1"];
$degree2 = $_GET["Degree2"];
$degree3 = $_GET["Degree3"];

$result = ($degree1 + $degree2 + $degree3) / 3; 

echo $result;


if ($result < 12 ){
    echo "fail";
}

if($result > 12 && $result < 17 ){
    echo "Normal";
}

if ($result > 17 && $result < 20 ){
    echo "Great";
}

}

?>