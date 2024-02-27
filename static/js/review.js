document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.querySelectorAll('.edit-button');

    editButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const reviewId = this.dataset.reviewId;
            const slug = this.dataset.slug;
            const url = `/review/edit/${slug}/${reviewId}/`;
            window.location.href = url;
        });
    });
});