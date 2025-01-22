document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-btn');
    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const id = button.getAttribute('data-likable_post-id');

            // Send AJAX request to like/unlike the post
            fetch(`/profile/like_post/${id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                const iTag = button.querySelector(`#i-${id}`)
                const count = document.getElementById(`like_count-${id}`)
                // Update the like button UI based on the response
                if (data.liked) {
                    // The user liked the post, update the like count
                    iTag.style.color = "red";
                    count.textContent = data.like_count

                    // button.textContent = 'Liked';
                } else{
                    iTag.style.color = "blue";
                    count.textContent = data.like_count
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
},{once : true});