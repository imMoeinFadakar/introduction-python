<?php  

// this array can find that entered number have factorial or no

if(isset($_GET["num"])){

$num = $_GET["num"];  
$factorial = 1;


for ($x=$num; $x>=1; $x--)   
{  
  $factorial = $factorial * $x;  
}  



if(is_integer($factorial) == true){

    echo "int"."<br>";
    echo "Factorial of $num is $factorial";  

}else{

    echo "no-int"."<br>";
    echo "Factorial of $num is $factorial";  


}

}else{

echo "enter a number";

}




?>  