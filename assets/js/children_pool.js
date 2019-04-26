function remove_error() {
    document.getElementById("error_box").style.display = 'none';
}

function remove_message() {
    document.getElementById("message_box").style.display = 'none';
}


let url = () => {
    let fetchpoolid = localStorage.getItem("poolDataId");
    return 'https://easyswimapi.herokuapp.com/api/v1/children_pools' + "/".concat(fetchpoolid)
}

const addChildPool = (event) => {
    event.preventDefault()
    let poolName = document.getElementById('name').value;
    let openingTime = document.getElementById('opening_time').value;
    let closingTime = document.getElementById('closing_time').value;
    let size = document.getElementById('size').value;
    let depth = document.getElementById('depth').value;
    let description = document.getElementById('description').value;
    let weekdayFee = document.getElementById('weekday_fee').value;
    let weekendFee = document.getElementById('weekend_fee').value;
    let available = document.getElementById('available').value;
    console.log(openingTime);

    fetch(url(), {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-type': 'application/json',
            "Authorization": localStorage.getItem("token")
        },
        body: JSON.stringify({
            "name": poolName,
            "opening_time": openingTime,
            "closing_time": closingTime,
            "size": size,
            "depth": depth,
            "description": description,
            "weekday_fee": weekdayFee,
            "weekend_fee": weekendFee,
            "available": available
        })
    })
        .then((response) => response.json())
        .then((data) => {
            // console.log()
            if (data.status == 201) {
                let message_box = document.getElementById("message_box");
                message_box.innerHTML = data.message;
                message_box.style.display = 'block';
                setTimeout(remove_message, 3000)
            }
            else {
                let error_box = document.getElementById("error_box");
                error_box.innerHTML = data.message;
                error_box.style.display = 'block';
                setTimeout(remove_error, 3000)

            }
        })

}