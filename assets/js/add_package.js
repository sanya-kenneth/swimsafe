function remove_package_error() {
    document.getElementById("package_error_box").style.display = 'none';
}

function remove_package_message() {
    document.getElementById("package_message_box").style.display = 'none';
}

let url = () => {
    let fetchpoolid = localStorage.getItem("poolDataId");
    return 'https://easyswimapi.herokuapp.com/api/v1/pools/packages' + "/".concat(fetchpoolid)
}

const addPackage = (event) => {
    event.preventDefault()
    let selectPackage = document.getElementById('select_package').value;
    let packageDetails = document.getElementById('package_details').value;
    fetch(url(), {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-type': 'application/json',
            "Authorization": localStorage.getItem("token")
        },
        body: JSON.stringify({
            "package_type": selectPackage,
            "package_details": packageDetails,
        })
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message === "Pool package was created" || data.message === "Pool package updated") {
                let message_package_box = document.getElementById("package_message_box");
                message_package_box.innerHTML = data.message;
                message_package_box.style.display = 'block';
                setTimeout(remove_package_message, 3000)
                setTimeout(() => {
                    window.location.href =
                        "./show_pools.htm"
                }, 3000)
            }
            else {
                let error_package_box = document.getElementById("package_error_box");
                error_package_box.innerHTML = data.message;
                error_package_box.style.display = 'block';
                setTimeout(remove_package_error, 3000)

            }
        })

}