/*
   Student Name: Jocelyn Meyer
   File Name: script.js
   Date: 3/5/2025
*/

var answer = document.querySelector("#answer p");
var heading = document.querySelector("#answer h2");

//Function to display the first answer
function ans1() {
	heading.style.display = "block";
	answer.textContent = "The primary focus of Fashion That Moves With You is to offer trendy, customizable apparel while promoting sustainable practices. The platform aims to provide fashion that reflects individuality and responsibility.";
}

function ans2() {
	heading.style.display = "block";
	answer.textContent = "The platform promotes individuality by offering customizable clothing options, allowing customers to personalize their outfits. It promotes responsibility through sustainable practices, ensuring that fashion choices are mindful of the environment.";
}

function ans3(){
	heading.style.display = "block";
	answer.textContent = "The platform offers customization options that allow customers to personalize their clothing to reflect their unique style, ensuring each piece tells a story of individuality.";
}

function ans4() {
	heading.style.display = "block";
	answer.textContent = "Customers can find a diverse collection of high-quality clothing, including everyday essentials and statement pieces designed to fit seamlessly into their lives.";
}

// Hamburger menu function
function hamburger() {
    var navlinks = document.getElementById("mobile-nav");
    var menuicon = document.getElementById("menu-toggle");

    if (navlinks.style.display === "block") {
        navlinks.style.display = "none";
        menuicon.style.color = "#3E2723";
    } else {
        navlinks.style.display = "block";
        menuicon.style.color = "#3E2723";
    }
}
