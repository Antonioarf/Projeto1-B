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
  console.log()
}

async function func4(){
  console.log("12345678901234567890")
  lista = await axios.get(`${window.location.href}api/users/` ); //requisicao da lista de usuarios
  console.log(lista.data)
  var x = document.forms["myForms"]["usuario"].value; //pra quem vai ser compartilhado
  var id = document.forms["myForms"]["custId"].value; //id do card a ser compartilhado
  var nome = document.getElementById('nomee').innerHTML ; //usuario compartilhando
  var token = document.getElementById('token').innerHTML; //token de acesso
  console.log(nome);
  console.log(token);

  if (lista.data.includes(x)) {
    console.log(options1)
    resp2 = await axios.post(`${window.location.href}api/share/` ,{nome :x, id :id  } , {headers: { token: token}})
    console.log("passou2")
    console.log(resp2)
    alert("Nota compartilhada com sucesos")
    document.getElementById("myPopup").style.display = 'none';

  }
  else {
    alert("Usuario nao encontrado");
    return false;
  }
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
    )} card-rotation-${getRandomInt(1, 6)}`;
  }
  console.log("testeeeeee")

  let botoes = document.getElementsByClassName("botao_mudar");
  Array.prototype.forEach.call(botoes, function(item) {
    console.log("@@@@@@@@@@@@@@@@@@@@")
      if  (item.innerHTML == " Feito: True" ){
        item.innerHTML = "Concluido";
        item.style.color = "blue";
        console.log("$$$$$$$$$$$$$$$$$$$")
      }
      else if  (item.innerHTML == " Feito: False" ){
        console.log("%%%%%%%%%%%%%%%%%%%%%")
        item.innerHTML = "Pendente";
        item.style.color = "red";

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



});
