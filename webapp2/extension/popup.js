document.addEventListener('DOMContentLoaded', function () {
  const urlInput = document.getElementById('urlInput');
  const checkButton = document.getElementById('checkButton');
  const result = document.getElementById('result');

  checkButton.addEventListener('click', function () {
    const url = urlInput.value;

    fetch('http://127.0.0.1:5005/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url }),
    })
    .then((response) => response.json())
    .then((data) => {
      result.textContent = `URL: ${data.url}, Prediction: ${data.prediction}`;
    })
    .catch((error) => {
      console.error('Error:', error);
      result.textContent = 'An error occurred.';
    });
  });
});
