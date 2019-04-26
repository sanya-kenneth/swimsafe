let urlDelete = "https://easyswimapi.herokuapp.com"


// Function to delete a record
let deleteMethod = (event) => {
    event.preventDefault();
    let confirmDelete = confirm("Are you sure you want to delete this swimming pool?");
    let deleteId = localStorage.getItem("poolDataId");
    if (confirmDelete == true) {
        fetch(urlDelete + "/".concat(deleteId),
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