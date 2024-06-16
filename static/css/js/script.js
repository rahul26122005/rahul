document.addEventListener('DOMContentLoaded', function() {
    console.log('Script loaded.');

    var button = document.getElementById('myButton');
    button.addEventListener('click', function() {
        alert('Button clicked!');
    });
});
