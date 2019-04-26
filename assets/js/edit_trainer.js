
function remove_error_edit() {
    document.getElementById("edit_error_box").style.display = 'none';
}

function remove_message() {
    document.getElementById("message_box").style.display = 'none';
}
let updatefirstName = document.getElementById("update_firstname");
let updatelastName = document.getElementById("update_lastname");;
let updateworkingTime = document.getElementById("update_workingtime");
let trainerContact = document.getElementById("trainer_contact");
let updatedescription = document.getElementById("update_description");

const loadTrainerData = () => {
    let trainer_id = localStorage.getItem("trainerDataId");
    fetch("https://easyswimapi.herokuapp.com/api/v1/trainers" + "/" + `${trainer_id}`, {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            Authorization: localStorage.getItem("token")
        }
    })
        .then(res => res.json())
        .then(data => {
            if ("data" in data) {
                let { first_name, last_name, working_time, description, trainer_contact } = data.data
                updatefirstName.value = first_name,
                    updatelastName.value = last_name,
                    updateworkingTime.value = working_time,
                    trainerContact.value = trainer_contact
                updatedescription.value = description
            }
        });
}

const editTrainer = (event) => {
    event.preventDefault();
    let trainer_id = localStorage.getItem("trainerDataId");
    updatefirstName = updatefirstName.value;
    updatelastName = updatelastName.value;
    updateworkingTime = updateworkingTime.value;
    trainer_contact = trainerContact.value;
    updatedescription = updatedescription.value;
    let url = "https://easyswimapi.herokuapp.com/api/v1/trainers" + "/" + `${trainer_id}` + "/".concat("update")

    fetch(url,
        {
            method: 'PUT',
            mode: 'cors',
            headers: {
                'Content-type': 'application/json',
                "Authorization": localStorage.getItem("token"),
            },
            body: JSON.stringify({
                "firstname": updatefirstName,
                "lastname": updatelastName,
                "working_time": updateworkingTime,
                "trainer_contact": trainer_contact,
                "description": updatedescription
            })
        })
        .then((res) => res.json())
        .then((data) => {
            if (data.message == "Trainer information updated successfuly") {
                let edit_message_box =
                    document.getElementById("message_box");
                edit_message_box.innerHTML = data.message;
                edit_message_box.style.display = 'block';
                setTimeout(remove_message, 3000);
                setTimeout(() => {
                    window.location.href =
                        "./show_pools.htm"
                }, 3000);
            }
            else if (data.message == "Trainer not registered with us") {
                let edit_error_box = document.getElementById("edit_error_box");
                edit_error_box.innerHTML = data.message;
                edit_error_box.style.display = 'block';
                setTimeout(remove_error_edit, 3000);
            }
            else {
                edit_error_box.innerHTML = data.message;
                edit_error_box.style.display = 'block';
                setTimeout(remove_error_edit, 3000);
            }
        });
}