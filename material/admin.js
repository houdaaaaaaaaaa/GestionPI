function selectMaterialType(select) {
    var selectedValue = select.value;
    if (selectedValue === 'hardware') {
        // Show fields for hardware
        document.getElementById('id_nom').parentNode.parentNode.style.display = 'block';
        document.getElementById('id_numero_serie').parentNode.parentNode.style.display = 'block';
        // Show/hide other fields as needed
    } else if (selectedValue === 'software') {
        // Hide fields for software
        document.getElementById('id_nom').parentNode.parentNode.style.display = 'none';
        document.getElementById('id_numero_serie').parentNode.parentNode.style.display = 'none';
        // Show/hide other fields as needed
    }
}
