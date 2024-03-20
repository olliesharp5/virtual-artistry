document.addEventListener('DOMContentLoaded', (event) => {
  let elem = document.querySelector('.masonry');
  let msnry = new Masonry(elem, {
      itemSelector: '.col',
      columnWidth: '.col',
  });
  return msnry;
});