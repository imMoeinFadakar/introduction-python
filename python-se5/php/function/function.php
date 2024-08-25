<?php

// this will print diamonds

function printDiamond($rows) { 
	for ($i = 1; $i <= $rows; $i++) { 
		
		// Print spaces 
		for ($j = 1; $j <= $rows - $i; $j++) { 
			echo " "; 
		} 
		
		// Print stars 
		for ($k = 1; $k <= 2 * $i - 1; $k++) { 
			echo "*"; 
		} 

		echo "<br>"; 
	} 

	for ($i = $rows - 1; $i >= 1; $i--) { 
		
		// Print spaces 
		for ($j = 1; $j <= $rows - $i; $j++) { 
			echo " "; 
		} 

		// Print stars 
		for ($k = 1; $k <= 2 * $i - 1; $k++) { 
			echo "*"; 
		} 

		echo "<br>"; 
	} 
} 

// this is for multiply table


function multiply_table($rows , $cols){

    echo "<table border=\"1\">";

    for ($r =0; $r < $rows; $r++){
    
        echo('<tr>');
    
        for ($c = 0; $c < $cols; $c++)
            echo( '<td>' .$c*$r.'</td>');
    
        echo('</tr>');
    
    }
    
    echo("</table>");


}

// pascal triangle :

function pascal_triangle($f){
   
    for ($x = 0; $x <= $f; $x++) {
        echo "1"." ";
        $previous_line[$x]=1;
    }
    
    echo "<br>";
    
    for ($x = 0; $x < $f; $x++) {
        $sum = 1; 
        echo $sum." ";
        for ($y = 1; $y <= $f-$x-1; $y++) {
            $sum = $sum + $previous_line[$y]; 
            echo $sum." ";              
            $previous_line[$y] =    $sum;                            
    }   
    echo "<br>";
    }

}


// chess border function

function chess_border($row , $col){
    echo "<table border='1'>";  
    for ($row = 1; $row <= $row; $row++) {  
        echo "<tr>";  
        for ($col = 1; $col <= $col; $col++) {  
            if (($row + $col) % 2 == 0) {  
                echo "<td style='background-color: #FFFFFF;'></td>"; // White square 
                
            

            } else {  
                echo "<td style='background-color: #000000;'></td>"; // Black square  
            }  
        }  
        echo "</tr>";  
    }  
    echo "</table>";  
    


}

