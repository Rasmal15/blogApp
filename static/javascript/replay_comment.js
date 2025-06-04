document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.replay-comment');
    console.log('fo',forms)

    forms.forEach(form => {
        form.addEventListener ('submit', function(event) {
            console.log('hello')
            event.preventDefault();  // Prevents the form from submitting and refreshing the page
            const id = form.getAttribute('data-likable_comment-id');
            console.log(id)
             // Get the form data (replay_comment value)
             let replayComment = form.querySelector('input[name="replay_comment"]').value;

            // You can send the form data using AJAX or fetch (for example)
            fetch(`/profile/replay_comment/${id}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // CSRF token
                },
                body: JSON.stringify({
                    replay_comment: replayComment  // Send the form data as JSON
                })
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response (e.g., show a success message)
                console.log('Form submitted successfully:', data);  
                if (data.status === 'success') {
                    
                    const comment_id = data.replay.comment
                    // Append the new review to the list
                    const replaylist = document.querySelector(`.replay_lists-${comment_id}`);
                    const newReplay = document.createElement('div');
                    newReplay.classList.add(`.replay-list-${data.replay.id}`);
                    newReplay.innerHTML = `
                    <div class="p-4 rounded-2 bg-light ms-7">
                        <div class="d-flex align-items-center gap-3">
                            <img src="${data.replay.user}" alt="" class="rounded-circle" width="40" height="40">
                            <h6 class="fw-semibold mb-0 fs-4">${data.replay.username }</h6>
                        <span class="fs-2"><span class="p-1 bg-muted rounded-circle d-inline-block"></span> just now</span>
                        </div>
                        <p class="my-3">
                        ${data.replay.replay}
                        </p>
                    </div>
                    `;
                    console.log(replaylist,comment_id)
                    replaylist.appendChild(newReplay);
    
                    // Clear the input field
                    form.querySelector('input[name="replay_comment"]').value = '';
                } else {
                    alert('Failed to add replay. Please try again later.');
                }
            })
            .catch(error => {
                // Handle any error that occurred
                console.log('Error:', error);
            });

    })
})
});
