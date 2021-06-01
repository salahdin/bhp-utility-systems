// Set the date we're counting down to
const countDownDate = new Date("2021-07-01 23:59").getTime();
const countDownDate2 = new Date("2021-06-01 23:59").getTime();

// Update the count down every 1 second
const x = setInterval(function () {

    // Get today's date and time
    const now = new Date().getTime();

    // Find the distance between now and the count down date
    const distance = countDownDate - now;
    const distance2 = countDownDate2 - now;

    // Time calculations for days, hours, minutes and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    const days2 = Math.floor(distance2 / (1000 * 60 * 60 * 24));
    const hours2 = Math.floor((distance2 % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes2 = Math.floor((distance2 % (1000 * 60 * 60)) / (1000 * 60));
    const seconds2 = Math.floor((distance2 % (1000 * 60)) / 1000);

    // Output the result in an element with id="demo"
    document.getElementById("second").innerHTML = seconds + "";
    document.getElementById("minute").innerHTML = minutes + "";
    document.getElementById("hour").innerHTML = hours + "";
    document.getElementById("day").innerHTML = days + "";

    document.getElementById("second2").innerHTML = seconds + "";
    document.getElementById("minute2").innerHTML = minutes + "";
    document.getElementById("hour2").innerHTML = hours + "";
    document.getElementById("day2").innerHTML = days + "";

    document.getElementById("second3").innerHTML = seconds + "";
    document.getElementById("minute3").innerHTML = minutes + "";
    document.getElementById("hour3").innerHTML = hours + "";
    document.getElementById("day3").innerHTML = days + "";

    document.getElementById("second1").innerHTML = seconds2 + "";
    document.getElementById("minute1").innerHTML = minutes2 + "";
    document.getElementById("hour1").innerHTML = hours2 + "";
    document.getElementById("day1").innerHTML = days2 + "";

    // If the count down is over, write some text
    if (distance < 0) {
        document.getElementById("wrapper").style.display = "none";

        document.getElementById("wrapper2").style.display = "none";
        document.getElementById("wrapper3").style.display = "none";

        document.getElementById("procurement").style.display = "block";

        document.getElementById("documents").style.display = "block";
        document.getElementById("contract").style.display = "block";

    }
    if (distance2 < 0) {
        document.getElementById("wrapper1").style.display = "none";
        document.getElementById("timesheet").style.display = "block";



    }
}, 1000);