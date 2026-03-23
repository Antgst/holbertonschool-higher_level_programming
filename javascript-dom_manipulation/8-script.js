document.addEventListener('DOMContentLoaded', function () {
  const hello = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      hello.textContent = data.hello;
    });
});
