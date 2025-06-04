document.addEventListener('DOMContentLoaded', function(){
    const deletePostButtons = document.querySelectorAll('.delete-post-btn');
    const radioButtons = document.querySelectorAll('.delete-post');
    const closeButtons = document.querySelectorAll('.close-btn');

    deletePostButtons.forEach(button => {
        button.addEventListener('click', function(){
            const id = button.getAttribute('data-delete-post-id');
            const postOverlay = document.getElementById(`overlay-${id}`);
            const popDialog = document.getElementById(`popupDialog-${id}`);
            postOverlay.classList.toggle('hidden');
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
            const postId = button.getAttribute('data-post-id');
            const deleted_post = button.value;
            const postDiv = document.getElementById(`post-${postId}`)
            const popupContainer = button.closest('.popupContainer'); // Find the closest popup container
            const overlay = popupContainer.querySelector('.overlay');
            const popDialog = popupContainer.querySelector('.popupDialog');
            if (button.checked) {
                if (deleted_post) {
                    fetch(`/profile/delete_post/${postId}`,{
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // CSRF token
                        },
                        body: JSON.stringify({
                            deleted_post: deleted_post  // Send the form data as JSON
                        })
                    }).then(response => response.json())
                    .then(data => {
                        if (data.status == 'success'){
                            postDiv.parentNode.removeChild(postDiv)
                            overlay.classList.add("hidden");
                            popDialog.classList.add("hidden");

                            // Optionally, reset opacity (if you're using opacity transitions)
                            popDialog.style.opacity = "0";
                        } else {
                            overlay.classList.add("hidden");
                            popDialog.classList.add("hidden");

                            // Optionally, reset opacity (if you're using opacity transitions)
                            popDialog.style.opacity = "0";
                        }
                    })
                }
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
})