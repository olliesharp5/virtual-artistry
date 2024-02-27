const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.querySelector(".reviewform");
const submitButton = document.getElementById("submitButton");

// Get the modal
const modal = new bootstrap.Modal(document.getElementById('myModal'));

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        console.log("Button clicked"); // Add this line
        let reviewId = e.target.getAttribute("data-review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        console.log("Review ID:", reviewId); // Add this line
        console.log("Review content:", reviewContent); // Add this line
        reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
        console.log("Form action:", reviewForm.getAttribute("action")); // Add this line

        // Show the modal
        modal.show();
    });
}