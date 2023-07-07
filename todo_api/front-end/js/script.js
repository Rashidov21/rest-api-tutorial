let todoList = document.querySelector("#todos");
let url = "http://127.0.0.1:8000/todos/";
fetch(url)
  .then((res) => res.json())
  .then((data) => {
    for(let todo of data){
        let li = document.createElement("li")
        let a = document.createElement('a')
        let h4 = document.createElement('h4')
        a.href = `${url}${todo.id}`
        h4.textContent = todo.title
        a.append(h4)
        li.append(a)
        
        li.classList = ["list-group-item"]

        todoList.append(li)
    }
    
  });
