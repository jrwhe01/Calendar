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
    //ie you can call manipulate() later to run this code

    let dayone = new Date(year, month, 1).getDay()
    //get day returns the dyas of the week as numbers so this will determine
    //what day if the week to be the first day of the month under

    let lastdate = new Date(year, month + 1, 0).getDate()
    //gets the date for the last day of the month by going back one
    //from the first day if the second month

    let dayend = new Date(year, month, lastdate).getDay()
    //day of the week for the last day of the month

    let monthlastdate = new Date(year, month, 0).getDate()
    //last day of the previous month

    let lit = "";
    //to store calendar html

    for (let i = dayone; i >0; i--)
    //filling in the empty days at the start of the calendar with the 
    //last days of the previous month
    {
       lit += `<li class="inactive">${monthlastdate - i + 1}</li>`;
        //html for inactive
    }

    for (let i = 1; i <= lastdate; i++)
    //fills in the days of the month 
    {
        let isToday = i === date.getDate()
            && month === new Date().getMonth()
            && year === new Date().getFullYear()
            ? "active"
            : "";
        lit += `<li class="${isToday}">${i}</li>`;
        //activates today's date
    }

    for (let i = dayend; i<6; i++)
    {
        lit += `<li class="inactive">${i - dayend + 1}</li>`;
        //fills in the days of the next month at are visable on the calendar 
    }
    day.innerHTML = lit;
    currdate.innerText = `${months[month]} ${year}`;

}

manipulate();
//set up calendar

prenexIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        month = icon.id === "calendar-prev" ? month -1 : month +1;

        if (month <0 || month > 11) {
            date = new Date(year, month, new Date().getDate());

            year = date.getFullYear();

            month = date.getMonth();
        }

        else 
        {
            date = new Date();
        }
        manipulate();
    });
});