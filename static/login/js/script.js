// const rangeInput = document.querySelectorAll(".range-input input"),
// priceInput = document.querySelectorAll(".price-input input"),
// range = document.querySelector(".slider .progress");
// let priceGap = 1000;
// priceInput.forEach(input =>{
//     input.addEventListener("input", e =>{
//         let minPrice = parseInt(priceInput[0].value),
//         maxPrice = parseInt(priceInput[1].value);
        
//         if((maxPrice - minPrice >= priceGap) && maxPrice <= rangeInput[1].max){
//             if(e.target.className === "input-min"){
//                 rangeInput[0].value = minPrice;
//                 range.style.left = ((minPrice / rangeInput[0].max) * 100) + "%";
//             }else{
//                 rangeInput[1].value = maxPrice;
//                 range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
//             }
//         }
//     });
// });
// rangeInput.forEach(input =>{
//     input.addEventListener("input", e =>{
//         let minVal = parseInt(rangeInput[0].value),
//         maxVal = parseInt(rangeInput[1].value);
//         if((maxVal - minVal) < priceGap){
//             if(e.target.className === "range-min"){
//                 rangeInput[0].value = maxVal - priceGap
//             }else{
//                 rangeInput[1].value = minVal + priceGap;
//             }
//         }else{
//             priceInput[0].value = minVal;
//             priceInput[1].value = maxVal;
//             range.style.left = ((minVal / rangeInput[0].max) * 100) + "%";
//             range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
//         }
//     });
// });

const minPriceInput = document.getElementById("min-price");
const maxPriceInput = document.getElementById("max-price");
const minPriceValue = document.getElementById("id_min_price");
const maxPriceValue = document.getElementById("id_max_price");

minPriceInput.addEventListener("input", updateMinPrice);
maxPriceInput.addEventListener("input", updateMaxPrice);

function updateMinPrice() {
  minPriceValue.value = minPriceInput.value;
  if (parseInt(minPriceInput.value) > parseInt(maxPriceInput.value)) {
    maxPriceInput.value = minPriceInput.value;
    maxPriceValue.value = minPriceInput.value;
  }
}

function updateMaxPrice() {
  maxPriceValue.value = maxPriceInput.value;
  if (parseInt(maxPriceInput.value) < parseInt(minPriceInput.value)) {
    minPriceInput.value = maxPriceInput.value;
    minPriceValue.value = maxPriceInput.value;
  }
}