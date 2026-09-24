const fetchButton = document.querySelector(".fetch_button")
const urlInput = document.getElementById('url')
const responseText = document.getElementById('response-text');

fetchButton.addEventListener("click", async () => {
    const url = urlInput.value.trim();

    if (!url) {
        responseText.textContent = "Please enter a URL."
        return;
    }

    responseText.textContent = "Loading...";

    try {
        const response = await fetch(`fetch?url=${encodeURIComponent(url)}`);
        const data = await response.json();

        if (!response.ok) {
            responseText.textContent = data.error || "Something went wrong. Please try again.";
            return;
        }

        responseText.textContent = `Video Title: ${data.title} | Video Duration: 20min`;
    } catch (error) {
        responseText.textContent = "Network error. Please check your connection and try again.";
    }
});