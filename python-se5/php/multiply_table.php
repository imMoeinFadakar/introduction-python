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

<div align="center" style="margin-bottom: 3rem;"  >
<?php

if($_GET){

$ROW = $_GET["row"];
$COL = $_GET["col"];

multiply_table($ROW,$COL);

}else{


echo"<h3 style=/'text-align:center' >enter params pls :))</h3>";


}






?>
</div>

    <form action="" method="get" style="text-align: center;" >
        <input name="row" placeholder="row" type="text">
        <input name="col" placeholder="col" type="text">
        <button type="submit">submit</button>
    </form>
</body>
</html>


