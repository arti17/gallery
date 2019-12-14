function addComment(photo_pk) {
    const csrftoken = getCookie('csrftoken')
    comment = $('#commentText').val()
    $.ajax({
        url: 'http://localhost:8000/api/comments/',
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        data: JSON.stringify({"text": comment, 'photo': photo_pk, 'author': user_id}),
        contentType: 'application/json',
        dataType: 'json',
        success: function (response, status) {
            console.log(response)
            comments = $('#comments')

            const comment = `<div class="card mb-2">
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
            </div>`

            comments.append(comment)
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
