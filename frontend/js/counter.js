const getCount = () => {
  fetch("https://pdsresumecounter.azurewebsites.net/api/counter")
  .then(response => response.text())
  .then(response => document.getElementById('counter').innerText = response)
}
getCount();