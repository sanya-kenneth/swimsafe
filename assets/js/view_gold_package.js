// let url = "http://127.0.0.1:5000/api/v1/pools/packages"

// const fetchgold = () => {
//     console.log("fuction called")
//     let targetPoolId = localStorage.getItem("poolDataId");
//     fetch(url + "/" + `${targetPoolId}` + "/" + "gold", {
//         method: "GET",
//         headers: {
//             "Content-type": "application/json",
//             Authorization: localStorage.getItem("token")
//         }
//     })
//         .then(res => res.json())
//         .then(data => {
//             if (data.package_type === "gold") {
//                 localStorage.setItem("gold_id", String(data.package_id))
//                 let silverPackage = document.getElementById("gold-package");
//                 let hideMessage = document.getElementById("no-gold-package");
//                 hideMessage.style.display = "none";
//                 silverPackage.style.display = "block";
//                 let silverDetails = document.getElementById("gold-package-details");
//                 let silver = document.getElementById("gold");
//                 let hr = document.createElement("hr");
//                 let package_type = document.createElement("p");
//                 let package_detail = document.createElement("p");
//                 let package_div = document.createElement("div");
//                 let deletebtn = document.createElement("button");
//                 deletebtn.setAttribute("class", "deletebtn")
//                 deletebtn.setAttribute("class", "btn")
//                 deletebtn.setAttribute("class", "btn-danger")
//                 deletebtn.addEventListener("click", deletePackage)
//                 package_type.setAttribute("class", "package_type")
//                 package_type.innerHTML = data.package_type;
//                 package_detail.innerHTML = data.package_details;
//                 silverDetails.value = data.package_details;
//                 deletebtn.innerHTML = "Delete Package";
//                 package_div.appendChild(package_type);
//                 package_div.appendChild(hr);
//                 package_div.appendChild(package_detail);
//                 package_div.appendChild(deletebtn);
//                 silver.appendChild(package_div);
//             } else if ("message" in data) {
//                 let silver_error_box = document.getElementById("gold_error_box");
//                 silver_error_box.innerHTML = data.message;
//                 silver_error_box.style.display = "block";
//             } else {
//                 let silver_error_box = document.getElementById("gold_error_box");
//                 silver_error_box.innerHTML = data.message;
//                 silver_error_box.display = "block";
//             }
//         });
// };

// const deletePackage = (event) => {
//     event.preventDefault();
//     let deleteId = localStorage.getItem("gold_id");
//     fetch("http://127.0.0.1:5000/api/v1/pools/packages" + "/" + `${deleteId}` + "/" + "delete",
//         {
//             method: 'DELETE',
//             mode: 'cors',
//             headers: {
//                 'Content-type': 'application/json',
//                 "Authorization": localStorage.getItem("token"),
//             }
//         }
//     )
//         .then((res) => res.json())
//         .then((data) => {
//             if (data.status == 204) {
//                 setTimeout(() => {
//                     window.location.href =
//                         "./view_packages.htm"
//                 }, 1000)
//                 alert(data.message)
//             }
//             else {
//                 alert(data.message)
//             }
//         })

// }
