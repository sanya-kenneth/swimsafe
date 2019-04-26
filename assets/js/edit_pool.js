
function remove_error_edit() {
    document.getElementById("edit_error_box").style.display = 'none';
}

function remove_message() {
    document.getElementById("message_box").style.display = 'none';
}

function Cancel() {
    document.getElementById("dataModal").style.display = 'none';
}

let updatePoolname = document.getElementById("update_poolname");
let updatePooldepth = document.getElementById("update_depth");
let updatePoolsize = document.getElementById("update_size");
let updatePooladdress = document.getElementById("update_address");
let updatePoolopening = document.getElementById("update_openingtime");
let updatePoolclosing = document.getElementById("update_closingtime");
let updatePoolweekday = document.getElementById("update_weekday");
let updatePoolweekend = document.getElementById("update_weekend");
let updadePooldescription = document.getElementById("update_description");

const loadInfo = () => {
    let pool_id = localStorage.getItem("poolDataId");
    fetch("https://easyswimapi.herokuapp.com/api/v1/pools" + "/" + `${pool_id}`, {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            Authorization: localStorage.getItem("token")
        }
    })
        .then(res => res.json())
        .then(data => {
            if ("data" in data) {
                updatePoolname.value = data.data['pool_name']
                updatePooldepth.value = data.data['depth']
                updatePoolsize.value = data.data['size']
                updatePooladdress.value = data.data['pool_address']
                updatePoolopening.value = data.data['opening_time']
                updatePoolclosing.value = data.data['closing_time']
                updatePoolweekday.value = data.data['weekday_fee']
                updatePoolweekend.value = data.data['weekdend_fee']
                updadePooldescription.value = data.data['description']

            }
        });
}

const editPoolInfo = (event) => {
    event.preventDefault();
    let pool_id = localStorage.getItem("poolDataId");
    updatePoolname = updatePoolname.value;
    updatePooldepth = updatePooldepth.value;
    updatePoolsize = updatePoolsize.value;
    updatePooladdress = updatePooladdress.value;
    updatePoolopening = updatePoolopening.value;
    updatePoolclosing = updatePoolclosing.value;
    updatePoolweekday = updatePoolweekday.value;
    updatePoolweekend = updatePoolweekend.value;
    updadePooldescription = updadePooldescription.value;
    let url = "https://easyswimapi.herokuapp.com/api/v1/pools" + "/" + `${pool_id}` + "/".concat("update")

    fetch(url,
        {
            method: 'PUT',
            mode: 'cors',
            headers: {
                'Content-type': 'application/json',
                "Authorization": localStorage.getItem("token"),
            },
            body: JSON.stringify({
                "pool_name": String(updatePoolname),
                "size": updatePoolsize,
                "depth": updatePooldepth,
                "pool_address": updatePooladdress,
                "opening_time": updatePoolopening,
                "closing_time": updatePoolclosing,
                "weekday_fee": updatePoolweekday,
                "weekend_fee": updatePoolweekend,
                "description": updadePooldescription

            })
        })
        .then((res) => res.json())
        .then((data) => {
            if (data.message == "Update was successful") {
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
            else if (data.message == "Swimmig pool not found") {
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