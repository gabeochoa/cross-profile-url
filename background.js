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
            console.error("Got bad response: ", response)
            return;
        }

        // chrome.tabs.query({ active: false, lastFocusedWindow: true }, function(tabs) {
          // if (tabs.length > 0) {
            // console.log("tabs: ", tabs)
            // const newestInactiveTab = tabs.reduce((newest, current) => {
              // return current.lastAccessed > newest.lastAccessed ? current : newest;
            // }, tabs[0]);
            // console.log("Newest inactive tab: ", newestInactiveTab);
            // // You can now use newestInactiveTab.id to remove the tab, for example:
            // // chrome.tabs.remove(newestInactiveTab.id);
          // }
        // });
    }
    );

  }
});
