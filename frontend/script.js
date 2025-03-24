// Event Listener for Disease Selection
document.getElementById("disease").addEventListener("change", async function () {
    const disease = this.value; // Get selected disease
    const formDiv = document.getElementById("features-form");

    clearForm(); // Clear previous input fields
    clearResult(); // Clear previous prediction result

    if (!disease) return; // Exit if no disease is selected

    try {
        // Fetch features for the selected disease
        const features = await fetchFeatures(disease);

        // Dynamically create input fields for each feature
        features.forEach(feature => {
            const { label, input } = createInputField(feature);
            formDiv.appendChild(label);
            formDiv.appendChild(input);
        });
    } catch (error) {
        alert("Error fetching features. Please try again.");
        console.error("Error fetching features:", error);
    }
});

// Event Listener for Diagnose Button
document.getElementById("submit").addEventListener("click", async function () {
    const disease = document.getElementById("disease").value;
    const inputs = document.querySelectorAll("#features-form input");

    // Validate user input
    if (!disease || inputs.length === 0) {
        alert("Please select a disease and fill all fields.");
        return;
    }

    const data = {};

    // Gather user input data
    for (let input of inputs) {
        const value = parseFloat(input.value);
        if (isNaN(value)) {
            alert(`Please provide a valid number for ${input.name}`);
            input.focus();
            return;
        }
        data[input.name] = value;
    }

    try {
        // Submit prediction request to the backend
        const result = await submitPrediction(disease, data);
        displayResult(result.prediction); // Display the prediction result
    } catch (error) {
        alert("Error processing the prediction. Please try again.");
        console.error("Error processing prediction:", error);
    }
});

// Utility Functions

// Fetch features for the selected disease from the backend
async function fetchFeatures(disease) {
    const response = await fetch(`http://127.0.0.1:8000/features/${disease}`);
    if (!response.ok) {
        throw new Error(`Failed to fetch features for disease: ${disease}`);
    }
    return response.json();
}

// Submit user input to the backend and get prediction
async function submitPrediction(disease, data) {
    const response = await fetch(`http://127.0.0.1:8000/predict/${disease}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });
    if (!response.ok) {
        throw new Error("Failed to submit prediction");
    }
    return response.json();
}

// Create input fields dynamically for each feature
function createInputField(name) {
    const label = document.createElement("label");
    label.innerText = name;

    const input = document.createElement("input");
    input.type = "number";
    input.name = name;
    input.placeholder = `Enter ${name}`;

    return { label, input };
}

// Clear the form when a new disease is selected
function clearForm() {
    document.getElementById("features-form").innerHTML = "";
}

// Clear the result section
function clearResult() {
    document.getElementById("result").innerText = "";
}

// Display the prediction result
function displayResult(prediction) {
    document.getElementById("result").innerText = `Prediction: ${prediction}`;
}