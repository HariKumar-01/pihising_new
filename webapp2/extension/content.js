// content.js
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === 'checkURL') {
    const url = message.url;
    
    // Send the URL to your Flask server for checking
    fetch('http://localhost:5005/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url }),
    })
    .then((response) => response.json())
    .then((data) => {
      sendResponse({ message: data.result });
    })
    .catch((error) => {
      console.error('Error:', error);
      sendResponse({ message: 'An error occurred.' });
    });

    return true; // Indicates that sendResponse will be called asynchronously
  }
});
