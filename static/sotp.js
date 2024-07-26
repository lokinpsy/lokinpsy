
document.addEventListener('DOMContentLoaded', function() {
    const subForm = document.getElementById('subForm');
    const messageDiv = document.getElementById('otpmsg');
    const otpform = document.getElementById('otp-form');
    var subcon = document.getElementById('sub-container');
    const loader = document.getElementById('loader');

    subForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(subForm);
        messageDiv.textContent = 'Sending OTP';
        loader.hidden = false;
        subcon.style.backgroundColor = 'rgb(9, 64, 91)' ;

        fetch("/sotp", {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
          if (data.message == "OTP sent successfully") {
                subForm.hidden = true;
                otpform.hidden = false;
                loader.hidden = true;
                messageDiv.hidden = true;
          } else {
            messageDiv.textContent = data.message;
            subcon.style.backgroundColor = '#FF6961';
            loader.hidden = true;
          }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
    });
});