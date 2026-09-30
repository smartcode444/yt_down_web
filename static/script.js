const fetchButton = document.querySelector(".fetch_button")
const urlInput = document.getElementById('url')
const responseText = document.getElementById('response-text');
const thumbnailImage = document.getElementById('thumbnail');

fetchButton.addEventListener("click", async () => {
    const url = urlInput.value.trim();

    if (!url) {
        responseText.textContent = "Please enter a URL."
        thumbnailImage.style.display = 'none';
        thumbnailImage.src = '';
        return;
    }

    responseText.textContent = "Loading...";
    thumbnailImage.style.display = 'none';
    thumbnailImage.src = '';

    try {
        const response = await fetch(`fetch?url=${encodeURIComponent(url)}`);
        const data = await response.json();

        if (!response.ok) {
            responseText.textContent = data.error || "Something went wrong. Please try again.";
            return;
        }

        responseText.textContent = `Video Title: ${data.title} | Video Duration: 20min`;

        if (data.thumbnail) {
            thumbnailImage.src = data.thumbnail;
            thumbnailImage.alt = data.title ? `${data.title} thumbnail` : 'Video thumbnail';
            thumbnailImage.style.display = 'block';
        } else {
            thumbnailImage.style.display = 'none';
            thumbnailImage.src = '';
        }
    } catch (error) {
        responseText.textContent = "Network error. Please check your connection and try again.";
        thumbnailImage.style.display = 'none';
        thumbnailImage.src = '';
    }
});