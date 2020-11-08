const emailField = document.querySelector("#email");
const namefield = document.querySelector("#name");
const messegefield = document.querySelector("#messege");
const sendbtn = document.querySelector("#send")

function apifetch() {
    let email = emailField.value;
    let messege = messegefield.value;
    let name = namefield.value;
    let data = { email, name, messege }
    let contstraints = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(data)
    }  
   
fetch("http://127.0.0.1:8000/api/contact/", contstraints)
.then(response => response.text())
.then(result => console.log(result))
.catch(error => console.log('error', error));
} 
    
   
