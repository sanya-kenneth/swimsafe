
let remove_offer_error = () => {
    document.getElementById("error_box").style.display = "none";
}

let fetchOfferUrl = (Poolid) => {
    return "https://easyswimapi.herokuapp.com/api/v1/pools/" + `${Poolid}` + "/" + "offers";
};

let showOffers = data => {
    let displayOffers = document.getElementById("offer_div");
    displayOffers.innerHTML = "";
    data.forEach(offer => {
        // document.getElementById(String(offer.pool_offer_id)).style.display = "none";
        let CategoryData = document.createElement("p");
        let PriceData = document.createElement("p");
        let infoContainer = document.createElement("div");
        CategoryData.innerHTML = offer.category;
        PriceData.innerHTML = offer.price;
        let datacard = document.createElement("div");
        let br = document.createElement("br");
        let Delete = document.createElement("button");
        let Update = document.createElement("button")
        let update_div = document.createElement("div");
        let update_category = document.createElement("textarea");
        let update_price = document.createElement("input");
        update_category.value = offer.category;
        update_price.value = offer.price;
        update_category.setAttribute("type", "text-area");
        update_price.setAttribute("type", "text");
        update_category_id = "update_category" + String(offer.pool_offer_id);
        update_category.setAttribute("id", update_category_id);
        update_price_id = "update_price" + String(offer.pool_offer_id);
        update_price.setAttribute("id", update_price_id);
        update_div.setAttribute("id", String(offer.pool_offer_id));
        update_price.setAttribute("class", "update_price");
        update_category.setAttribute("class", "update_category");
        Delete.setAttribute("id", "delete_offer_btn");
        Delete.innerHTML = "Delete";
        Update.setAttribute("id", "update_offer_btn");
        Update.innerHTML = "Update";
        Delete.setAttribute("class", "w3-round-large");
        Update.setAttribute("class", "w3-round-large");
        datacard.setAttribute("id", "offer_card");
        datacard.setAttribute("class", "offer_card");
        datacard.setAttribute("class", "w3-card-4");
        datacard.setAttribute("class", "w3-white");
        datacard.setAttribute("class", "hvr-grow-shadow");
        CategoryData.setAttribute("class", "category");
        CategoryData.setAttribute("id", "category");
        PriceData.setAttribute("class", "price");
        PriceData.setAttribute("id", "price");
        infoContainer.setAttribute("class", "offer_info");
        Delete.addEventListener("click", () => { deleteOffer(offer.pool_offer_id); });
        Update.addEventListener("click", () => {
            editOffer(offer.pool_offer_id);

        })
        datacard.addEventListener("click", () => {
            localStorage.setItem("offerDataId", offer.pool_offer_id);
        });
        update_div.appendChild(update_category);
        update_div.appendChild(update_price);
        infoContainer.appendChild(CategoryData);
        infoContainer.appendChild(PriceData);
        datacard.appendChild(infoContainer);
        datacard.appendChild(br);
        datacard.appendChild(update_div);
        datacard.appendChild(Update);
        datacard.appendChild(Delete);
        let display = document.getElementById("offer_div");
        display.appendChild(datacard);
    });
};

const fetchOffers = (poolId) => {
    fetch(fetchOfferUrl(poolId), {
        method: "GET",
        headers: {
            "Content-type": "application/json",
            Authorization: localStorage.getItem("token")
        }
    })
        .then(res => res.json())
        .then(data => {
            if ("data" in data) {
                data = data.data.reverse();
                showOffers(data);
            } else if ("message" in data) {
                let error_box = document.getElementById("offer_error_box");
                error_box.innerHTML = data.message;
                error_box.style.display = "block";
            } else {
                let error_box = document.getElementById("offer_error_box");
                error_box.innerHTML = data.error;
                error_box.style.display = "block";
            }
        });
};