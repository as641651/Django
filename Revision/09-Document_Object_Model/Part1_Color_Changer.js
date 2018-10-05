// Alright so we've discussed the way you can grab html elements, let's
// see how we can interact with them in Javascript!

// Type this into your console:

// Grab the Header with h1
var header = document.querySelector("h1")

//list of methods on js_htmldom_document
//https://www.w3schools.com/jsref/dom_obj_document.asp


// querySelector is preferred over getElementbyID or getElementsByClassName
// because a single method can be used for pick up all kinds of objects
document.querySelector("#pickme");
document.querySelectorAll(".myul"); // returns list of all elements

// Then you can interface with the object.

// Interface with the style.
//You will see a ton of options show up!
header.style.color = 'red'

//Changing HTML Elements

//element.innerHTML =  new html content
//element.attribute = new value
//element.setAttribute(attribute, value)
//element.style.property = new style

//Adding Events Handlers

//document.getElementById(id).onclick = function(){code}


//more details:
//https://www.w3schools.com/js/js_htmldom_document.asp


// Now let's connect it to the script to
// change it once every second to a random color!

// Random Color Function:

// http://stackoverflow.com/questions/1484506/random-color-generator-in-javascript
function getRandomColor(){
  var letters = "0123456789ABCDEF";
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
setInterval("changeHeaderColor()",500);
