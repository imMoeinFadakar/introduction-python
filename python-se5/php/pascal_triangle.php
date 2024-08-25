<?php
require_once("./function/function.php");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div style="width:100%; text-align:center">

    <?php
if($_GET){

$user_number = (int) $_GET["number"] ;

pascal_triangle($user_number);

}else{



}



?>
    </div>
<div style="display:flex; justify-content: center; align-items: center;"  >
<form action="" method="get" style="" >
    <input type="text" name="number" placeholder="enter a number pls :) " >
<button type="submit">submit</button>    
</form>

</div>



</body>
</html>

