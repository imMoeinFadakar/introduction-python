<?php

if(isset($_GET["param"])){

$houres = $_GET["param"];

$HoursToSec = ($houres * 60) * 60;

echo "sec :" .  $HoursToSec ;

}else{

echo"add a param";

}


















