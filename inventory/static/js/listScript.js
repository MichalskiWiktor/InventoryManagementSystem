$(document).ready(function () {
    $("#myInput").on("input", function () {
        var value = $(this).val().toLowerCase();
        $("table tbody tr").each(function () {
            var rowText = $(this).text().toLowerCase();
            if (rowText.includes(value)) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
    $("#filterCategory").on("change", function () {
        alert("ok")
        var selectedCategory = $(this).val().toLowerCase();
        $("table tbody tr").each(function () {
            var category = $(this).find("td:nth-child(4)").text().toLowerCase();
            if (selectedCategory[1] === '' || selectedCategory === 'all' || category === selectedCategory) {
                $(this).show();
            }else{
                $(this).hide();
            }
        });
    });
    $("#sortBy").on("change", function () {
        var selectedSortBy = $(this).val().toLowerCase();
        var rows = Array.from(document.querySelectorAll(".productRow"));
        var rowsExpanded = Array.from(document.querySelectorAll(".productRowExpanded"));
        function sortBy(data, order){
            function sortRow(a,b){
                const dataA = parseFloat(a.getAttribute(data));
                const dataB = parseFloat(b.getAttribute(data));
                if(order)return dataB - dataA;
                else return dataA - dataB;
            }
            rows.sort(sortRow);
            rowsExpanded.sort(sortRow);
        }
        if (selectedSortBy === "price_desc") {
            sortBy("data-price", true)
        } else if (selectedSortBy === "price_asc") {
            sortBy("data-price", false)
        } else if (selectedSortBy === "stock_desc") {
            sortBy("data-stock", true)
        } else if (selectedSortBy === "stock_asc") {
            sortBy("data-stock", false)
        } else if (selectedSortBy === "oldest") {
            sortBy("data-id", true)
        } else if (selectedSortBy === "default") {
            sortBy("data-id", false)
        }
        var tableBody = $("table tbody");
        tableBody.empty();
        rows.forEach(function (row) {
            tableBody.append(row);
            tableBody.append(rowsExpanded);
        });
        rows.forEach((row, index) => {
            tableBody.append(row);
            tableBody.append(rowsExpanded[index]);
          });
    });
});