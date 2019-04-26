// import "./show_child_pools";

let remove_error = () => {
  document.getElementById("error_box").style.display = "none";
}

let fetchUrl = () => {
  return "https://easyswimapi.herokuapp.com/api/v1/pools";
};

let showData = data => {
  data.forEach(incident => {
    let poolName = document.createElement("p");
    let image = document.createElement("img");
    let size = document.createElement("h6");
    let depth = document.createElement("h6");
    let meta1 = document.createElement("div");
    let meta2 = document.createElement("div");
    let sizeData = document.createElement("p");
    let depthData = document.createElement("p");
    let infoContainer = document.createElement("div");
    sizeData.innerHTML = incident.size;
    depthData.innerHTML = incident.depth;
    size.innerHTML = "size:";
    depth.innerHTML = "depth:";
    let datacard = document.createElement("div");
    let br = document.createElement("br");
    poolName.innerHTML = incident.pool_name;
    if (incident.pool_thumbnail !== null) {
      let pic = incident.pool_thumbnail;
      image.setAttribute("src", pic);
    }
    else {
      let pic = "./assets/images/default.jpg"
      image.setAttribute("src", pic);
    }
    image.setAttribute("class", "pool_img");
    datacard.setAttribute("id", "data_card");
    datacard.setAttribute("class", "w3-card-4");
    datacard.setAttribute("class", "w3-white");
    datacard.setAttribute("class", "hvr-grow-shadow");
    size.setAttribute("class", "meta1");
    sizeData.setAttribute("class", "size");
    depth.setAttribute("class", "meta2");
    depthData.setAttribute("class", "depth");
    infoContainer.setAttribute("class", "info");
    meta1.setAttribute("class", "hold1");
    meta2.setAttribute("class", "hold2");
    poolName.setAttribute("class", "pool_name");
    datacard.addEventListener("click", () => {
      localStorage.setItem("poolDataId", incident.pool_id);
      fetchOneIncident();
      activateModal();
    });
    datacard.appendChild(image);
    infoContainer.appendChild(poolName);
    infoContainer.appendChild(meta1);
    infoContainer.appendChild(meta2);
    meta1.appendChild(size);
    meta1.appendChild(sizeData);
    meta2.appendChild(depth);
    meta2.appendChild(depthData);
    datacard.appendChild(infoContainer);
    datacard.appendChild(br);
    let display = document.getElementById("display_record");
    display.appendChild(datacard);
  });
};

let fetchOne = data => {
  let poolName = document.getElementById("pool_name");
  let depth = document.getElementById("depth");
  let size = document.getElementById("size");
  let address = document.getElementById("address");
  let weekday = document.getElementById("weekday");
  let openingTime = document.getElementById("opening_time");
  let closingTime = document.getElementById("closing_time");
  let weekend = document.getElementById("weekend");
  let availability = document.getElementById("availability");
  // let pic = `${data.pool_thumbnail}`;
  let pool_pic = document.getElementById("pool_photo");
  let description = document.getElementById("pool_description");
  poolName.innerHTML = data.pool_name;
  depth.innerHTML = data.depth;
  size.innerHTML = data.size;
  address.innerHTML = data.pool_address;
  weekday.innerHTML = data.weekday_fee;
  openingTime.innerHTML = data.opening_time;
  closingTime.innerHTML = data.closing_time;
  weekend.innerHTML = data.weekdend_fee
  availability.innerHTML = data.availability;
  description.innerHTML = data.description;
  if (data.pool_thumbnail !== null) {
    let pic = data.pool_thumbnail;
    pool_pic.setAttribute("src", pic);
  }
  else {
    let pic = "./assets/images/default.jpg"
    pool_pic.setAttribute("src", pic);
  }
};

const fetchPools = () => {
  fetch(fetchUrl(), {
    method: "GET",
    headers: {
      "Content-type": "application/json",
      Authorization: localStorage.getItem("token")
    }
  })
    .then(res => res.json())
    .then(data => {
      //   console.log(data.data);
      if ("data" in data) {
        data = data.data.reverse();

        showData(data);
      } else if ("message" in data) {
        let error_box = document.getElementById("error_box");
        error_box.innerHTML = data.message;
        error_box.style.display = "block";
      } else {
        let error_box = document.getElementById("error_box");
        error_box.innerHTML = data.error;
        error_box.style.display = "block";
      }
    });
};

const fetchOneIncident = () => {
  // import fetchChildPools from "./show_child_pools";
  let poolid = localStorage.getItem("poolDataId");
  // console.log(poolid);
  fetch(fetchUrl() + "/".concat(poolid), {
    method: "GET",
    headers: {
      "Content-type": "application/json",
      Authorization: localStorage.getItem("token")
    }
  })
    .then(res => res.json())
    .then(data => {
      if ("data" in data) {
        fetchOne(data.data);
        fetchTrainers();
        fetchOffers(data.data.pool_id);
        loadTrainers();
        // showSubs();
        // fetchChildPools();
        statistcs();
      } else if ("message" in data) {
        let error_box = document.getElementById("error_box");
        error_box.innerHTML = data.message;
        error_box.style.display = "block";
      } else {
        let error_box = document.getElementById("error_box");
        error_box.innerHTML = data.message;
        error_box.style.display = "block";
      }
    });
};

// Get the modal
var modal = document.getElementById("dataModal");

// Get the button that opens the modal
var activate = document.getElementById("comment");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
function activateModal() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function closeModal() {
  modal.style.display = "none";
  window.location.href = "./show_pools.htm";
}

// When the user clicks anywhere outside of the modal, close it
// window.onclick = function (event) {
//   if (event.target == modal) {
//     // modal.style.display = "none";
//   }
// };

let switchTab = (event, tabName) => {
  let i, tabcontent, tabLink;
  document.getElementById("Record_details").style.display = "block";
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tabLink = document.getElementsByClassName("tablinks");
  for (i = 0; i < tabLink.length; i++) {
    tabLink[i].className = tabLink[i].className.replace("active", "");
  }
  document.getElementById(tabName).style.display = "block";
  event.currentTarget.className += " active";
};
let detailsView = () => {
  let viewInfo = document.getElementById("Record_details");
  viewInfo.style.display = "block";
};

let currentTrainerId;
// show trainers
let showTrainers = data => {
  let displayTrainer = document.getElementById("trainer-div");
  displayTrainer.innerHTML = "";
  data.forEach((t) => {
    let firstName = document.createElement("p");
    let lastName = document.createElement("p");
    let description = document.createElement("p");
    let workingTime = document.createElement("p");
    let trainer_contact = document.createElement("p");
    let availability = document.createElement("p");
    let imageDiv = document.createElement("div");
    let trainerImage = document.createElement("img");
    let deletetTrainerBtn = document.createElement("button");
    let editTrainerBtn = document.createElement("button");
    firstName.innerHTML = t.first_name;
    lastName.innerHTML = t.last_name;
    description.innerHTML = t.description;
    workingTime.innerHTML = t.working_time;
    trainer_contact.innerHTML = t.trainer_contact;
    availability.innerHTML = t.availability;
    deletetTrainerBtn.innerHTML = "Delete";
    editTrainerBtn.innerHTML = "Update";
    let trainerCard = document.createElement("div");
    let trainerCardBody = document.createElement("div");
    trainerCard.setAttribute("id", "trainer-card");
    trainerCard.setAttribute("class", "trainer_card");
    trainerCard.setAttribute("class", "w3-card");
    imageDiv.setAttribute("class", "trainer-image-div");
    if (t.trainer_img !== null) {
      let pic = t.trainer_img;
      trainerImage.setAttribute("src", pic);
    }
    else {
      let pic = "./assets/images/swimming.png";
      trainerImage.setAttribute("src", pic);
    }
    trainerImage.setAttribute("class", "card-img-top");
    trainerImage.setAttribute("class", "trainer-img");
    trainerCardBody.setAttribute("class", "card-body");
    firstName.setAttribute("class", "card-text");
    lastName.setAttribute("class", "card-text");
    description.setAttribute("class", "card-text");
    workingTime.setAttribute("class", "card-text");
    trainer_contact.setAttribute("class", "card-text")
    availability.setAttribute("class", "card-text");
    firstName.setAttribute("id", "firstname");
    lastName.setAttribute("id", "lastname");
    description.setAttribute("id", "desc");
    workingTime.setAttribute("id", "worktime");
    trainer_contact.setAttribute("id", "trainer_contact");
    availability.setAttribute("id", "avail");
    editTrainerBtn.setAttribute('class', 'btn');
    editTrainerBtn.setAttribute('class', 'btn-primary');
    editTrainerBtn.setAttribute('id', 'edit-trainer');
    deletetTrainerBtn.setAttribute('class', 'btn');
    deletetTrainerBtn.setAttribute('class', 'btn-danger');
    deletetTrainerBtn.setAttribute('id', 'delete-trainer');
    imageDiv.appendChild(trainerImage);
    trainerCard.appendChild(imageDiv);
    trainerCardBody.appendChild(firstName);
    trainerCardBody.appendChild(lastName);
    trainerCardBody.appendChild(description);
    trainerCardBody.appendChild(workingTime);
    trainerCardBody.appendChild(trainer_contact);
    trainerCardBody.appendChild(availability);
    trainerCard.appendChild(trainerCardBody);
    trainerCard.appendChild(deletetTrainerBtn);
    trainerCard.appendChild(editTrainerBtn);
    displayTrainer.appendChild(trainerCard);
    trainerCard.addEventListener("click", () => {
      localStorage.setItem("trainerDataId", t.trainer_id);
    });
    editTrainerBtn.addEventListener("click", (e) => {
      e.preventDefault();
      localStorage.setItem("trainerDataId", t.trainer_id);
      console.log(localStorage.getItem("trainerDataId"))
      window.location.href =
        "./edit_trainer.htm"
    })

    deletetTrainerBtn.addEventListener("click", (e) => { e.preventDefault(); deleteTrainer(t.trainer_id) })
  });
};

const fetchTrainers = () => {
  let fetchpoolid = localStorage.getItem("poolDataId");
  fetch("https://easyswimapi.herokuapp.com/api/v1/trainers/pool" + "/".concat(fetchpoolid), {
    method: "GET",
    headers: {
      "Content-type": "application/json",
      Authorization: localStorage.getItem("token")
    }
  })
    .then(res => res.json())
    .then(data => {
      if ("data" in data) {
        localStorage.removeItem("pool_trainers");
        if (fetchpoolid === data.data[0]["pool_id"]) {
          localStorage.setItem("numberOfTrainers", data.data.length)
        }
        localStorage.setItem("pool_trainers", JSON.stringify(data.data));
        trainers = document.getElementById("trainer-div");
        trainer_diplayed = document.getElementById("trainer-card");
        let error_box = document.getElementById("trainer_error_box");
        if (error_box) {
          error_box.style.display = "none";
        }
        info = JSON.parse(localStorage.getItem("pool_trainers"));
        error_box = document.getElementById("trainer_error_box");
        showTrainers(info);
      } else if ("message" in data) {
        let remove_card = document.getElementById("trainer-card");
        if (remove_card) {
          remove_card.style.display = "none";
        }
        let error_box = document.getElementById("trainer_error_box");
        error_box.innerHTML = data.message;
        error_box.style.display = "block";
      } else {
        localStorage.setItem("numberOfTrainers", 0)
        let remove_card = document.getElementById("trainer-card");
        if (remove_card) {
          remove_card.style.display = "none";
        }
        let error_box = document.getElementById("trainer_error_box");
        error_box.innerHTML = data.error;
        error_box.style.display = "block";
      }
    });
};

let statistcs = () => {
  let fetchpoolId = localStorage.getItem("poolDataId");
  fetch("https://easyswimapi.herokuapp.com/api/v1/pools/" + `${fetchpoolId}` + "/" + "statistics", {
    method: "GET",
    headers: {
      "Content-type": "application/json",
      Authorization: localStorage.getItem("token")
    }
  })
    .then(res => res.json())
    .then(data => {
      showSubs(data)
    });
};

let showSubs = (data) => {
  let stats = document.getElementById("show_statistics")
  let numberOfSubscribers = data.Subscribers;
  let numberOfTrainers = data.Trainers;
  let subscriber = document.createElement("p");
  let trainers = document.createElement("p")
  let stats_div = document.createElement("div")
  subscriber.setAttribute("id", "subscriber");
  trainers.setAttribute("id", "trainers");
  stats_div.setAttribute("id", "stats-div")
  // subscriber.setAttribute("class", "badge badge-secondary")
  // trainers.setAttribute("class", "badge badge-secondary")
  subscriber.innerHTML = numberOfSubscribers;
  trainers.innerHTML = numberOfTrainers;
  stats_div.appendChild(trainers);
  stats_div.appendChild(subscriber);
  let stats_card_remove = document.getElementById("stats-div");
  if (stats_card_remove) {
    stats_card_remove.parentNode.removeChild(stats_card_remove);
  }
  stats.appendChild(stats_div);
}

const deleteTrainer = (deleteId) => {
  let deleteTrainerId = localStorage.getItem("trainerDataId");
  console.log(deleteTrainerId)
  fetch("https://easyswimapi.herokuapp.com/api/v1/trainers/" + `${deleteId}` + "/" + "delete",
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

