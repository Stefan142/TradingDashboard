// Handles toggle of the sidebar.
window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Checks local storage for the saved state of the sidebar toggle
        if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
             document.body.classList.toggle('sb-sidenav-toggled');
        }
        // Adds a click event listener to the sidebar toggle button
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            // Toggles the 'sb-sidenav-toggled' class on the body
            document.body.classList.toggle('sb-sidenav-toggled');
            // Saves the current state of the sidebar toggle in local storage
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

// Makes the element that has this class draggable AND resizable.
interact('.draggable')
    .draggable({
        listeners: {
            // Handles the movement of the draggable element
            move(event) {
                const target = event.target;
                // Calculates new coordinates based on the movement
                const x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx;
                const y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

                // Applies the translation to the element
                target.style.transform = `translate(${x}px, ${y}px)`;

                // Updates the data attributes with the new coordinates
                target.setAttribute('data-x', x);
                target.setAttribute('data-y', y);
            },
        },
    })
    .resizable({
        // Enables resizing from the right and bottom edges
        edges: { right: true, bottom: true },
        listeners: {
            // Handles the resizing of the element
            move(event) {
                const target = event.target;
                const x = parseFloat(target.getAttribute('data-x')) || 0;
                const y = parseFloat(target.getAttribute('data-y')) || 0;
                // Ensures a minimum width and height during resizing
                const newWidth = Math.max(100, event.rect.width); 
                const newHeight = Math.max(100, event.rect.height); 

                // Applies the new dimensions to the element
                target.style.width = `${newWidth}px`;
                target.style.height = `${newHeight}px`;
            },
        },
    });

// Makes resizing for elements with the class resizable possible
interact('.resizable')
    .resizable({
        edges: { right: true, bottom: true },
        listeners: {
            move(event) {
                const target = event.target;
                const x = parseFloat(target.getAttribute('data-x')) || 0;
                const y = parseFloat(target.getAttribute('data-y')) || 0;
                const newWidth = Math.max(100, event.rect.width); 
                const newHeight = Math.max(100, event.rect.height); 

                target.style.width = `${newWidth}px`;
                target.style.height = `${newHeight}px`;
            },
        },
    });

// Function to add a new stock input field
function addStockInput() {
    const stockCount = document.querySelectorAll('.stock-input').length + 1;
    const newInput = document.createElement('div');
    // Creates and appends a new stock input field
    newInput.classList.add('stock-input', 'form-floating', 'mb-3');
    newInput.innerHTML = `
        <input class="form-control" id="stock${stockCount}" type="text" name="stock${stockCount}" placeholder="Enter stock symbol">
        <label for="stock${stockCount}">Stock Symbol ${stockCount}</label>
     `;

    // Appends the new input field to the container
    document.getElementById('stock-input-container').appendChild(newInput);
}

// Function to delete the last stock input field
function deleteLastStockInput() {
    const stockInputs = document.querySelectorAll('.stock-input');
    // Removes the last stock input field if more than one exists
    if (stockInputs.length > 1) {
        const lastInput = stockInputs[stockInputs.length - 1];
        lastInput.parentNode.removeChild(lastInput);
    }
}

// Function to submit the stock form
function submitForm() {
    const stockInputs = document.querySelectorAll('.stock-input input');
    const stockCount = stockInputs.length;

    // Creates a hidden input field for the stock count and appends it to the form
    const stockCountInput = document.createElement('input');
    stockCountInput.type = 'hidden';
    stockCountInput.name = 'stock_count';
    stockCountInput.value = stockCount;
    
    const form = document.getElementById('stock-form');
    // Appends the stock_count input to the form
    form.appendChild(stockCountInput);
    
    // Submits the form
    form.submit();
}

// Function to submit the drawing tool form
function submitForm2() {
    const form = document.getElementById('drawingToolForm');
    // Submits the form with the id drawingToolForm
    form.submit();
}

// Function to display the seconds per bar message
function showSecondsPerBarMessage() {
    document.getElementById("secondsPerBarMessage").style.display = "block";
}

// Function to hide the seconds per bar message
function hideSecondsPerBarMessage() {
    document.getElementById("secondsPerBarMessage").style.display = "none";
}

// Function to toggle the visibility of a description based on its index
function toggleDescription(index) {
    var description = document.getElementById('desc_' + index);
    // Toggles the 'expanded' class to show/hide the description
    description.classList.toggle('expanded');
}