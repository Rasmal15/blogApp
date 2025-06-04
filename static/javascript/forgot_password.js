document.addEventListener('DOMContentLoaded',function(){
    const userForm = document.getElementById('user-form');
    const userDiv = document.getElementById('user-div');
    const passwordForm = document.getElementById('password-form');
    const passwordDiv = document.getElementById('password-div');

    userForm.addEventListener('submit',function(event){
        event.preventDefault();
        const username = userForm.querySelector('input[name = "username"]').value;
        console.log(username);
        fetch(`/users/forgot_password/`,{
            method : 'POST',
            headers : {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value, // CSRF token
            },
            body : JSON.stringify({
                'username' : username
            })
        }).then(respone => respone.json())
        .then(data => {
            console.log(data,'hrdjg')
            if (data.user) {
                userDiv.classList.add('d-none');
                passwordDiv.classList.remove('d-none')
            }
        })
    })
})