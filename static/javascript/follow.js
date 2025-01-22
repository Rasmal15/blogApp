document.addEventListener('DOMContentLoaded', function(){
    console.log('hello')
    const followButtons = document.querySelectorAll('.follow');
    followButtons.forEach(button => {
        button.addEventListener('click', function(event){
            event.preventDefault()
            const id = button.getAttribute('data-follow-user')
            fetch(`/profile/follow/${id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            }).then(response => response.json())
            .then(data => {
                console.log(data)
                if(data.status == 'follow'){
                    button.textContent = 'follwing'
                } else {
                    button.textContent = 'follow'
                }
            })
        })
    })
})