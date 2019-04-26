let OfferurlDelete = "https://easyswimapi.herokuapp.com/api/v1/pools/offers"


// Function to delete a pool offer
let deleteOffer = (offerId) => {
    let confirmDeleteOffer = confirm("Are you sure you want to delete this swimming pool offer?");
    if (confirmDeleteOffer == true) {
        fetch(OfferurlDelete + "/".concat(offerId),
            {
                method: 'DELETE',
                mode: 'cors',
                headers: {
                    'Content-type': 'application/json',
                    "Authorization": localStorage.getItem("token"),
                }
            }
        )
            .then((res) => res.json())
            .then((data) => {
                if (data.status == 204) {
                    setTimeout(() => {
                        window.location.href =
                            "./show_pools.htm"
                    }, 1000)
                    alert(data.message)
                }
                else {
                    alert(data.message)
                }
            })
    }
}