<?php 


$number =  $_GET["number"];

$str_to_array = array_map('strval',str_split($number));

$input  = $str_to_array ;
$sorted = array_values($input);
sort($sorted);

if ( $input === $sorted ) {
  print("this array is sorted!");
}else{
    print("this array is not sorted!");
}



