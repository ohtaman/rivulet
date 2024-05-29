async function fetchComponents() {
    const response = await fetch('/components');
    const virtualDOM = await response.json();
    renderComponents(virtualDOM);
}

function renderComponents(virtualDOM) {
    const app = document.getElementById('app');
    app.innerHTML = ''; // Clear existing content

    virtualDOM.forEach(component => {
        const componentDiv = document.createElement('div');
        componentDiv.id = component.id;

        // Render states within the component
        for (const [stateName, stateValue] of Object.entries(component.states)) {
            const stateDiv = document.createElement('div');
            stateDiv.className = 'state';
            stateDiv.innerText = `${stateName}: ${JSON.stringify(stateValue)}`;

            const updateButton = document.createElement('button');
            updateButton.innerText = `Update ${stateName}`;
            updateButton.onclick = () => {
                const newValue = prompt(`Enter new value for ${stateName}:`, JSON.stringify(stateValue));
                if (newValue !== null) {
                    updateState(component.id, stateName, JSON.parse(newValue));
                }
            };

            stateDiv.appendChild(updateButton);
            componentDiv.appendChild(stateDiv);
        }

        app.appendChild(componentDiv);
    });
}

async function updateState(componentId, stateName, newState) {
    const response = await fetch(`/components/${componentId}/states/${stateName}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newState)
    });

    const updatedVirtualDOM = await response.json();
    renderComponents(updatedVirtualDOM);
}
