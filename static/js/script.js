if (document.getElementById("food-form")) {
    document.getElementById("add-records").addEventListener("click", hideFoodItemsGroupOne);
}

function hideFoodItemsGroupOne() {
    let groupOne = document.getElementsByClassName("group-one");
    let groupTwo = document.getElementsByClassName("group-two");
        console.log(groupOne);
        $(groupOne).addClass("hidden");
        $(groupTwo).removeClass("hidden");
        document.getElementById("add-records-container").classList.add("hidden");
}