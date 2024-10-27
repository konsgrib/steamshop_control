document.addEventListener('DOMContentLoaded', async () => {
    const reportDiv = document.getElementById('report');

    try {
        // const sensorsResponse = await fetch('/api/sensors');
        // const sensorsData = await sensorsResponse.json();

        const statusResponse = await fetch('/api/status');
        const statusData = await statusResponse.json();

        reportDiv.innerHTML = `
            <h2>Status</h2>
            <pre>${JSON.stringify(statusData, null, 2)}</pre>
        `;
    } catch (error) {
        reportDiv.innerHTML = `<p>Error fetching data: ${error}</p>`;
    }
});