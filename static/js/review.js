const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.querySelector(".reviewform");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Get the modal
const modal = new bootstrap.Modal(document.getElementById('myModal'));

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        console.log("Button clicked"); // console.log debug
        let reviewId = e.target.getAttribute("data-review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        console.log("Review ID:", reviewId); // console.log debug
        console.log("Review content:", reviewContent); // console.log debug
        reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}/`);
        console.log("Form action:", reviewForm.getAttribute("action")); // console.log debug

        // Show the modal
        modal.show();
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("data-review_id");
      deleteConfirm.href = `delete_review/${reviewId}/`;
      console.log(reviewId);  // console.log debug
      deleteModal.show();
    });
  }