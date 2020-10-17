function queryClick(id) {
  let queryOne = document.getElementById(id);
  let plusCheck = queryOne.classList.contains("fa-plus-square");
  let minusCheck = queryOne.classList.contains("fa-minus-square");

  if (plusCheck) {
    queryOne.classList.remove("fa-plus-square");
    queryOne.classList.add("fa-minus-square");
  } else if (minusCheck) {
    queryOne.classList.remove("fa-minus-square");
    queryOne.classList.add("fa-plus-square");
  }
}