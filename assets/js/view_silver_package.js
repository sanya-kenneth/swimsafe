let url = "https://easyswimapi.herokuapp.com/api/v1/pools/packages"

const fetchsilverPackage = () => {
    let targetPoolId = localStorage.getItem("poolDataId");
    fetch(url + "/" + `${targetPoolId}` + "/" + "silver", {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            Authorization: localStorage.getItem("token")
        }
    })
        .then(res => res.json())
        .then(data => {
            if (data.package_type === "silver") {
                localStorage.setItem("silver_id", String(data.package_id))
                let silverPackage = document.getElementById("silver-package");
                let hideMessage = document.getElementById("no-silver-package");
                hideMessage.style.display = "none";
                silverPackage.style.display = "block";
                let silverDetails = document.getElementById("silver-package-details");
                let silver = document.getElementById("silver");
                let hr = document.createElement("hr");
                let package_type = document.createElement("p");
                let package_detail = document.createElement("p");
                let package_div = document.createElement("div");
                let deletebtn = document.createElement("button");
                deletebtn.setAttribute("class", "deletebtn")
                deletebtn.setAttribute("class", "btn")
                deletebtn.setAttribute("class", "btn-danger")
                deletebtn.addEventListener("click", deletesilverPackage)
                package_type.setAttribute("class", "package_type")
                package_type.innerHTML = data.package_type;
                package_detail.innerHTML = data.package_details;
                silverDetails.value = data.package_details;
                deletebtn.innerHTML = "Delete Package";
                package_div.appendChild(package_type);
                package_div.appendChild(hr);
                package_div.appendChild(package_detail);
                package_div.appendChild(deletebtn);
                silver.appendChild(package_div);
            } else if ("message" in data) {
                let silver_error_box = document.getElementById("silver_error_box");
                silver_error_box.innerHTML = data.message;
                silver_error_box.style.display = "block";
            } else {
                let silver_error_box = document.getElementById("silver_error_box");
                silver_error_box.innerHTML = data.message;
                silver_error_box.display = "block";
            }
        });
};

const fetchgold = () => {
    let targetPoolId = localStorage.getItem("poolDataId");
    fetch(url + "/" + `${targetPoolId}` + "/" + "gold", {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            Authorization: localStorage.getItem("token")
        }
    })
        .then(res => res.json())
        .then(data => {
            if (data.package_type === "gold") {
                localStorage.setItem("gold_id", String(data.package_id))
                let silverPackage = document.getElementById("gold-package");
                let hideMessage = document.getElementById("no-gold-package");
                hideMessage.style.display = "none";
                silverPackage.style.display = "block";
                let silverDetails = document.getElementById("gold-package-details");
                let silver = document.getElementById("gold");
                let hr = document.createElement("hr");
                let package_type = document.createElement("p");
                let package_detail = document.createElement("p");
                let package_div = document.createElement("div");
                let deletebtn = document.createElement("button");
                deletebtn.setAttribute("class", "deletebtn")
                deletebtn.setAttribute("class", "btn")
                deletebtn.setAttribute("class", "btn-danger")
                deletebtn.addEventListener("click", deletegoldPackage)
                package_type.setAttribute("class", "package_type")
                package_type.innerHTML = data.package_type;
                package_detail.innerHTML = data.package_details;
                silverDetails.value = data.package_details;
                deletebtn.innerHTML = "Delete Package";
                package_div.appendChild(package_type);
                package_div.appendChild(hr);
                package_div.appendChild(package_detail);
                package_div.appendChild(deletebtn);
                silver.appendChild(package_div);
            } else if ("message" in data) {
                let silver_error_box = document.getElementById("gold_error_box");
                silver_error_box.innerHTML = data.message;
                silver_error_box.style.display = "block";
            } else {
                let silver_error_box = document.getElementById("gold_error_box");
                silver_error_box.innerHTML = data.message;
                silver_error_box.display = "block";
            }
        });
};

const platinumDataDetails = () => {
    console.log("function platinum called")
    let targetPoolId = localStorage.getItem("poolDataId");
    fetch(url + "/" + `${targetPoolId}` + "/" + "platinum", {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            Authorization: localStorage.getItem("token")
        }
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            if (data.package_type === "platinum") {
                localStorage.setItem("platinum_id", String(data.package_id))
                let platinumPackage = document.getElementById("platinum-package");
                let hideMessage = document.getElementById("no-platinum-package");
                hideMessage.style.display = "none";
                platinumPackage.style.display = "block";
                let platinumDetails = document.getElementById("platinum-package-details");
                let platinum = document.getElementById("platinum");
                let phr = document.createElement("hr");
                let package_type = document.createElement("p");
                let package_detail = document.createElement("p");
                let package_div = document.createElement("div");
                let deletebtn = document.createElement("button");
                deletebtn.setAttribute("class", "deletebtn")
                deletebtn.setAttribute("class", "btn")
                deletebtn.setAttribute("class", "btn-danger")
                deletebtn.addEventListener("click", deleteplatinumPackage)
                package_type.setAttribute("class", "package_type")
                package_type.innerHTML = data.package_type;
                package_detail.innerHTML = data.package_details;
                platinumDetails.value = data.package_details;
                deletebtn.innerHTML = "Delete Package";
                package_div.appendChild(package_type);
                package_div.appendChild(phr);
                package_div.appendChild(package_detail);
                package_div.appendChild(deletebtn);
                platinum.appendChild(package_div);
            } else if ("message" in data) {
                let platinum_error_box = document.getElementById("platinum_error_box");
                platinum_error_box.innerHTML = data.message;
                platinum_error_box.style.display = "block";
            } else {
                let platinum_error_box = document.getElementById("platinum_error_box");
                platinum_error_box.innerHTML = data.message;
                platinum_error_box.display = "block";
            }
        });
};

const deletegoldPackage = (event) => {
    event.preventDefault();
    let deleteId = localStorage.getItem("gold_id");
    fetch("https://easyswimapi.herokuapp.com/api/v1/pools/packages" + "/" + `${deleteId}` + "/" + "delete",
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
                        "./view_packages.htm"
                }, 1000)
                alert(data.message)
            }
            else {
                alert(data.message)
            }
        })

}


const deletesilverPackage = (event) => {
    event.preventDefault();
    let deleteId = localStorage.getItem("silver_id");
    fetch("https://easyswimapi.herokuapp.com/api/v1/pools/packages" + "/" + `${deleteId}` + "/" + "delete",
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
                        "./view_packages.htm"
                }, 1000)
                alert(data.message)
            }
            else {
                alert(data.message)
            }
        })
}

const deleteplatinumPackage = (event) => {
    event.preventDefault();
    let deleteId = localStorage.getItem("platinum_id");
    fetch("https://easyswimapi.herokuapp.com/api/v1/pools/packages" + "/" + `${deleteId}` + "/" + "delete",
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
                        "./view_packages.htm"
                }, 1000)
                alert(data.message)
            }
            else {
                alert(data.message)
            }
        })
}
