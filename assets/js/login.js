function remove_error() {
    document.getElementById("error_box").style.display = 'none';
}

function remove_message() {
    document.getElementById("message_box").style.display = 'none';
}


const logIn = (event) => {
    event.preventDefault()
    let userEmail = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    fetch('https://easyswimapi.herokuapp.com/api/v1/users/login', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            "email": userEmail,
            "password": password
        })
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message == "You are now loggedin") {
                let message_box = document.getElementById("message_box");
                message_box.innerHTML = data.message;
                message_box.style.display = 'block';
                setTimeout(remove_message, 3000)
                localStorage.setItem("token", data.access_token)
                setTimeout(() => {
                    window.location.href =
                        "./show_pools.htm"
                }, 3000)
            }
            else {
                let error_box = document.getElementById("error_box");
                error_box.innerHTML = data.message;
                error_box.style.display = 'block';
                setTimeout(remove_error, 3000)
            }
        })

}