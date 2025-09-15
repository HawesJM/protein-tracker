if (document.getElementById("food-form")) {
    document.getElementById("add-records").addEventListener("click", hideFoodItemsGroupOne);
}

if (document.getElementById("add-category")) {
    document.getElementById("add-category").addEventListener("click", unhideAddCategory);

}

function hideFoodItemsGroupOne() {
    let groupOne = document.getElementsByClassName("group-one");
    let groupTwo = document.getElementsByClassName("group-two");
        console.log(groupOne);
        $(groupOne).addClass("hidden");
        $(groupTwo).removeClass("hidden");
        document.getElementById("add-records-container").classList.add("hidden");
}

function unhideAddCategory() {
    document.getElementById("new-category-form").classList.remove("hidden");
    document.getElementById("add-category").classList.add("hidden");
}