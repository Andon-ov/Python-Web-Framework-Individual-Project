// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", function () {
    const searchModal = document.getElementById("searchModal");
    const searchBtn = document.getElementById("searchBtn");
    const modalCloseBtn = searchModal.querySelector(".close");


    // Function to open search modal
    searchBtn.addEventListener("click", function () {
        searchModal.style.display = "block";
    });

    // Function to close search modal
    modalCloseBtn.addEventListener("click", function () {
        searchModal.style.display = "none";
    });

    // Function to close search modal when clicking outside
    window.addEventListener("click", function (event) {
        if (event.target === searchModal) {
            searchModal.style.display = "none";
        }
    });
});
