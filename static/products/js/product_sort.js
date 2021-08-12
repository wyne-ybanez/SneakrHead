// Sort Selector filter on change
function updateFilter() {  
    let checkBoxes = document.querySelectorAll('.form-check-input').forEach( checkBox => {

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

function showPriceRange(Val){
    document.getElementById('Range').innerHTML = ` - Max: €${Val}`
}