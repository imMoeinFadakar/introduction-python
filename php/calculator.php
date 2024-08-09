<?php

$firstNumber = $_GET["param1"];
$secondNumber = $_GET["param2"];

if(isset($firstNumber) && isset($secondNumber)){

echo $plusResult = $firstNumber + $secondNumber;
echo $MinResult = $firstNumber - $secondNumber;
echo $MulResult = $firstNumber * $secondNumber;
echo $DivResult = $firstNumber / $secondNumber;

}

if(isset($firstNumber)){

   echo $endResult = sqrt($firstNumber);
   echo $endResult = sin($firstNumber);
   echo $endResult = cos($firstNumber);

    $deg2rad = deg2rad($firstNumber);
   echo $endResult = tan($deg2rad);

    }


    
?>