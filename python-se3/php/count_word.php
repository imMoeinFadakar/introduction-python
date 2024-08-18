<?php

if(isset($_GET["string"])){

$string_wrapper = $_GET["string"];


$result = str_word_count($string_wrapper);

print("we have :".$result." word(s)");

}else{
echo "fill out input pls!";

}


?>


<form action="" method="">
<input type="text" name="string">
<button type="submit">submit</button>
</form>



