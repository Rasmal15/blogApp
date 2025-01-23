document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.comment-form')
    
    forms.forEach(form => {
        form.addEventListener('submit',function(event) {
            event.preventDefault();
            const comment = form.querySelector('input[name="comment"]').value;
            const postId = form.getAttribute('data-commented-post-id')
            fetch(`/profile/comment/${postId}`,{
                method : 'POST',
                headers : {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // CSRF token
                },
                body : JSON.stringify({
                    comment : comment
                })
            }).then(respone => respone.json())
            .then(data => {
                console.log(data)
                console.log(data.post)
                const id = data.post.id
                console.log(id)
                const comment_div = document.querySelector(`.comment_lists-${id}`);
                console.log(comment_div,id)
                const new_comment = document.createElement('div');
                new_comment.setAttribute('id',`comment-${data.id}`);
                new_comment.classList.add('position-relative');
                const temp = `
                    <div class="p-4 rounded-2 bg-light mb-3">
                        <div class="d-flex align-items-center gap-3">
                            <img src="${data.profile.profile_picture}" alt="" class="rounded-circle" width="33" height="33">
                            
                            <h6 class="fw-semibold mb-0 fs-4"></h6>
                            <span class="fs-2"><span class="p-1 bg-muted rounded-circle d-inline-block">${data.user.username}</span> 5 min ago</span>
                        </div>
                        <p class="my-3">
                            ${data.comment}
                        </p>
                        <div class="d-flex align-items-center">
                            <div class="d-flex align-items-center gap-2">
                            <button class="text-dark d-flex align-items-center justify-content-center bg-light-dark p-2 fs-4 rounded-circle like-cmnt-btn"
                            data-likable_comment-id="${data.id}">
                                <i class="fa fa-thumbs-up" id="i-${data.id}" style="color:blue;"></i>
                            </button>
                            <span class="text-dark fw-semibold" id="comment_like_count-${data.id}">0</span>
                            </div>
                            <div class="d-flex align-items-center gap-2 ms-4">
                            <button class="text-white d-flex align-items-center justify-content-center bg-success p-2 fs-4 rounded-circle"  data-toggle="collapse" data-target="#replay-${data.id}" >
                                <i class="fa fa-arrow-down"></i>
                            </button>
                            <span class="text-dark fw-semibold">0</span>
                            </div>
                            <div class="d-flex align-items-center gap-2 ms-4">
                                <button class="text-white d-flex align-items-center justify-content-center bg-danger p-2 fs-4 rounded-circle delete-cmnt-btn"
                                data-delete-comment-id="${data.id}">
                                <i class="fa fa-trash"></i>
                                </button>
                                <div class="popupContainer" id="popupContainer-${data.id}">
                                    <div id="overlay-${data.id}" class="overlay hidden"></div>
                                    <div id="popupDialog-${data.id}" class="popupDialog hidden">
                                        <button class="close-btn">X</button>
                                        <fieldset>
                                        <legend>Are you sure you want to delete this?</legend>

                                        <form method='post'>
                                            {% csrf_token %}
                                            <div>
                                            <input class="delete" type="radio" id="delete-comment-yes"
                                                    name="delete-comment" value="True" data-comment-id='${data.id}' />
                                            <label for="delete-comment-yes">YES</label>
                                            </div>
                                        
                                            <div>
                                            <input class="delete" type="radio" id="delete-comment-no"
                                                    name="delete-comment" value="False" data-comment-id='${data.id}' />
                                            <label for="delete-comment-no">NO</label>
                                            </div>
                                        </form>
                                        </fieldset>
                                    </div>
                                    </div>
                            </div>
                        </div>
                    </div>
                `
                new_comment.innerHTML = temp;
                comment_div.appendChild(new_comment);
                form.querySelector('input[name="comment"]').value = '';
            })
        })
    })
})