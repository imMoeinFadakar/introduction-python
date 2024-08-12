let form = document.querySelector("#form")
function addDegree(){
let input = document.createElement("input")
input.setAttribute("name" , "mydegree[]")
form.append(input)

}