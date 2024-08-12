<?php

if(isset($_GET["param"])){

    $Sec = $_GET["param"];

     $min = $Sec / 60;
    $hours = $min / 60;

echo $hours."H" ;
}











