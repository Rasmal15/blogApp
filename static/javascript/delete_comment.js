document.addEventListener('DOMContentLoaded',function(){
    const deleteButtons = document.querySelectorAll('.delete-cmnt-btn');
    const closeButtons = document.querySelectorAll('.close-btn');
    const radioButtons = document.querySelectorAll('.delete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(){
            const id = button.getAttribute('data-delete-comment-id');
            const overlay = document.getElementById(`overlay-${id}`);
            const popDialog = document.getElementById(`popupDialog-${id}`);
            overlay.classList.toggle("hidden");
            popDialog.classList.toggle("hidden");

            // Optionally, toggle opacity for smooth transition if not handled by CSS
            if (popDialog.style.opacity === "1") {
                popDialog.style.opacity = "0";
            } else {
                popDialog.style.opacity = "1";
            }
        })
    });

    closeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const popupContainer = button.closest('.popupContainer'); // Find the closest popup container
            const overlay = popupContainer.querySelector('.overlay');
            const popDialog = popupContainer.querySelector('.popupDialog');

            // Hide the overlay and popup dialog
            overlay.classList.add("hidden");
            popDialog.classList.add("hidden");

            // Optionally, reset opacity (if you're using opacity transitions)
            popDialog.style.opacity = "0";
        });
    });

    radioButtons.forEach(button => {
        button.addEventListener('change', function () {
            const id = button.getAttribute('data-comment-id');
            const comment_div = document.getElementById(`comment-${id}`);
            const popupContainer = button.closest('.popupContainer'); // Find the closest popup container
            const overlay = popupContainer.querySelector('.overlay');
            const popDialog = popupContainer.querySelector('.popupDialog');
            let deleted_comment = button.value
            if (button.checked) {
                if (button.value == 'True'){
                    fetch(`/profile/delete_comment/${id}`,{
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // CSRF token
                        },
                        body: JSON.stringify({
                            deleted_comment: deleted_comment  // Send the form data as JSON
                        })
                    })
                    .then(respone => respone.json())
                    .then(data => {
                        const postId = data.comment.post;
                        comment_div.parentNode.removeChild(comment_div);
                        comment_count = document.getElementById(`comment_count-${postId}`)
                        comment_count.textContent = data.comment.count
                        overlay.classList.add("hidden");
                        popDialog.classList.add("hidden");

                        // Optionally, reset opacity (if you're using opacity transitions)
                        popDialog.style.opacity = "0";
                    })
                    .catch(error=>{
                        console.log('Error:', error)
                    })
                }else{
                    fetch(`/profile/delete_comment/${id}`,{
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // CSRF token
                        },
                        body: JSON.stringify({
                            deleted_comment: deleted_comment  // Send the form data as JSON
                        })
                    })
                    .then(respone => respone.json())
                    .then(data => {
                        overlay.classList.add("hidden");
                        popDialog.classList.add("hidden");

                        // Optionally, reset opacity (if you're using opacity transitions)
                        popDialog.style.opacity = "0";
                    })
                    .catch(error=>{
                        console.log('Error:', error)
                    })
                }
            }
        });
    });
})
