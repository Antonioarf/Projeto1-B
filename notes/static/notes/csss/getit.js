// const axios = require("axios");
// const async = require('async');
// const await = require('await');


function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function func1(nome1,nome2,nome3){
  document.getElementById(nome1).style.display = "none";
  document.getElementById(nome2).style.display = "block";
  document.getElementById(nome3).style.transform = "none";
  // document.getElementById("update").disable = false;
  console.log("entrouuuuuuuuuu1")
}
function func2(nome1,nome2,nome3){
  document.getElementById(nome1).style.display = "none";
  document.getElementById(nome2).style.display = "block";
  document.getElementById(nome3).style.transform = "none";
  // document.getElementById("update").disable = false;
  console.log("entrouuuuuuuuuu2")
}

function func3(inp){
  
  document.getElementById("myPopup").style.display = 'block';
  // document.getElementById("myPopup").className += ` ${document.getElementById(`card${inp}`).className.split(" ")[1]}`;
  document.getElementById("idid").value = inp;
  console.log(inp);
  console.log(document.getElementById("myPopup").className);
  setTimeout(() => {  document.getElementById("apareceu").innerHTML = 'true'; }, 500);
}

async function func4(){
  console.log("5555555555555555555555555555555555555555555")
  lista = await axios.get(`${window.location.href}api/users/` ); //requisicao da lista de usuarios
  console.log(lista.data)
  var x = document.forms["myForms"]["usuario"].value; //pra quem vai ser compartilhado
  var id = document.forms["myForms"]["custId"].value; //id do card a ser compartilhado
  var nome = document.getElementById('nomee').innerHTML ; //usuario compartilhando
  var token = document.getElementById('token').innerHTML; //token de acesso
  console.log(nome);
  console.log(token);

  if (lista.data.includes(x)) {
    resp2 = await axios.post(`${window.location.href}api/share/` ,{nome :x, id :id  } , {headers: { token: token}})
    console.log("passou2")
    console.log(resp2)
    document.getElementById('status').innerHTML = "Nota compatilhada com sucesso!" ; //usuario compartilhando
    document.getElementById("myPopup2").style.display = 'block';



  }
  else {
    // document.getElementById('status').innerHTML = "Nota compatilhada com sucesso!" ; //usuario compartilhando
    alert("Usuario nao encontrado");
    return false;
  }
}

function func5(){
  document.getElementById("myPopup2").style.display = 'none';
  document.getElementById("myPopup").style.display = 'none';
  document.getElementById("apareceu").innerHTML = 'false';

}

document.addEventListener("DOMContentLoaded", function () {
  
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} `;
  }
  console.log("testeeeeee")

  let botoes = document.getElementsByClassName("botao_mudar");
  Array.prototype.forEach.call(botoes, function(item) {
      if  (item.innerHTML == " Feito: True" ){
        item.innerHTML = "Concluido";
        item.style.color = "blue";
      }
      else if  (item.innerHTML == " Feito: False" ){
        item.innerHTML = "Pendente";
        item.style.color = "red";

      }
  }); 

  let contentes = document.getElementsByClassName("corpo_card");
  Array.prototype.forEach.call(contentes, function(item) {
      console.log("333333333333333333333333333333333333")
      if  (item.innerHTML == "" ){
        console.log("@@@@@@@@@@@@@@@@@@@@")
        item.innerHTML = "nota sem corpo"
      }
      else{
        console.log(item.innerHTML)
      }

  }); 


  let dates = document.getElementsByClassName("card-date");

  Array.prototype.forEach.call(dates, function(item) {
    try {
    item.innerHTML = item.innerHTML.split("-").reverse().join("/");
    }
    catch(err) {
      console.log("DDDDDDDDDDDD");

    }
});

// document.getElementById('cardcont').addEventListener("click", function(){
//   console.log("clicou");
// });
var ignortar = document.getElementById('myPopup');


document.addEventListener('click', function(event) {
  if (document.getElementById("apareceu").innerHTML == 'true'){ 

    var isClickInsideElement = ignortar.contains(event.target);
    if (!isClickInsideElement) {
        //Do something click is outside specified element
        document.getElementById("myPopup").style.display = 'none';
        document.getElementById("myPopup2").style.display = 'none';

        console.log("clicou");
        document.getElementById("apareceu").innerHTML = 'false';

    }}
});



});
