let backToTop = document.getElementsByClassName('.btt-link');

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

// Products Stock Filter
function updateStockFilter() {  
        document.querySelectorAll('.stock-check').forEach( checkBox => {
            checkBox.addEventListener('change', () => {
            let currentUrl = new URL(window.location);
            let stock = checkBox.value;

            if (stock == 'no_stock' || stock == 'in_stock') {
                currentUrl.searchParams.delete("no_stock");
                currentUrl.searchParams.delete("in_stock");
                window.location.replace(currentUrl);
            }

            // In Stock
            if(stock != 'no_stock'){
                let inStock = stock;

                currentUrl.searchParams.set("in_stock", inStock);
                window.location.replace(currentUrl);
            }

            // Not in Stock
            if(stock != 'in_stock'){
                let noStock = stock;

                currentUrl.searchParams.set("no_stock", noStock);
                window.location.replace(currentUrl);
            }  
        })
    })
}

function showPriceRange(Val){
    document.getElementById('Range').innerHTML = ` - Max: €${Val}`
}

document.getElementById('btt-link').addEventListener('click', ()=> {
    window.scrollTo(0,0)
}) 

