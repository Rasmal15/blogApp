document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-cmnt-btn');
    console.log(likeButtons)

    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const id = button.getAttribute('data-likable_comment-id');
            console.log(id)
            // Send AJAX request to like/unlike the post
            fetch(`/profile/like_comment/${id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                // Update the like button UI based on the response
                const iTag = button.querySelector(`#i-${id}`)
                const count = document.getElementById(`comment_like_count-${id}`)
                // Update the like button UI based on the response
                if (data.liked) {
                    // The user liked the post, update the like count
                    iTag.style.color = "red";
                    count.textContent = data.count

                    // button.textContent = 'Liked';
                } else{
                    iTag.style.color = "blue";
                    count.textContent = data.count
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});