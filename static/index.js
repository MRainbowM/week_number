var form = document.querySelector('form');
var result = document.querySelector('#result');

function calcWeekNumber() {
    var input_date = form.elements.date;

    fetch(`http://127.0.0.1:8080/week/?date=${input_date.value}`)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            if (data.status == "success" && data.week_number) {
                result.textContent = `Номер недели: ${data.week_number}`
            }
            else if (data.status == "error" && data.msg) {
                result.textContent = data.msg
            }
        })

    return false;
};