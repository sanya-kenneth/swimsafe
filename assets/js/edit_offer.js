function remove_error_on_edit() {
    document.getElementById("update_failure").style.display = 'none';
}

function remove_update_message() {
    document.getElementById("update_success").style.display = 'none';
}

const editOffer = (offer_id) => {
    category_id = "update_category" + String(offer_id);
    price_id = "update_price" + String(offer_id);
    let Incategory = document.getElementById(category_id);
    let Inprice = document.getElementById(price_id);
    console.log(Incategory.value)
    console.log(Inprice.value)
    let url = "https://easyswimapi.herokuapp.com/api/v1/pools/offers" + "/" + `${offer_id}`

    fetch(url,
        {
            method: 'PUT',
            mode: 'cors',
            headers: {
                'Content-type': 'application/json',
                "Authorization": localStorage.getItem("token"),
            },
            body: JSON.stringify({
                "category": Incategory.value,
                "price": Inprice.value
            })
        })
        .then((res) => res.json())
        .then((data) => {
            if (data.message === "Update was successful") {
                setTimeout(() => {
                    window.location.href =
                        "./show_pools.htm"
                }, 3000);
            }

        });
}
