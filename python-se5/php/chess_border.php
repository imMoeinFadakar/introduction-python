<?php  


if (isset($_GET["row"]) and isset($_GET["col"])){

echo "<table border='1'>";  
for ($row = 1; $row <= (int) $_GET["row"]; $row++) {  
    echo "<tr>";  
    for ($col = 1; $col <= (int) $_GET["row"]; $col++) {  
        if (($row + $col) % 2 == 0) {  
            echo "<td style='background-color: #FFFFFF;'></td>"; // White square  
        } else {  
            echo "<td style='background-color: #000000;'></td>"; // Black square  
        }  
    }  
    echo "</tr>";  
}  
echo "</table>";  


}else{

echo "please enter both params :)";

}


require_once("./function/function.php")

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<form action="" method="get" >
<input type="number" name="row" id="">
<input type="number" name="col" id="">

<button type="submit" >send</button>
</form>


</body>
</html>



