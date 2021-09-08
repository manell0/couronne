var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var header = document.querySelector('#colors')




console.log('va fan da och kontakt')
// Hover (mouseover and mouseout)
headOne.addEventListener('mouseover',function(){
    headOne.textContent = "Registrerat resultat kan ej att tas bort!";
    headOne.style.color = 'red';
})

headOne.addEventListener('mouseout',function(){
    headOne.textContent = "Endast registrerade namn uppdateras!"; 
    headOne.style.color = 'darkred';
})

headTwo.addEventListener("mouseover", function() {   
    // highlight the mouseover target
    headTwo.style.color = "grey";

    // reset the color after a short delay
    setTimeout(function() {
      headTwo.style.color = "";
    }, 1500);
  }, false);


header.style.color = 'black'
function getRandomColor(){
    var letters = "0123456789";
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random()*16)];
    }
    return color
  }
  
  // Simple function for clarity
  function changeHeaderColor(){
    colorInput = getRandomColor()
    header.style.color = colorInput;
  }
  
  // Now perform the action over intervals (milliseocnds):
  setInterval("changeHeaderColor()",800);




