// infrastructure for when move to Vue
// var app = new Vue({
//   // connects to html div of id 'app'
//   el: '#app',
//   data: {
//       product: ""
//   }
// })

function showModal() {
  document.getElementById('loginModal').style.display="block";
}

// Get the modal
var modal = document.getElementById('loginModal');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}