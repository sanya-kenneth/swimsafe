
function remove_error_on_edit() {
    document.getElementById("update_failure").style.display = 'none';
}

function remove_update_message() {
    document.getElementById("update_success").style.display = 'none';
}

const editPackageDetails = (event, packageType) => {
    event.preventDefault();
    let pool_id = localStorage.getItem("poolDataId");
    let packageDetailInput;
    if (packageType === "silver") {
        packageDetailInput = document.getElementById("silver-package-details");
    }
    else if (packageType === "gold") {
        packageDetailInput = document.getElementById("gold-package-details");
    }
    else if (packageType === "platinum") {
        packageDetailInput = document.getElementById("platinum-package-details");
    }
    updatePackageDetail = packageDetailInput.value;
    let url = "https://easyswimapi.herokuapp.com/api/v1/pools/packages" + "/" + `${pool_id}`

    fetch(url,
        {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-type': 'application/json',
                "Authorization": localStorage.getItem("token"),
            },
            body: JSON.stringify({
                "package_type": packageType,
                "package_details": updatePackageDetail
            })
        })
        .then((res) => res.json())
        .then((data) => {
            if (data.message === "Pool package updated") {
                let edit_message_box =
                    document.getElementById("update_success");
                let edit_message_box_gold =
                    document.getElementById("gold_update_success");
                let edit_message_box_platinum =
                    document.getElementById("platinum_update_success");
                edit_message_box.innerHTML = data.message;
                edit_message_box_gold.innerHTML = data.message;
                edit_message_box_platinum.innerHTML = data.message;
                if (packageType === "silver") {
                    edit_message_box.style.display = 'block';
                }
                else if (packageType === "gold") {
                    edit_message_box_gold.style.display = 'block';
                }
                else {
                    edit_message_box_platinum.style.display = 'block';
                }
                setTimeout(remove_update_message, 3000);
                setTimeout(() => {
                    window.location.href =
                        "./view_packages.htm"
                }, 3000);
            }
            else if (data.message == "Swimmig pool not found") {
                let edit_error_box = document.getElementById("update_failure");
                edit_error_box.innerHTML = data.message;
                edit_error_box.style.display = 'block';
                setTimeout(remove_error_on_edit, 3000);
            }
            else {
                edit_error_box.innerHTML = data.message;
                edit_error_box.style.display = 'block';
                setTimeout(remove_error_on_edit, 3000);
            }
        });
}
