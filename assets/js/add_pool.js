function remove_error() {
    document.getElementById("error_box").style.display = 'none';
}

function remove_message() {
    document.getElementById("message_box").style.display = 'none';
}


let url = () => {
    return 'https://easyswimapi.herokuapp.com/api/v1/pools'
}

const addPool = (event) => {
    event.preventDefault()
    let name = document.getElementById('name').value;
    let address = document.getElementById('address').value;
    let latCordinate = Number(document.getElementById('location_lat').value);
    let longCordinate = Number(document.getElementById('location_long').value);
    let openingTime = document.getElementById('opening_time').value;
    let closingTime = document.getElementById('closing_time').value;
    let size = document.getElementById('size').value;
    let depth = document.getElementById('depth').value;
    let description = document.getElementById('description').value;
    let weekdayFee = document.getElementById('weekday_fee').value;
    let weekendFee = document.getElementById('weekend_fee').value;
    let available = document.getElementById('availability').value;

    fetch(url(), {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-type': 'application/json',
            "Authorization": localStorage.getItem("token")
        },
        body: JSON.stringify({
            "pool_name": name,
            "pool_address": address,
            "location_lat": latCordinate,
            "location_long": longCordinate,
            "opening_time": openingTime,
            "closing_time": closingTime,
            "size": size,
            "depth": depth,
            "description": description,
            "weekday_fee": weekdayFee,
            "weekend_fee": weekendFee,
            "available": available,
        })
    })
        .then((response) => response.json())
        .then((data) => {
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