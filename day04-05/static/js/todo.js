function checkBoxClick(event, todo_id, user_id)
{
    //console.log(todo_id, user_id)

    let url = "http://127.0.0.1:8080/update_done";
    let data = { 'todo_id' : todo_id, 'user_id' : user_id, 'done' : event.target.checked}
    fetchUrl(url, data)

}

function fetchUrl(url, data)
{
    fetch(
        // url을 비동기 방식으로 호출한다
        url,
        {
            method : "POST",
            headers : {"Content-Type" : "application/json"},
            body : JSON.stringify(data)
        }
    ).then( function(response){
        if (response.ok)
        {
            console.log('요청이 성공적을 수행되었음')
            if ( response.redirected )
                window.location.href = response.url;
        }
        else
        {
            console.log('요청이 실패했음')
        }
    }

    ).catch(
        console.log('요청중에 요류가 발생함')
    );   
}