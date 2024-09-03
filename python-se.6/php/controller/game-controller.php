<?php


$block_array = array("","","",
                     "","","",
                     "","","");


if (isset($_POST)){

$cell1 = $_POST["cell-1"];
$cell2 = $_POST["cell-2"];
$cell3 = $_POST["cell-3"];
$cell4 = $_POST["cell-4"];
$cell5 = $_POST["cell-5"];
$cell6 = $_POST["cell-6"];
$cell7 = $_POST["cell-7"];
$cell8 = $_POST["cell-8"];
$cell9 = $_POST["cell-9"];

}else{
  
 echo"
<script>
alert(\"There is no field cells!\")
</script>
";

}



$array_one = [$cell1,$cell2,$cell3,$cell4,$cell5,$cell6,$cell7,$cell8,$cell9];



switch($array_one){

case($array_one[0] == 'o' && $array_one[1] == 'o' && $array_one[2] == 'o' ):
     o_wins();

break;
case($array_one[3] == 'o' && $array_one[4] == 'o' && $array_one[5] == 'o' ):
     o_wins();

break;
case($array_one[6] == 'o' && $array_one[7] == 'o' && $array_one[8] == 'o' ):
     o_wins();

break;
case($array_one[0] == 'o' && $array_one[4] == 'o' && $array_one[8] == 'o' ):
     o_wins();

break;
case($array_one[2] == 'o' && $array_one[4] == 'o' && $array_one[6] == 'o' ):
     o_wins();

break;
case($array_one[0] == 'o' && $array_one[3] == 'o' && $array_one[6] == 'o' ):
     o_wins();

break;
case($array_one[1] == 'o' && $array_one[4] == 'o' && $array_one[7] == 'o' ):
     o_wins();

break;
case($array_one[2] == 'o' && $array_one[5] == 'o' && $array_one[8] == 'o' ):
     o_wins();
break;

default:
no_win("player O");
break;
}

switch($array_one){

     case($array_one[0] == 'x' && $array_one[1] == 'x' && $array_one[2] == 'x' ):
          x_wins();
     break;
     case($array_one[3] == 'x' && $array_one[4] == 'x' && $array_one[5] == 'x' ):
          x_wins();
     break;
     case($array_one[6] == 'x' && $array_one[7] == 'x' && $array_one[8] == 'x' ):
          x_wins();
     break;
     case($array_one[0] == 'x' && $array_one[4] == 'x' && $array_one[8] == 'x' ):
          x_wins();
     break;
     case($array_one[2] == 'x' && $array_one[4] == 'x' && $array_one[6] == 'x' ):
          x_wins();
     break;
     case($array_one[0] == 'x' && $array_one[3] == 'x' && $array_one[6] == 'x' ):
          x_wins();
     break;
     case($array_one[1] == 'x' && $array_one[4] == 'x' && $array_one[7] == 'x' ):
          x_wins();
     break;
     case($array_one[2] == 'x' && $array_one[5] == 'x' && $array_one[8] == 'x' ):
          x_wins();
     break;
     
     default:
          no_win("player X ");
          break;
     }


     function no_win($player){
          echo"no win for " . $player . "<br>";

     }


     $X_score = 0;
     $O_score = 0;


     function add_score($x_or_o){

          if($x_or_o == "x"){

               return  $GLOBALS['X_score'] + 1;

          }else if($x_or_o == "o"){

               return  $GLOBALS['O_score'] + 1;

          }

     }

    function x_wins(){
     echo"x wons! score:" . add_score("x");
    }

    function o_wins(){
     echo"o wons! score:" . add_score("o");

    }





?>