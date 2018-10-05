// Let's type this into the console, follow along with the video lecture

var x = document.querySelector("p")

// Show Text
x.textContent

// Reassign Text
x.textContent = "new"

// Refresh the page
// Show actual HTML
x.innerHTML

// Edit HTML
x.innerHTML = "This is <strong>BOLD</strong>"

// Can't do that with just textContent

/////////////////
// Attributes //
///////////////

var special = document.querySelector("#special")
var specialA = special.querySelector("a")

specialA.getAttribute("href")

specialA.setAttribute("href","https://www.amazon.com")


//list of all methods ND props
//https://www.w3schools.com/jsref/dom_obj_all.asp
