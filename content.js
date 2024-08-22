document.addEventListener("click", function(event) {

    chrome.runtime.sendMessage({type: "getUser"}, function(response) {
      console.log(JSON.stringify(response));
    });

    let target = event.target;
    while (target && target.tagName !== "A") {
        target = target.parentNode;
    }

    if(target == null){
        return;
    }

    if (event.metaKey && target.tagName === "A") { // Cmd key pressed and link clicked
        // console.log("Sending open link message for");
        chrome.runtime.sendMessage({ action: "openLink", url: target.href });
        event.preventDefault();
    }
});
