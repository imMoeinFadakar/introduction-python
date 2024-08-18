<?php
if(isset($_GET["first"]) && isset($_GET["second"])){

$first_number = $_GET["first"];
$second_number =  $_GET["second"];

function lcm($a, $b) {  
    return ($a * $b) / gcd($a, $b);  
}  

function gcd($a, $b) {  
    return $b == 0 ? $a : gcd($b, $a % $b);  
}  


$result = lcm($first_number, $second_number);  
echo "L.C.M. of " . $first_number . " and " . $second_number . " is: " . $result;  
}else{

    echo"please fill out values!";


}

?>
<form action="" method="">
<input type="number" name="first">
<input type="number" name="second">
<button type="submit">submit</button>
</form>





