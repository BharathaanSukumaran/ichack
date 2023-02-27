clientData = [];




function log_client(new_client,new_password){
    clientData.push({
        name: new_client,
        Password: new_password
    })

}

function client_login(username_input,password_input,db){
    var p = false;  
     for(let i=0; i<db.length;i++)
       if(username_input == db[i].name && password_input == db[i].Password){
         p = true;
       }
     return p
   }

document.getElementById("admin-login").addEventListener("submit",function(e){
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    if(!(client_login(username,password,AdminData))){
    e.preventDefault()
    alert("Invalid username or password")
    }
})

var new_client = document.getElementById()

document.getElementById("admin-registration").addEventListener("submit",log_client())
