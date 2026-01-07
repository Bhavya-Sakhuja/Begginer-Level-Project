import React, { useState } from 'react';
import './App.css';
import ToDoInput from './components/ToDoInput';

const App = () => {
  const [Entries, SetEntries] = useState([]); // parent state

  function HandleAppend(newTodo) {
    if (newTodo.trim() === "") return; // empty todo ignore
    SetEntries([...Entries, newTodo]); // add new todo
  }

  return (
    <div className='container'>
      <h1 id='heading'>TO-DO-APP</h1>
      <ToDoInput addToDo={HandleAppend} />

      <div className="box">
        <h3>-----------------------------------------Entered Task----------------------------------------- </h3>
        <div className="entries">
          {Entries.map((entry, index) => (
            <div key={index}>{entry}</div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
