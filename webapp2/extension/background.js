// background.js

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "getURL") {
    chrome.scripting.executeScript(
      {
        target: { tabId: sender.tab.id },
        function: () => {
          const url = window.location.href;
          chrome.runtime.sendMessage({ action: "receivedURL", url });
        },
      },
      () => {}
    );
  }
});
