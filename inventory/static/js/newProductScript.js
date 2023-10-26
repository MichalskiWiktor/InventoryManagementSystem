function addItemToForm(fieldName) {
    var fieldNameLower = fieldName.toLowerCase();
    var elements = document.getElementById("fields");
    var button = document.getElementById("btn-" + fieldNameLower);

    var xhr = new XMLHttpRequest();
    xhr.open("GET", `/get_field_data/?field_name=${fieldNameLower}`, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                elements.innerHTML += `<div class="col-md-4 mb-4">
                  <label for="${response.name}" style="margin-bottom:0">
                    ${response.label}
                  </label>
                  <button type="button" class="btn-close" aria-label="Close"></button>
                  <input type="${response.type}"class="form-control" id="${response.id}" name="${response.name}" type="text" placeholder="${response.label}">
                </div>`;
                button.hidden = true;
                /// check if all buton are hidden if yes then hide avaible fields 
            }
        }
    };

    xhr.send();
}