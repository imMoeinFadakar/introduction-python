


let machineNum = Math.random() * 50
let celidNumber = Math.ceil(machineNum)


console.log(celidNumber)



for(let i = 0 ; i < 20 ; i++){

let userNumber = prompt("Enter The age:")

if(userNumber == celidNumber){

alert("you Won! " + celidNumber)
break

}else if(userNumber > celidNumber){
alert("its to Height!")

}else if(userNumber < celidNumber){
    alert("its to low!")


}



}


