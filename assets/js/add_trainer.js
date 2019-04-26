function remove_error() {
    document.getElementById("error_box").style.display = 'none';
}

function remove_message() {
    document.getElementById("message_box").style.display = 'none';
}

let url = () => {
    let fetchpoolid = localStorage.getItem("poolDataId");
    return 'https://easyswimapi.herokuapp.com/api/v1/trainers' + "/".concat(fetchpoolid)
}

const addTrainer = (event) => {
    event.preventDefault()
    let firstName = document.getElementById('firstname').value;
    let lastName = document.getElementById('lastname').value;
    let workingTime = document.getElementById('workingtime').value;
    let trainer_contact = document.getElementById('trainer_contact').value;
    let description = document.getElementById('description').value;

    fetch(url(), {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-type': 'application/json',
            "Authorization": localStorage.getItem("token")
        },
        body: JSON.stringify({
            "firstname": firstName,
            "lastname": lastName,
            "working_time": workingTime,
            "trainer_contact": trainer_contact,
            "description": description
        })
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message === "Trainer was successfuly added") {
                let trainer_form = document.getElementById("add_trainer_form");
                let message_box = document.getElementById("message_box");
                message_box.innerHTML = data.message;
                message_box.style.display = 'block';
                setTimeout(() => { remove_message(); trainer_form.reset(); }, 3000)
            }
            else {
                let error_box = document.getElementById("error_box");
                error_box.innerHTML = data.message;
                error_box.style.display = 'block';
                setTimeout(remove_error, 3000)
            }
        })

}