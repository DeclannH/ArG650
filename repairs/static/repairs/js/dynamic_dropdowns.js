document.addEventListener('DOMContentLoaded', function() {
    const yearSelect = document.getElementById('year');
    const makeSelect = document.getElementById('make');
    const modelSelect = document.getElementById('model');
    const trimSelect = document.getElementById('trim');
    const repairTypeSelect = document.getElementById('repair_type');
    const repairSelect = document.getElementById('repair');

    yearSelect.addEventListener('change', function() {
        updateDropdown('year', yearSelect.value, makeSelect);
    });

    makeSelect.addEventListener('change', function() {
        updateDropdown('make', makeSelect.value, modelSelect);
    });

    modelSelect.addEventListener('change', function() {
        updateDropdown('model', modelSelect.value, trimSelect);
    });

    repairTypeSelect.addEventListener('change', function() {
        updateDropdown('repair_type', repairTypeSelect.value, repairSelect);
    });

    function updateDropdown(type, value, nextDropdown) {
        if (value) {
            fetch('/repairs/get-dropdown-data/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ [type]: value })
            })
            .then(response => response.json())
            .then(data => {
                nextDropdown.innerHTML = `<option value="">Select ${nextDropdown.name.charAt(0).toUpperCase() + nextDropdown.name.slice(1)}</option>`;
                for (const item of data[nextDropdown.name] || []) {
                    const option = document.createElement('option');
                    option.value = item;
                    option.textContent = item;
                    nextDropdown.appendChild(option);
                }
                nextDropdown.disabled = false;
            });
        } else {
            nextDropdown.innerHTML = `<option value="">Select ${nextDropdown.name.charAt(0).toUpperCase() + nextDropdown.name.slice(1)}</option>`;
            nextDropdown.disabled = true;
        }
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
