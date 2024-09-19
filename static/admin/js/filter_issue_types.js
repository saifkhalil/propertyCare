document.addEventListener("DOMContentLoaded", function () {
    const equipmentSelect = document.getElementById("id_equipment");
    const issueTypeSelect = document.getElementById("id_issue_type");

    if (equipmentSelect) {
        equipmentSelect.addEventListener("change", function () {
            const equipmentId = this.value;
            const issueTypeUrl = window.location.origin + "/api/propertyCare/filter_issue_types/?equipment_id=" + equipmentId;

            // Fetch issue types based on the selected equipment
            fetch(issueTypeUrl)
                .then(response => response.json())
                .then(data => {
                    // Clear existing options
                    issueTypeSelect.innerHTML = "";

                    // Add new options
                    data.issue_types.forEach(function (issueType) {
                        const option = document.createElement("option");
                        option.value = issueType.id;
                        option.textContent = issueType.type;
                        issueTypeSelect.appendChild(option);
                    });
                });
        });
    }
});
