function predictGrade() {

    let attendance = document.getElementById("attendance").value;
    let studyHours = document.getElementById("study_hours").value;
    let previousGrade = document.getElementById("previous_grade").value;

    if(attendance==="" || studyHours==="" || previousGrade===""){
        document.getElementById("result").innerHTML = "Please fill all the fields.";
        return;
    }

    let prediction = (Number(attendance) + Number(studyHours) + Number(previousGrade)) / 3;

    document.getElementById("result").innerHTML =
    "Predicted Grade: " + prediction.toFixed(2);
}
