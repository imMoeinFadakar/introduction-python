<?php

if (isset($_GET["side1"])&&isset($_GET["side2"])&&isset($_GET["side3"])){

$side1 = $_GET["side1"];
$side2 = $_GET["side2"];
$side3 = $_GET["side3"];

if (($side1 + $side2) < $side3){
    echo "its Impossible";

}elseif ( ($side1 + $side3) < $side2 ){
    echo "its Impossible";

}elseif ( ($side2 + $side3) < $side1 ){
    echo "its Impossible";

}else{
    echo "You can have this  triangle";

}





}

?>