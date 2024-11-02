async function fetchContestData() {
    const selector = document.getElementById('platform-selector');
    const selectedValue = selector.value;
    const display = document.getElementById('selected-platform');
    const contestInfo = document.getElementById('contest-info');

    if (selectedValue) {
        display.textContent = `You selected: ${selector.options[selector.selectedIndex].text}`;

        try {
            console.log(selectedValue)
            const response = await fetch(`https://cp-contest-notification.onrender.com/process?choice=${selectedValue}`);
            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();
            contestInfo.textContent = data.output;
        } catch (error) {
            contestInfo.textContent = 'Error fetching contest data: ' + error.message;
        }
    } else {
        display.textContent = '';
        contestInfo.textContent = '';
    }
}
