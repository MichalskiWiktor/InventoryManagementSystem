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
        var selectedCategory = $(this).val().toLowerCase();
        $("table tbody tr").each(function () {
            var category = $(this).find("td:nth-child(4)").text().toLowerCase();
            if (selectedCategory[1] === '' || selectedCategory === 'all' || category === selectedCategory) {
                $(this).show();
            }else{
                $(this).hide();
            }
        });
    $("#sortBy").on("change", function () {
        var selectedSortBy = $(this).val().toLowerCase();
        $("table tbody tr").each(function () {
            var price = $(this).find("td:nth-child(5)").text().toLowerCase();
            if (selectedCategory[1] === '' || selectedCategory === 'all' || category === selectedSortBy) {
                $(this).show();
            }else{
                $(this).hide();
            }
        });
    });
    });
});