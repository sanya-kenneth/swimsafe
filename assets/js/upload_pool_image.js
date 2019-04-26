let pool_id = localStorage.getItem("poolDataId");
let spinner = document.getElementById("upload-spinner");
let url = "https://easyswimapi.herokuapp.com/api/v1/pools/upload/" + `${pool_id}`

function remove_error_upload() {
    document.getElementById("upload_error_box").style.display = 'none';
}

function remove_message_upload() {
    document.getElementById("upload_message_box").style.display = 'none';
}

const form = document.querySelector('form')
form.addEventListener('submit', e => {
    e.preventDefault()
    const file = document.querySelector('[type=file]').files[0]
    const formData = new FormData()
    spinner.style.display = "block";
    formData.append('file', file)
    fetch(url, {
        method: 'POST',
        headers: {
            "Authorization": localStorage.getItem("token"),
        },
        body: formData,
    }).then((response) => response.json())
        .then((data) => {
            if (data.message === "Image uploaded successfully") {
                spinner.style.display = "none";
                let message_box = document.getElementById("upload_message_box");
                message_box.innerHTML = data.message;
                message_box.style.display = 'block';
                setTimeout(() => { remove_message_upload(); }, 3000)
            }
            else {
                spinner.style.display = "none";
                let error_box = document.getElementById("upload_error_box");
                error_box.innerHTML = data.message;
                error_box.style.display = 'block';
                setTimeout(remove_error_upload, 3000)
            }
        })
})
