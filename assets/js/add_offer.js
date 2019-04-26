function remove_package_error() {
    document.getElementById("offer_error_box").style.display = 'none';
}

function remove_package_message() {
    document.getElementById("offer_message_box").style.display = 'none';
}

let url = () => {
    let fetchpoolid = localStorage.getItem("poolDataId");
    return 'https://easyswimapi.herokuapp.com/api/v1/pools/' + `${fetchpoolid}` + '/offers'
}

const addOffer = (event) => {
    event.preventDefault()
    let categoryInput = document.getElementById('offer_category').value;
    let priceInput = document.getElementById('offer_price').value;
    fetch(url(), {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-type': 'application/json',
            "Authorization": localStorage.getItem("token")
        },
        body: JSON.stringify({
            "category": categoryInput,
            "price": priceInput,
        })
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message === "Pool offer successfully created") {
                let message_package_box = document.getElementById("offer_message_box");
                message_package_box.innerHTML = data.message;
                message_package_box.style.display = 'block';
                setTimeout(remove_package_message, 3000)
                setTimeout(() => {
                    window.location.href =
                        "./show_pools.htm"
                }, 3000)
            }
            else {
                let error_package_box = document.getElementById("offer_error_box");
                error_package_box.innerHTML = data.message;
                error_package_box.style.display = 'block';
                setTimeout(remove_package_error, 3000)

            }
        })

}