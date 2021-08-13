// Sort Selector filter on change
function updateFilter() {  
    document.querySelectorAll('.form-check-input').forEach( checkBox => {

        checkBox.addEventListener('change', function() {
            let currentUrl = new URL(window.location);
            let selectedVal = this.value;
            
            if(selectedVal != "" || undefined || null){
                let sort = selectedVal.split("_")[0];
                let direction = selectedVal.split("_")[1];

                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);
                window.location.replace(currentUrl);     
            }
            else {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");
                window.location.replace(currentUrl);
            }
        })
    })
}

function updateStockFilter() {  
        document.querySelectorAll('.stock-check').forEach( checkBox => {
            checkBox.addEventListener('change', () => {
            let currentUrl = new URL(window.location);
            let selectedVal = checkBox.value;

            // In Stock
            if(selectedVal != "no_stock"){
                let stock = selectedVal.split("_")[0];

                currentUrl.searchParams.set("in_stock", stock);
                window.location.replace(currentUrl);
            }
            else {
                currentUrl.searchParams.delete("in_stock");
                window.location.replace(currentUrl);
            }
            // Not in Stock
            if(selectedVal != "in_stock"){
                let stock = selectedVal.split("_")[0];

                currentUrl.searchParams.set("no_stock", stock);
                window.location.replace(currentUrl);
            }
            else {
                currentUrl.searchParams.delete("no_stock");
                window.location.replace(currentUrl);
            }
        })
    })
}

function showPriceRange(Val){
    document.getElementById('Range').innerHTML = ` - Max: €${Val}`
}

