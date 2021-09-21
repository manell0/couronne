var headOne = document.querySelector('#one')

// Hover (mouseover and mouseout)
headOne.addEventListener('mouseover',function(){
    headOne.textContent = "Registered result can not be changed!";
    headOne.style.color = 'red';
})

headOne.addEventListener('mouseout',function(){
    headOne.textContent = "Registered results cannot be deleted!"; 
    headOne.style.color = 'darkred';
})

