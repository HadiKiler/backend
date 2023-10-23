let loginForm = document.getElementById("login-form")
let searchForm = document.getElementById("search-form")
const content = document.getElementById("content")
const productsBtn =  document.getElementById("productsBtn")
const basePoint = "http://localhost:8000/api"


searchForm.addEventListener('submit',(e)=>{
  e.preventDefault()
  let searchFormObject = new FormData(searchForm)
  let searchFormData = Object.fromEntries(searchFormObject)
  let searchParams = new URLSearchParams(searchFormData)
  const searchPoint = `${basePoint}/search/?${searchParams}`
  
  const headers = {"Content-Type": "application/json"}
  const authToken = localStorage.getItem('access') 
  if (authToken) {
      headers['Authorization'] = `Bearer ${authToken}`
  }
  let options = {
      method : "GET",
      headers : headers
  }
  fetch(searchPoint, options)
  .then(response=>{
      return response.json()
  })
  .then(data => {
    refreshToken(data)
  })
  .catch(err=> {
     console.log('err', err)
  })
})



function refreshToken(data){
  if (!isTokenValid(data)) {
    const refreshPoint = `${basePoint}/token/refresh/`;
    let refreshOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"refresh": localStorage.getItem('refresh')})
    };

    fetch(refreshPoint, refreshOptions)
      .then(refreshResponse => {
        return refreshResponse.json();
      })
      .then(refreshData => {
        if (isTokenValid(refreshData)) {
          localStorage.setItem("access", refreshData.access);
          alert("refreshing... , please test again.")
        } else {
          alert("Please login.");
        }
      });
  } else {
    content.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
  }
}


loginForm.addEventListener('submit',(e)=>{
    e.preventDefault()
    const loginPoint = `${basePoint}/token/`
    let loginFormObject = new FormData(loginForm)
    let loginFormData = Object.fromEntries(loginFormObject)
    let save = true
    let options = {
        method : "POST",
        headers : {
            "Content-Type": "application/json"
        },
        body : JSON.stringify(loginFormData)
    }
    fetch(loginPoint, options)
    .then(response=>{
        save = (response.status == 200) 
        return response.json()
    })
    .then(data => {
        if (save){
            alert('logined !')
            localStorage.setItem("access", data.access)
            localStorage.setItem("refresh", data.refresh)
        }else{
            content.innerHTML = `<p>${JSON.stringify(data)}</p>`
            localStorage.removeItem("access")
            localStorage.removeItem("refresh")
        }
    })
    .catch(err=> {
       console.log('err', err)
    })
})


productsBtn.addEventListener('click', e=>{
    const productsPoint = `${basePoint}/products/`;
    let options = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${localStorage.getItem("access")}`
      }
    };
    fetch(productsPoint, options)
      .then(response => {
        return response.json();
      })
      .then(data => {
        refreshToken(data)
      })
      .catch(err => {
        console.log('err', err);
      });
})

function isTokenValid(jsonData) {
    if (jsonData.code && jsonData.code === "token_not_valid"){
        return false
    }
    return true
}