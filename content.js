document.addEventListener("click", function(event) {
    let target = event.target;
    while (target && target.tagName !== "A") {
        target = target.parentNode;
    }

    if(target == null){
        return;
    }

    console.log("event click, ", event);
    console.log("event meta key? , ", event.metaKey);
    console.log("event target tagname? , ", target.href);

    if (event.metaKey && target.tagName === "A") { // Cmd key pressed and link clicked
        console.log("sending open link message");
        chrome.runtime.sendMessage({ action: "openLink", url: target.href });
    }
});
