<?php




if(isset($_GET["param"])){

$userselection = $_GET["param"];

$computerSelect  = random_int(1,3);

if($computerSelect == 1){
    $computerSelect == "rock";
}else if($computerSelect == 2){
    $computerSelect == "scessores";
}else if($computerSelect == 3){
    $computerSelect == "paper";
}

$user_score = 0;
$computer_score = 0;


if($userselection == "scessores" or $userselection == "rock" or $userselection == "paper"){

if($userselection == "scessores" or $computerSelect == "rock"){
        $computer_score++;
    echo"computer Won ; computer: "+$computer_score + "user Score:" + $user_score ;
    
}else if($userselection == "rock" or $computerSelect == "rock"){

   
    echo" equall " ;

}else if($userselection == "paper" or $computerSelect == "rock"){
    
    $user_score++;
    echo"suer Won ; computer: "+$computer_score + "user Score:" + $user_score ;

}else if($userselection == "scessores" or $computerSelect == "scessores"){
    
    echo" equall " ;

}else if($userselection == "rock" or $computerSelect == "scessores"){
    
    $user_score++;
    echo"user Won ; computer: "+$computer_score + "user Score:" + $user_score ;

}else if($userselection == "paper" or $computerSelect == "scessores"){
    
    $computer_score++;
    echo"computer Won ; computer: "+$computer_score + "user Score:" + $user_score ;

}else if($userselection == "scessores" or $computerSelect == "paper"){
    
    $user_score++;
    echo"user Won ; computer: "+$computer_score + "user Score:" + $user_score ;

}else if($userselection == "rock" or $computerSelect == "paper"){
    
    $computer_score++;
    echo"computer Won ; computer: "+$computer_score + "user Score:" + $user_score ;

}else if($userselection == "paper" or $computerSelect == "paper"){
    
    echo" equall " ;

}




}else{

    echo"please Enter a valid Option!";

}


}else{

echo"Enter a Option Please!";

}








