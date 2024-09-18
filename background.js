
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {

  if (request.action === "openLink") {
    // Open URL in external application here
    console.log(`Opening URL in external application: ${request.url}`);

    chrome.runtime.sendNativeMessage('com.gabeochoa.openinprofile', {
      url: request.url
    },
    (response) => {
        console.log("got response: ", response)
        if(!response || !response.success){
            console.error("Got bad response: ", response)
            return;
        }
    }
    );

  }
});
