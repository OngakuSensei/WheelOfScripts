// Simulated function to fetch script data based on script ID
function fetchScriptData(scriptID) {
    // Replace this with actual logic to fetch data from the server or database
    return {
        name: "Example Script",
        author: "John Doe",
        description: "This is a description of the example script.",
        alsoKnownAs: [
            { id: 2, name: "Script Alias 1", author: "Jane Doe" },
            { id: 3, name: "Script Alias 2", author: "Alex Smith" }
        ],
        fabled: ["Gardener"],
        travelers: ["Barista", "Judge"]
    };
}

// Function to set the dynamic page title
function setDynamicPageTitle(scriptTitle, scriptAuthor) {
    document.title = `Wheel of Scripts - ${scriptTitle} by ${scriptAuthor}`;
}

// Function to load and display the script data
function loadScript(scriptID) {
    const scriptData = fetchScriptData(scriptID);

    document.getElementById("script-name").innerText = scriptData.name;
    document.getElementById("script-author").innerText = "by " + scriptData.author;

    // Set dynamic page title
    setDynamicPageTitle(scriptData.name, scriptData.author);

    // Display description if available
    if (scriptData.description) {
        document.getElementById("script-description").innerText = scriptData.description;
        document.getElementById("description-section").classList.remove("hidden");
    }

    // Display "Also Known As" section if available
    if (scriptData.alsoKnownAs && scriptData.alsoKnownAs.length > 0) {
        const list = document.getElementById("also-known-as-list");
        scriptData.alsoKnownAs.forEach((alias) => {
            const link = document.createElement("a");
            link.href = `scriptDisplay.html?id=${alias.id}`;
            link.innerText = `${alias.name} by ${alias.author}`;
            list.appendChild(link);
            list.appendChild(document.createElement("br"));
        });
        document.getElementById("also-known-as-section").classList.remove("hidden");
    }

    // Populate Fabled and Travelers sections
    populateList("fabled-container", scriptData.fabled);
    populateList("travelers-container", scriptData.travelers);

    // Handle JSON download
    document.getElementById("download-json").addEventListener("click", () => downloadJson(scriptData));
}

// Function to populate a list container with items
function populateList(containerId, items) {
    const container = document.getElementById(containerId);
    container.innerHTML = "";
    items.forEach((item) => {
        const bubble = document.createElement("div");
        bubble.className = "bubble";
        bubble.innerText = item;
        container.appendChild(bubble);
    });
}

// Function to download the script data as a JSON file
function downloadJson(scriptData) {
    const data = {
        name: scriptData.name,
        author: scriptData.author,
        description: scriptData.description,
        fabled: scriptData.fabled,
        travelers: scriptData.travelers
    };
    const jsonString = JSON.stringify(data, null, 2);
    const blob = new Blob([jsonString], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${scriptData.name.replace(/\s+/g, "_")}.json`;
    a.click();
    URL.revokeObjectURL(url);
}

// Load script with a placeholder ID (replace with actual ID from URL)
loadScript(1);
// JavaScript Document