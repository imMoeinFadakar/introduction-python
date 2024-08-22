<?php

// this code will remove same indexes in array:

$duplicated_array = array( 0=>3 , 1=>2 ,  2=>3 , 3=>4 ,  4=>5);
print_r(array_unique($duplicated_array));