function addComment(photo_pk) {
    const csrftoken = getCookie('csrftoken')
    comment = $('#commentText').val()
    $.ajax({
        url: 'http://localhost:8000/api/comments/',
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        data: JSON.stringify({"text": comment, 'photo': photo_pk}),
        contentType: 'application/json',
        dataType: 'json',
        success: function (response, status) {
            const comments = $('#comments')
            const comment = `<div class="card mb-2" id="comment_${response.id}">
                <div class="card-header text-danger">
                    Комментрий от ${response.author}
                </div>
                <div class="card-body">
                    <blockquote class="blockquote mb-0">
                        <p>${response.text}</p>
                        <footer class="blockquote-footer">Дата
                            добавления: ${response.create_at}</footer>
                    </blockquote>
                </div>
                <button class="btn btn-danger" onclick="deleteComment(${response.id})" id="deleteComment">Удалить комментарий</button>
            </div>`

            comments.append(comment)
        },
        error: function (response, status) {
            console.log(response)
        }
    })
}

function deleteComment(id) {
    const csrftoken = getCookie('csrftoken')
    $.ajax({
        url: `http://localhost:8000/api/comments/${id}/`,
        method: 'DELETE',
        headers: {'X-CSRFToken': csrftoken},
        contentType: 'application/json',
        dataType: 'json',
        success: function (response, status) {
            const deleted_comment = $(`#comment_${id}`)
            console.log(deleted_comment)
            deleted_comment.remove()
        },
        error: function (response, status) {
            console.log(response)
        }
    })
}

function like(photo_pk) {
    const csrftoken = getCookie('csrftoken')
    $.ajax({
        url: `http://localhost:8000/api/like/${photo_pk}/`,
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        contentType: 'application/json',
        dataType: 'json',
        success: function (response, status) {
            const like_btn = $(`#like_${photo_pk}`)
            const dizlike_btn = $(`#dizlike_${photo_pk}`)
            const likes = $(`#likes_${photo_pk}`)
            likes.text(response.rating)
            like_btn.addClass('d-none')
            dizlike_btn.removeClass('d-none')

        },
        error: function (response, status) {
            console.log(response)
        }
    })
}

function dizlike(photo_pk) {
    const csrftoken = getCookie('csrftoken')
    $.ajax({
        url: `http://localhost:8000/api/dizlike/${photo_pk}/`,
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        contentType: 'application/json',
        dataType: 'json',
        success: function (response, status) {
            const like_btn = $(`#like_${photo_pk}`)
            const dizlike_btn = $(`#dizlike_${photo_pk}`)
            const likes = $(`#likes_${photo_pk}`)
            likes.text(response.rating)
            like_btn.removeClass('d-none')
            dizlike_btn.addClass('d-none')
        },
        error: function (response, status) {
            console.log(response)
        }
    })
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
