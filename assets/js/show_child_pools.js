// show children pools
// let showChildPool = data => {
//     ChildInfo = data
//     ChildInfo.forEach(childPool => {
//         let childName = document.createElement("p");
//         let childSize = document.createElement("p");
//         let childWeekDayFee = document.createElement("p");
//         let childWeekendFee = document.createElement("p");
//         let childAvailability = document.createElement("p");
//         let childDepth = document.createElement("img");
//         childName.innerHTML = childPool.name;
//         childSize.innerHTML = childPool.size;
//         childWeekDayFee.innerHTML = childPool.weekday_fee;
//         childWeekendFee.innerHTML = childPool.weekend_fee;
//         childAvailability.innerHTML = childPool.availability;
//         childDepth.innerHTML = childPool.depth;
//         let childPoolCard = document.createElement("div");
//         let childPoolCardBody = document.createElement("div");
//         childPoolCard.setAttribute("id", "childpool-card");
//         childPoolCard.setAttribute("class", "childpool_card");
//         childPoolCard.setAttribute("class", "w3-card");
//         trainerImage.setAttribute("src", "assets/images/bg1.jpg");
//         trainerImage.setAttribute("class", "card-img-top");
//         trainerImage.setAttribute("class", "trainer-img");
//         childPoolCardBody.setAttribute("class", "card-body");
//         childName.setAttribute("class", "card-text");
//         childSize.setAttribute("class", "card-text");
//         childWeekDayFee.setAttribute("class", "card-text");
//         childWeekendFee.setAttribute("class", "card-text");
//         childAvailability.setAttribute("class", "card-text");
//         childDepth.setAttribute("class", "card-text");
//         firstName.setAttribute("id", "firstname");
//         lastName.setAttribute("id", "lastname");
//         description.setAttribute("id", "desc");
//         workingTime.setAttribute("id", "worktime");
//         availability.setAttribute("id", "avail");
//         childPoolCard.addEventListener("click", () => {
//             localStorage.setItem("childPoolDataId", childPool.child_pool_id);
//         });
//         childPoolCard.appendChild(trainerImage);
//         childPoolCardBody.appendChild(childName);
//         childPoolCardBody.appendChild(childSize);
//         childPoolCardBody.appendChild(childWeekDayFee);
//         childPoolCardBody.appendChild(childWeekendFee);
//         childPoolCardBody.appendChild(childAvailability);
//         childPoolCardBody.appendChild(childDepth)
//         childPoolCard.appendChild(childPoolCardBody);
//         let childPool_card_remove = document.getElementById("childpool-card");
//         if (childPool_card_remove) {
//             childPool_card_remove.parentNode.removeChild(childPool_card_remove);
//         }
//         let displayChildPool = document.getElementById("child-pool-div");
//         displayChildPool.appendChild(childPoolCard);
//         // trainer_card_remove.style.display = "block";
//     });
// };

// export const fetchChildPools = () => {
//     let fetchpoolid = localStorage.getItem("poolDataId");
//     console.log(fetchpoolid)
//     fetch("http://127.0.0.1:5000/api/v1/" + `${fetchpoolid}` + "/children_pools", {
//         method: "GET",
//         headers: {
//             "Content-type": "application/json",
//             Authorization: localStorage.getItem("token")
//         }
//     })
//         .then(res => res.json())
//         .then(data => {
//             if ("data" in data) {
//                 // localStorage.removeItem("pool_trainers");
//                 // localStorage.setItem("pool_trainers", JSON.stringify(data.data));
//                 // trainers = document.getElementById("trainer-div");
//                 // trainer_diplayed = document.getElementById("trainer-card");
//                 let error_box = document.getElementById("trainer_error_box");
//                 if (error_box) {
//                     error_box.style.display = "none";
//                 }
//                 // info = JSON.parse(localStorage.getItem("pool_trainers"));
//                 console.log(data.data);
//                 error_box = document.getElementById("trainer_error_box");
//                 showChildPool(data.data);
//             } else if ("message" in data) {
//                 let remove_card = document.getElementById("childpool-card");
//                 if (remove_card) {
//                     remove_card.style.display = "none";
//                 }
//                 let error_box = document.getElementById("trainer_error_box");
//                 error_box.innerHTML = data.message;
//                 error_box.style.display = "block";
//             } else {
//                 let remove_card = document.getElementById("trainer-card");
//                 if (remove_card) {
//                     remove_card.style.display = "none";
//                 }
//                 let error_box = document.getElementById("trainer_error_box");
//                 error_box.innerHTML = data.error;
//                 error_box.style.display = "block";
//             }
//         });
// };