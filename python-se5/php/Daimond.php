<?php 

require_once("./function/function.php");

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>diamond</title>
</head>
<body>
    
<div style="text-align: center;" >
<?php

if(isset($_GET["number"])){


    $num = $_GET["number"];
    
    printDiamond($num);
    
    
    
    }else{
    
    echo"enter a num";
    
    }

?>
</div>

<form action="" style="text-align: center;" method="get" >
    <input name="number" type="text">
    <button type="submit">submit</button>
</form>

</body>
</html>










