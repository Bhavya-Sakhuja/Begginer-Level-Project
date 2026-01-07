import React, { useState } from 'react'
import './ToDoInput.css'
const ToDoInput = (props) => {
  const [Text,ChangeText] = useState("")

  function handleChange(event){
     ChangeText(event.target.value)
  }

  function handleAdd(){
     props.addToDo(Text)
     ChangeText("")
  }

  return (
    <div>
      <p id='detail'>Enter Your Task: </p>
      <label htmlFor="task">
      <input type="text" name="task" id="task" value={Text} onChange={handleChange} placeholder=' Enter Task...'/>
      </label>
      <button id="add_value" onClick={handleAdd}>Add</button>
    </div>
  )
}

export default ToDoInput
