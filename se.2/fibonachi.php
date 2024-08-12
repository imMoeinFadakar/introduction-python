<?php  
function fibonacci($n) {  
    $fib = [0, 1];  

    for ($i = 2; $i < $n; $i++) {  
        $fib[] = $fib[$i - 1] + $fib[$i - 2]; 
    }  
    
    return $fib;  
}  


if(isset($_GET["param"])){

$n = $_GET["param"];  
$result = fibonacci($n);  

echo "دنباله فیبوناچی اولین $n عدد:\n";  
foreach ($result as $value) {  
    echo  $value . " -";  
}  

}else{
    echo "add a Number";
}


?>  


