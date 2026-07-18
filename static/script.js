document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("scholarshipForm");

    const button = document.getElementById("predictBtn");

    const loading = document.getElementById("loading");

    form.addEventListener("submit", function (event) {

        let valid = true;

        // Remove previous highlights
        document.querySelectorAll(".error").forEach(field => {
            field.classList.remove("error");
        });

        // Get values
        const cgpa = parseFloat(document.getElementsByName("cgpa")[0].value);

        const attendance = parseInt(document.getElementsByName("attendance")[0].value);

        const income = parseFloat(document.getElementsByName("family_income")[0].value);

        const backlogs = parseInt(document.getElementsByName("backlogs")[0].value);

        const semester = parseInt(document.getElementsByName("semester")[0].value);

        // Validation

        if (cgpa < 0 || cgpa > 10) {

            alert("CGPA must be between 0 and 10.");

            document.getElementsByName("cgpa")[0].classList.add("error");

            valid = false;

        }

        if (attendance < 0 || attendance > 100) {

            alert("Attendance must be between 0 and 100.");

            document.getElementsByName("attendance")[0].classList.add("error");

            valid = false;

        }

        if (income < 0) {

            alert("Family Income cannot be negative.");

            document.getElementsByName("family_income")[0].classList.add("error");

            valid = false;

        }

        if (backlogs < 0) {

            alert("Backlogs cannot be negative.");

            document.getElementsByName("backlogs")[0].classList.add("error");

            valid = false;

        }

        if (semester < 1 || semester > 8) {

            alert("Semester must be between 1 and 8.");

            document.getElementsByName("semester")[0].classList.add("error");

            valid = false;

        }

        if (!valid) {

            event.preventDefault();

            return;

        }

        button.disabled = true;

        button.innerHTML = "Predicting...";

        loading.style.display = "block";

    });

});