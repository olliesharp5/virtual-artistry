document.addEventListener('DOMContentLoaded', (event) => {
    var elem = document.querySelector('.masonry');
    new Masonry(elem, {
      itemSelector: '.col',
      columnWidth: '.col',
    });
  });