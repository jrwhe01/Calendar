let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();
//built in js funtions to get the date

const day = document.querySelector(".calendar-dates");
//takes calendar-dates from index.html

const currdate = document
    .querySelector(".calendar-current-date");

const prenexIcons = document
    .querySelectorAll(".calendar-nav span");

const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
];

const manipulate = () => {
    //this is like a js version of a method in a class 
    //ie you ccan call manipulate() later to run this code

    let 
}