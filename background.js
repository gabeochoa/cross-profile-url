chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "openLink") {
    // Open URL in external application here
    console.log(`Opening URL in external application: ${request.url}`);

    chrome.runtime.sendNativeMessage('com.gabeochoa.openinprofile', {
      url: request.url
    },
    (response) => {
        console.log("got response: ", response)
        if(!response.success){
            console.err("Got bad response: ", response)
            return;
        }

        chrome.tabs.query({ active: false, lastFocusedWindow: true }, function(tabs) {
          if (tabs.length > 0) {
                console.log("tabs: ", tabs)
                // setTimeout(function() {
                    // chrome.tabs.remove(tabs[tabs.length - 1].id);
                // }, 100);
          }
        });
        
    }
    );

  }
});
