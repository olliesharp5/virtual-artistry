document.addEventListener('DOMContentLoaded', (event) => {
  let elem = document.querySelector('.masonry');
  if (elem) {
    let msnry = new Masonry(elem, {
        itemSelector: '.col',
        columnWidth: '.col',
    });
    return msnry;
  }
});