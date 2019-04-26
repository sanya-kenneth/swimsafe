function remove_error() {
    document.getElementById("error_box").style.display = 'none';
}

function remove_message() {
    document.getElementById("message_box").style.display = 'none';
}

function redirectToLogin() {
    window.location.replace('../templates/index.htm')
}

const signUp = (event) => {
    event.preventDefault()
    let names = document.getElementById('names').value;
    let userEmail = document.getElementById('email').value;
    let phoneNumber = document.getElementById('phonenumber').value;
    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirm_password').value;

    fetch('https://easyswimapi.herokuapp.com/api/v1/users', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            "names": names,
            "email": userEmail,
            "phonenumber": phoneNumber,
            "password": password,
            "confirmpassword": confirmPassword

        })
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.status == 201) {
                let message_box = document.getElementById("message_box");
                message_box.innerHTML = data.message;
                message_box.style.display = 'block';
                setTimeout(remove_message, 3000)
                setTimeout(redirectToLogin(), 1000)
            }
            else {
                console.log(password);
                let error_box = document.getElementById("error_box");
                error_box.innerHTML = data.message;
                error_box.style.display = 'block';
                setTimeout(remove_error, 3000)

            }
        })

}