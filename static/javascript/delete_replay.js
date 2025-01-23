document.addEventListener('DOMContentLoaded', function(){
    const deleteReplayButtons = document.querySelectorAll('.delete-replay-button');
    const radioButtons = document.querySelectorAll('.delete-replay');
    console.log(radioButtons)
    deleteReplayButtons.forEach(button =>{
        button.addEventListener('click', function(){
            const id = button.getAttribute('data-delete-replay-id');
            console.log(id)
            const replayOverlay = document.getElementById(`overlay-${id}`);
            const popDialog = document.getElementById(`popupDialog-${id}`);
            replayOverlay.classList.toggle('hidden');
            popDialog.classList.toggle('hidden');
            if (popDialog.style.opacity === '1'){
                popDialog.style.opacity = '0'
            } else {
                popDialog.style.opacity = '1'
            }  
        })
    });

    radioButtons.forEach(button => {
        button.addEventListener('change', function(){
            const id = button.getAttribute('data-replay-id')
            const delete_replay = button.value
            const replay_div = document.querySelector(`.replay-list-${id}`)
            const replayOverlay = document.getElementById(`overlay-${id}`);
            const popDialog = document.getElementById(`popupDialog-${id}`);
            console.log(replay_div)
            console.log(delete_replay)
            fetch(`/profile/delete_replay/${id}`, {
                method : 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // CSRF token
                },
                body : JSON.stringify({
                    delete_replay : delete_replay
                })
            }).then(response => response.json())
            .then(data => {
                if (data.status == true){
                    replay_div.parentNode.removeChild(replay_div)
                    replayOverlay.classList.add('.hidden')
                    popDialog.classList.add('.hidden')
                    popDialog.style.opacity = 0;
                    console.log(data)
                } else {
                    replayOverlay.classList.add('.hidden')
                    popDialog.classList.add('.hidden')
                    popDialog.style.opacity = 0;
                }
            }).catch(error => {
                console.log('ERROR:' , error)
            })
        })
    })
})