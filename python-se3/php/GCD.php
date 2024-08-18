<?php

if (isset($_GET["first"]) && $_GET["second"]){

$firstnumber = $_GET["first"];
$secondNumber = $_GET["second"];

function gcd($a, $b) {  
    return $b == 0 ? $a : gcd($b, $a % $b);  
}  


$result = gcd($firstnumber, $secondNumber);  
echo "G.C.D. of " . $firstnumber . " and " . $secondNumber . " is: " . $result;  

}else{

echo"please fill out values!";

}








