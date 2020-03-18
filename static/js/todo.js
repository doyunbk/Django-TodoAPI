
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


var csrftoken = getCookie('csrftoken');

var clickedtodo = null


// Fetch todolist from backend
function fetchData() {

	var lists = document.getElementById('todo-lists')
	lists.innerHTML = ''
	var url = 'http://0.0.0.0:8000/api/todolist/'


	fetch(url)
	.then((resp) => resp.json())
	.then(function(data){
		console.log('Data:', data)

		var tasks = data

		for (var i in tasks){

			var subject = `<span class="subject"> ${tasks[i].subject}</button>`
			if (tasks[i].status == true){
				subject = `<strike class="subject"> ${tasks[i].subject}</strike>`
			}

			var item = `
						<div id="data-row-${i}" class="task-wrapper flex list-wrapper">
							<div class="subject">
								${subject}
							</div>
							<div class="btn-flex">
								<button class="btn btn-sm btn-primary update"> Update </button>
							</div>
							<div class="btn-flex">
								<button class="btn btn-sm btn-danger delete"> Delete </button>
							</div>
							<div class="btn-flex">
								<button class="btn btn-sm btn-warning done"> Done </button>
							</div>
						</div>

					`
					lists.innerHTML += item
		}

		for (var i in tasks){
				var updated = document.getElementsByClassName('update')[i]
				var deleted = document.getElementsByClassName('delete')[i]
				var done = document.getElementsByClassName('done')[i]
				var subject = document.getElementsByClassName('subject')[i]


				updated.addEventListener('click', (function(todo){
					
					return function(){
						updateTodo(todo)
					}
				})(tasks[i]))

				deleted.addEventListener('click', (function(todo){
					
					return function(){
						deleteTodo(todo)
					}
				})(tasks[i]))

				done.addEventListener('click', (function(todo){
					
					return function(){
						doneTodo(todo)
					}
				})(tasks[i]))
		}

	})

}



var forms = document.getElementById('todo-form')
var form = document.getElementById('form')

forms.addEventListener('submit', function(evt){
evt.preventDefault()
console.log('form submitted')
	
var url = 'http://0.0.0.0:8000/api/createtask/'

if (clickedtodo != null) {
		var url = `http://0.0.0.0:8000/api/updatetask/${clickedtodo.id}`
		clickedtodo = null
}


var subject = document.getElementById('subject').value
	
fetch (url, {
	method: 'POST',
	headers: {
		'Content-type': 'application/json',
		'X-CSRFToken': csrftoken,
	},
	body: JSON.stringify({'subject': subject})
}

).then(function(response){
	fetchData()
	form.reset()
	})
})



function updateTodo(todo){

	console.log(todo)
	clickedtodo = todo
	document.getElementById('subject').value = clickedtodo.subject

}

function deleteTodo(todo){
	console.log('delete clicked')
	var url = `http://0.0.0.0:8000/api/deletetask/${todo.id}`
	fetch(url, {
		method:'DELETE',
		headers:{
			'Content-type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
	}).then((response) => {
		fetchData()
	}).catch(function() {
		console.log('you are not an owner')
	})
}

function doneTodo(todo){

	console.log('done clicked')
	var url = `http://0.0.0.0:8000/api/updatetask/${todo.id}`
	
	todo.status = !todo.status

	fetch(url, {
		method:'POST',
		headers:{
			'Content-type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body:JSON.stringify({'subject':todo.subject, 'status':todo.status})
	}).then((response) => {
		fetchData()
	})
}
















