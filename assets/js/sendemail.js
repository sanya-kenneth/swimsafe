const loadTrainers = () => {
    let fetchpoolid = localStorage.getItem("poolDataId");
    fetch("https://easyswimapi.herokuapp.com/api/v1/trainers/pool" + "/".concat(fetchpoolid), {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            Authorization: localStorage.getItem("token")
        }
    })
        .then(res => res.json())
        .then(data => {
            let selectElement = document.getElementById("trainer_select");
            if ("data" in data) {
                listData = data.data
                listData.forEach(trainer_item => {
                    selectElement.options[selectElement.options.length] =
                        new Option(String(trainer_item.first_name) + " " + String(trainer_item.last_name),
                            trainer_item.trainer_id);
                });
            }
        });
};


function remove_send_error() {
    document.getElementById("sendmail_error_box").style.display = 'none';
}

function remove_send_message() {
    document.getElementById("sendemail_message_box").style.display = 'none';
}

const sendMail = (event) => {
    event.preventDefault()
    let clientEmail = document.getElementById('client_email').value;
    let TrainerSelection = document.getElementById('trainer_select').value;
    let url = "https://easyswimapi.herokuapp.com/api/v1/trainers/sendinfo/" + `${TrainerSelection}`
    fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-type': 'application/json',
            "Authorization": localStorage.getItem("token")
        },
        body: JSON.stringify({
            "user_email": clientEmail
        })
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message === "Email was successfuly sent to user") {
                let message_send_box = document.getElementById("sendemail_message_box");
                message_send_box.innerHTML = data.message;
                message_send_box.style.display = 'block';
                setTimeout(remove_send_message, 7000)
            }
            else {
                let error_send_box = document.getElementById("sendmail_error_box");
                error_send_box.innerHTML = data.message;
                error_send_box.style.display = 'block';
                setTimeout(remove_send_error, 3000)

            }
        })

}
