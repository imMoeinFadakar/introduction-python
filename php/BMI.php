<?php

if(isset($_GET["weight"]) && isset($_GET["height"])){

$Weight = $_GET["weight"];
$Height = $_GET["height"];

$result = $Weight / ($Height ** 2);
 
if($result < 18.5){
    echo "Under Weight";

}else if ($result > 18.5 && $result < 24) {
    echo "Under Weight";

}else if ($result > 24 && $result < 30) {
    echo "Under Weight";

}else if ($result > 30 && $result < 35) {
    echo "Under Weight";
    
}else if ($result > 35 ) {
    echo "Under Weight";
}


}





?>